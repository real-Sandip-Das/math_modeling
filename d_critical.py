import numpy as np

def analyze_schnakenberg(a, b, gamma=1.0, Du=1.0):
    """
    Calculates the required diffusion coefficients for Turing patterns.
    """
    # 1. Steady State (u*, v*)
    u_ss = a + b
    v_ss = b / (u_ss**2)

    # 2. Jacobian elements at steady state
    # f = a - u + u^2*v  =>  fu = -1 + 2uv, fv = u^2
    # g = b - u^2*v      =>  gu = -2uv,     gv = -u^2
    fu = gamma * (-1 + 2 * u_ss * v_ss)
    fv = gamma * (u_ss**2)
    gu = gamma * (-2 * u_ss * v_ss)
    gv = gamma * (-u_ss**2)

    # 3. Stability Checks
    trace = fu + gv
    det = fu * gv - fv * gu
    
    if trace >= 0 or det <= 0:
        return "The steady state is unstable without diffusion. Turing patterns won't form."

    # 4. Solve for critical diffusion ratio d = Dv/Du
    # Derived from (d*fu + gv)^2 - 4*d*(det) = 0
    # Equation: (fu^2)d^2 + (2*fu*gv - 4*det)d + (gv^2) = 0
    A = fu**2
    B = 2 * fu * gv - 4 * det
    C = gv**2
    
    discriminant = B**2 - 4 * A * C
    
    if discriminant < 0:
        return "No real critical d exists for these a, b values."

    # We take the larger root for the threshold
    d_crit = (-B + np.sqrt(discriminant)) / (2 * A)
    Dv_min = d_crit * Du

    return {
        "Steady State (u, v)": (round(u_ss, 4), round(v_ss, 4)),
        "Jacobian [fu, fv, gu, gv]": [round(fu, 4), round(fv, 4), round(gu, 4), round(gv, 4)],
        "Critical Ratio (d)": round(d_crit, 4),
        "Minimum Dv (for Du=1)": round(Dv_min, 4)
    }

# --- Usage ---
a_val, b_val, gamma_val = 0.01, 2, 1
params = analyze_schnakenberg(a_val, b_val, gamma_val)
print(params)

import numpy as np

def find_params_from_equilibrium(u_ss, v_ss, gamma=1.0, Du=1.0):
    """
    Finds a, b from equilibrium (u, v) and calculates Turing stability.
    """
    # 1. Solve for a and b
    b = v_ss * (u_ss**2)
    a = u_ss - b
    
    if a <= 0:
        return f"Invalid Equilibrium: a would be {a:.4f}. Must have u*v < 1."

    # 2. Jacobian elements at steady state
    # fu = -1 + 2uv, fv = u^2, gu = -2uv, gv = -u^2
    fu = gamma * (-1 + 2 * u_ss * v_ss)
    fv = gamma * (u_ss**2)
    gu = gamma * (-2 * u_ss * v_ss)
    gv = gamma * (-u_ss**2)

    # 3. Stability Checks
    trace = fu + gv
    det = fu * gv - fv * gu
    
    if trace >= 0 or det <= 0:
        return f"Steady state (u={u_ss}, v={v_ss}) is naturally unstable. No Turing possible."

    # 4. Critical diffusion ratio d = Dv/Du
    A = fu**2
    B = 2 * fu * gv - 4 * det
    C = gv**2
    
    discriminant = B**2 - 4 * A * C
    
    if discriminant < 0:
        return "No Turing space exists for this equilibrium."

    d_crit = (-B + np.sqrt(discriminant)) / (2 * A)
    
    return {
        "Calculated a": round(a, 4),
        "Calculated b": round(b, 4),
        "Critical Ratio (d)": round(d_crit, 4),
        "Min Dv (for Du=1)": round(d_crit * Du, 4),
        "Check (u*v)": round(u_ss * v_ss, 4) # Must be < 1
    }

# Example: Target equilibrium u=1.0, v=0.9
target_u, target_v = 0.5, 0.45
results = find_params_from_equilibrium(target_u, target_v,gamma=1.2)
print(results)
