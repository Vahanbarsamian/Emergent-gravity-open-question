import numpy as np

# =============================================================================
# SOLVEUR H2C V1.4-2D.2 : CORRECTION NOETHER U(1) ET CONVERGENCE NON LINÉAIRE
# =============================================================================

def apply_dealiasing_2d_23(field_k, Nx, Ny):
    cutoff_x = Nx // 3
    cutoff_y = Ny // 3
    field_k_filtered = field_k.copy()
    field_k_filtered[cutoff_x:-cutoff_x, :] = 0.0
    field_k_filtered[:, cutoff_y:-cutoff_y] = 0.0
    return field_k_filtered

def rhs_H2C_2D_complex(Phi, dPhi_dt, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny):
    """
    Calcule le second membre de l'équation H2C 2D.
    K_mat: (K00, K01, K02, K11, K12, K22)
    """
    K00, K01, K02, K11, K12, K22 = K_mat
    
    Phi_k = np.fft.fft2(Phi)
    dPhi_dt_k = np.fft.fft2(dPhi_dt)
    
    d2Phi_dx2 = np.fft.ifft2(-(K_vec_x**2) * Phi_k)
    d2Phi_dy2 = np.fft.ifft2(-(K_vec_y**2) * Phi_k)
    d2Phi_dxdy = np.fft.ifft2(-K_vec_x * K_vec_y * Phi_k)
    
    d2Phi_dtdx = np.fft.ifft2(1j * K_vec_x * dPhi_dt_k)
    d2Phi_dtdy = np.fft.ifft2(1j * K_vec_y * dPhi_dt_k)
    
    if lambda_p != 0.0:
        abs_sq = np.abs(Phi)**2
        dV_dPhi = lambda_p * (abs_sq - phi0**2) * Phi
        dV_dPhi_k = apply_dealiasing_2d_23(np.fft.fft2(dV_dPhi), Nx, Ny)
        dV_dPhi_filtered = np.fft.ifft2(dV_dPhi_k)
    else:
        dV_dPhi_filtered = 0.0
    
    d2Phi_dt2 = -(
        2.0 * K01 * d2Phi_dtdx + 
        2.0 * K02 * d2Phi_dtdy + 
        K11 * d2Phi_dx2 + 
        2.0 * K12 * d2Phi_dxdy + 
        K22 * d2Phi_dy2 - 
        dV_dPhi_filtered
    ) / K00
    
    return dPhi_dt, d2Phi_dt2

def run_rk4_step(Phi, dPhi_dt, dt, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny):
    p, v_p = Phi, dPhi_dt
    k1_p, k1_v = rhs_H2C_2D_complex(p, v_p, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny)
    k2_p, k2_v = rhs_H2C_2D_complex(p + 0.5*dt*k1_p, v_p + 0.5*dt*k1_v, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny)
    k3_p, k3_v = rhs_H2C_2D_complex(p + 0.5*dt*k2_p, v_p + 0.5*dt*k2_v, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny)
    k4_p, k4_v = rhs_H2C_2D_complex(p + dt*k3_p, v_p + dt*k3_v, K_mat, K_vec_x, K_vec_y, lambda_p, phi0, Nx, Ny)
    
    Phi_next = p + (dt / 6.0) * (k1_p + 2.0*k2_p + 2.0*k3_p + k4_p)
    dPhi_dt_next = v_p + (dt / 6.0) * (k1_v + 2.0*k2_v + 2.0*k3_v + k4_v)
    return Phi_next, dPhi_dt_next

def compute_noether_charge_2d(Phi, dPhi_dt, dx, dy, K_vec_x, K_vec_y, K_mat):
    """
    Calcule la charge de Noether U(1) exacte j^0.
    """
    K00, K01, K02, K11, K12, K22 = K_mat
    
    Phi_k = np.fft.fft2(Phi)
    dPhi_dx = np.fft.ifft2(1j * K_vec_x * Phi_k)
    dPhi_dy = np.fft.ifft2(1j * K_vec_y * Phi_k)
    
    # Courant de Noether temporel exact j^0 sous métrique effective
    j0 = (
        K00 * np.imag(np.conj(Phi) * dPhi_dt) +
        K01 * np.imag(np.conj(Phi) * dPhi_dx) +
        K02 * np.imag(np.conj(Phi) * dPhi_dy)
    )
    
    return np.sum(j0).real * dx * dy

def compute_hamiltonian_2d(Phi, dPhi_dt, dx, dy, K_vec_x, K_vec_y, K_mat, lambda_p, phi0):
    """
    Calcule l'Hamiltonien du système.
    """
    K00, K01, K02, K11, K12, K22 = K_mat
    
    Phi_k = np.fft.fft2(Phi)
    dPhi_dx = np.fft.ifft2(1j * K_vec_x * Phi_k)
    dPhi_dy = np.fft.ifft2(1j * K_vec_y * Phi_k)
    
    if lambda_p != 0.0:
        V_Phi = 0.25 * lambda_p * (np.abs(Phi)**2 - phi0**2)**2
    else:
        V_Phi = 0.0
        
    H_density = -0.5 * K00 * np.abs(dPhi_dt)**2 + \
                 0.5 * K11 * np.abs(dPhi_dx)**2 + \
                 K12 * np.real(np.conj(dPhi_dx) * dPhi_dy) + \
                 0.5 * K22 * np.abs(dPhi_dy)**2 + V_Phi
                 
    return np.sum(np.real(H_density)) * dx * dy
