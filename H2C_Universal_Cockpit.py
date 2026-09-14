import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, glob, zipfile, io, datetime, tempfile

# --- CORE H2C SOLVER ---
class H2CSolver:
    def __init__(self, a0=1.2e-10):
        self.a0 = a0 # Cosmological anchor c^2 * sqrt(Lambda/3)

    def calculate(self, df):
        res = df.copy()
        kpc_m, km_ms = 3.086e19, 1000.0
        r_m = res['Rad'].values * kpc_m
        
        # Newtonian Acceleration from Baryons
        v_n2 = res['V_gas']**2 + res['V_disk']**2 + res['V_bulge']**2
        a_n = (v_n2 * (km_ms**2)) / (r_m + 1e-10)
        
        # H2C Universal Transition Function (Derived from S2 dynamics)
        y = a_n / self.a0
        mu_inv = np.sqrt(0.5 + 0.5 * np.sqrt(1.0 + 4.0 / (y**2 + 1e-15)))
        
        # Emergent Velocity
        a_h2c = a_n * mu_inv
        res['V_h2c'] = np.sqrt(a_h2c * r_m) / km_ms
        res['V_newton'] = np.sqrt(v_n2)
        return res

# --- UI CONFIGURATION ---
st.set_page_config(page_title="H2C Universal Cockpit", page_icon="🌌", layout="wide")

st.title("🌌 H2C Universal Cockpit")
st.markdown("*Emergent Gravity Solver - Automated Validation on SPARC Data*")

# Sidebar
st.sidebar.header("📁 Data Source")
uploaded = st.sidebar.file_uploader("Upload SPARC Archive (Rotmod_LTG.zip)", type="zip")

if not uploaded:
    st.info("👋 Please upload the SPARC ZIP archive in the sidebar to start analysis.")
    st.stop()

# Data Processing
@st.cache_data
def load_sparc(zip_bytes):
    galaxies = {}
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
            z.extractall(tmp)
            files = glob.glob(os.path.join(tmp, "**", "*.dat*"), recursive=True)
            for f in files:
                try:
                    data = np.loadtxt(f, comments='#')
                    name = os.path.basename(f).split('.')[0]
                    galaxies[name] = pd.DataFrame(data[:,:6], columns=['Rad','V_obs','V_err','V_gas','V_disk','V_bulge'])
                except: continue
    return galaxies

galaxies = load_sparc(uploaded.read())
target = st.sidebar.selectbox("Select Galaxy Target", sorted(list(galaxies.keys())))

if target:
    df = galaxies[target]
    solver = H2CSolver()
    final = solver.calculate(df)
    
    # Metrics
    rmse_n = np.sqrt(np.mean((final['V_obs'] - final['V_newton'])**2))
    rmse_h = np.sqrt(np.mean((final['V_obs'] - final['V_h2c'])**2))
    gain = ((rmse_n - rmse_h) / rmse_n) * 100
    
    c1, c2, c3 = st.columns(3)
    c1.metric("RMSE Newton", f"{rmse_n:.2f} km/s")
    c2.metric("RMSE H2C", f"{rmse_h:.2f} km/s", delta=f"-{gain:.1f}%")
    c3.metric("Data Points", len(df))
    
    # Visualization
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.errorbar(final['Rad'], final['V_obs'], yerr=final['V_err'], fmt='ko', label='Observation (V_obs)', alpha=0.4)
    ax.plot(final['Rad'], final['V_newton'], 'r--', label='Newton (Baryons)')
    ax.plot(final['Rad'], final['V_h2c'], 'b-', lw=3, label='H2C Emergence')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Rotation Velocity (km/s)")
    ax.set_title(f"Rotation Curve: {target}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    
    st.divider()
    st.subheader("📊 Raw Data comparison")
    st.dataframe(final[['Rad','V_obs','V_newton','V_h2c']].head(10))
