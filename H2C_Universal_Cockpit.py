import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, glob, zipfile, io, datetime, tempfile

# --- NOYAU SCIENTIFIQUE H2C (VERSION AUTO-CONSISTANTE COUPLÉE AVEC LOI UNIVERSELLE) ---
class H2CSolverPro:
    """
    Solveur H2C de grade recherche incluant :
    1. Ancrage cosmologique sur Lambda.
    2. Rétroaction itérative sur le rapport Masse/Luminosité (M/L).
    3. Correction géométrique adaptative du disque.
    4. Loi d'Auto-Correction Universelle (Transfer Function) extraite du catalogue SPARC.
    """
    def __init__(self, a0=5.4546e-10):
        self.a0 = a0 
        self.KPC_TO_M = 3.085677581491367e19
        self.KM_S_TO_M_S = 1000.0
        
        # Loi d'Auto-Correction Universelle (Points de contrôle)
        self.x_nodes = np.array([-6.0, -3.3, -2.7, -2.5, -1.7, -1.0, -0.5, 0.0, 1.0])
        self.y_nodes = np.array([1.0,  1.0,  0.92, 0.88, 0.95, 0.95, 0.99, 1.0, 1.0])

    def _get_correction(self, a_n):
        log_ratio = np.log10(np.maximum(a_n, 1e-25) / (self.a0 / 4.54) + 1e-25) # On ramène à l'échelle MOND pour la table
        # Interpolation linéaire manuelle pour éviter la dépendance scipy dans l'exécutable
        return np.interp(log_ratio, self.x_nodes, self.y_nodes)

    def solve(self, df_galaxy, max_iter=15, tol=1e-4, use_universal_law=True):
        r_m = df_galaxy['Rad'].values * self.KPC_TO_M
        v_gas = df_galaxy['V_gas'].values
        v_disk = df_galaxy['V_disk'].values
        v_bulge = df_galaxy['V_bulge'].values
        
        # Initialisation Newtonienne
        v_n2_raw = np.sign(v_gas)*(v_gas**2) + 0.5*(v_disk**2) + 0.7*(v_bulge**2)
        a_n = (np.maximum(1e-15, v_n2_raw) * (self.KM_S_TO_M_S**2)) / (r_m + 1e-10)
        a_n_new = a_n.copy()
        
        y = a_n / self.a0
        eta = 1.0 - np.exp(-np.sqrt(np.maximum(1e-12, y)))
        
        iters_done = 0
        for i in range(max_iter):
            iters_done = i + 1
            eta_old = eta.copy()
            ml_d = 0.50 * (1.0 + 0.15 * np.exp(-y))
            ml_b = 0.70 * (1.0 + 0.10 * np.exp(-y))
            gamma_geom = 1.0 - 0.15 * eta

            v_bar_sq = (np.sign(v_gas)*(v_gas**2) + ml_d*(v_disk**2) + ml_b*(v_bulge**2)) * gamma_geom
            a_n_new = (np.maximum(1e-15, v_bar_sq) * (self.KM_S_TO_M_S**2)) / (r_m + 1e-10)
            y = a_n_new / self.a0
            eta = 1.0 - np.exp(-np.sqrt(np.maximum(1e-12, y)))

            if np.max(np.abs(eta - eta_old)) < tol:
                break

        # Formule de transition universelle H2C
        mu_inv = np.sqrt(0.5 + 0.5 * np.sqrt(1.0 + 4.0 / (y**2 + 1e-15)))
        
        # Application optionnelle de la Loi Universelle d'Auto-Correction
        if use_universal_law:
            corr = self._get_correction(a_n_new)
            a_h2c = a_n_new * mu_inv * (1.0 / np.maximum(corr, 0.1))
        else:
            a_h2c = a_n_new * mu_inv
            
        v_h2c = np.sqrt(a_h2c * r_m) / self.KM_S_TO_M_S
        
        res = df_galaxy.copy()
        res['V_h2c'] = v_h2c
        res['V_newton'] = np.sqrt(np.maximum(0, v_gas**2 + v_disk**2 + v_bulge**2))
        return res, iters_done

# --- INTERFACE UTILISATEUR (UX/UI) ---
st.set_page_config(page_title="H2C Cockpit V8.5-R", page_icon="🌌", layout="wide")

st.title("🌌 Cockpit H2C : Solveur Gravitationnel Universel")
st.markdown("*Analyse cinématique automatisée avec Loi d'Auto-Correction Universelle.*")

# Sidebar
st.sidebar.header("📁 Source de Données")
uploaded_zip = st.sidebar.file_uploader("Archive SPARC (.zip)", type="zip")

# Paramètres Physiques
st.sidebar.divider()
st.sidebar.subheader("⚙️ Paramètres Physiques")
anchor_mode = st.sidebar.selectbox("Ancrage Cosmologique (a0)", ["H2C Théorique (5.45e-10)", "Empirique MOND (1.20e-10)"])
a0_val = 5.4546e-10 if "Théorique" in anchor_mode else 1.2e-10
use_law = st.sidebar.checkbox("Appliquer la Loi d'Auto-Correction Universelle", value=True)

if not uploaded_zip:
    st.info("👋 Bienvenue. Veuillez charger l'archive SPARC (`Rotmod_LTG.zip`) pour activer le solveur.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NGC_4414_%28NASA-Hubble%29.jpg/1200px-NGC_4414_%28NASA-Hubble%29.jpg", use_column_width=True)
    st.stop()

# Chargement Catalogue
@st.cache_data
def load_and_extract(zip_bytes):
    galaxies = {}
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
            z.extractall(tmpdir)
            files = glob.glob(os.path.join(tmpdir, "**", "*.dat*"), recursive=True)
            for f in files:
                try:
                    data = np.loadtxt(f, comments='#')
                    if data.size > 0 and data.shape[1] >= 6:
                        name = os.path.basename(f).split('.')[0]
                        galaxies[name] = pd.DataFrame(data[:,:6], columns=['Rad','V_obs','V_err','V_gas','V_disk','V_bulge'])
                except: continue
    return galaxies

galaxies_dict = load_and_extract(uploaded_zip.read())
selected_target = st.sidebar.selectbox("Sélectionner la Galaxie", sorted(list(galaxies_dict.keys())))

# Exécution du Solveur
if selected_target:
    df_gal = galaxies_dict[selected_target]
    solver = H2CSolverPro(a0=a0_val)
    df_res, iters = solver.solve(df_gal, use_universal_law=use_law)
    
    # Statistiques
    mask_valid = ~np.isnan(df_res['V_obs'])
    rmse_n = np.sqrt(np.mean((df_res['V_obs'][mask_valid] - df_res['V_newton'][mask_valid])**2))
    rmse_h = np.sqrt(np.mean((df_res['V_obs'][mask_valid] - df_res['V_h2c'][mask_valid])**2))
    gain = ((rmse_n - rmse_h) / np.maximum(rmse_n, 1e-5)) * 100
    
    # Dashboard de Performance
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📉 RMSE Newtonien", f"{rmse_n:.2f} km/s")
    c2.metric("🚀 RMSE H2C", f"{rmse_h:.2f} km/s", delta=f"-{gain:.1f}%")
    c3.metric("🔄 Itérations", iters)
    c4.metric("✨ Points", len(df_res))
    
    st.divider()
    
    # Graphique
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.errorbar(df_res['Rad'], df_res['V_obs'], yerr=df_res['V_err'], fmt='ko', label='Observations SPARC', alpha=0.5, capsize=3)
    ax.plot(df_res['Rad'], df_res['V_newton'], color='red', linestyle='--', label='Newton Pur (Baryons)')
    ax.plot(df_res['Rad'], df_res['V_h2c'], color='blue', linewidth=3, label='Modèle H2C Auto-Correction')
    
    ax.set_xlabel("Rayon (kpc)", fontsize=12)
    ax.set_ylabel("Vitesse de rotation (km/s)", fontsize=12)
    ax.set_title(f"Profil Cinématique : {selected_target}", fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    st.pyplot(fig)
    
    with st.expander("📊 Voir les données brutes"):
        st.dataframe(df_res.head(20))
