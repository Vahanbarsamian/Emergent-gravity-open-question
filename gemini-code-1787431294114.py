import numpy as np

def simuler_masse_emergente(R_max=10.0, N_points=500, C_c=0.2000, kappa=2.0, G=1.0, c=1.0, omega0=1.0):
    """
    Simulation du profil de masse et de courbure emergente a partir d'une perturbation
    locale du champ de coherence C(r).
    """
    r = np.linspace(0.01, R_max, N_points)
    dr = r[1] - r[0]
    
    # 1. Profil de coherence injecte C(r) : saturation a C=1 au cœur, retour vers C_c
    # r0 = rayon du cœur d'intrication
    r0 = 0.5
    C_r = C_c + (1.0 - C_c) * np.exp(-(r / r0)**2)
    
    # 2. Integration de la Masse Emergente M(r)
    # M(r) = (c^2 * kappa / (G * omega0^2)) * int_0^r 4*pi*r'^2 * (C(r') - C_c) dr'
    integrande_M = 4.0 * np.pi * (r**2) * (C_r - C_c)
    M_r = (c**2 * kappa / (G * omega0**2)) * np.cumsum(integrande_M) * dr
    
    M_totale = M_r[-1]
    
    # 3. Potentiel gravitationnel emergent Phi(r)
    # Phi(r) = - (G * M(r) / r) - correction_taille_coherente
    Phi_r = - (G * M_r / r)
    
    # 4. Acceleration emergente g(r) = -dPhi/dr
    g_emergente = np.gradient(-Phi_r, dr)
    
    # Acceleration newtonienne theorique pour une masse ponctuelle M_totale
    g_newton = G * M_totale / (r**2)
    
    # 5. Detection du Rayon de Confinement Minimal (pas de singularite r -> 0)
    # Le champ g_emergente tend vers 0 au centre r -> 0 au lieu de diverger vers l'infini
    g_max_idx = np.argmax(g_emergente)
    r_min_confinement = r[g_max_idx]
    
    return {
        "r": r,
        "C_r": C_r,
        "M_r": M_r,
        "M_totale": M_totale,
        "g_emergente": g_emergente,
        "g_newton": g_newton,
        "r_min_confinement": r_min_confinement
    }

# Execution
res = simuler_masse_emergente()

print("=== RESULTATS DU MODULE DE MASSE EMERGENTE M(C) ===")
print(f"Masse totale emergente M_tot    : {res['M_totale']:.4f} (unites arbitraires)")
print(f"Rayon de confinement minimal r_min : {res['r_min_confinement']:.3f} (seuil de saturation sans singularite)")
print(f"Coherence au cœur r -> 0        : {res['C_r'][0]:.4f} (Saturation absolue C = 1.0)")
print(f"Coherence asymptotique r -> inf  : {res['C_r'][-1]:.4f} (Retour au vide critique C_c = 0.2000)")