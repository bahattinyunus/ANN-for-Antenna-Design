import numpy as np
import pandas as pd
import os

def generate_antenna_data(num_samples=1000, filename="antenna_dataset.csv"):
    """
    Generates synthetic data for a microstrip patch antenna.
    Formulas are simplified for demonstration purposes.
    """
    # Physical Constants
    c0 = 3e8  # Speed of light in m/s

    # Randomly sample physical parameters
    # W: Width (mm), L: Length (mm), h: Height (mm), er: Dielectric constant
    W = np.random.uniform(20, 60, num_samples)
    L = np.random.uniform(20, 60, num_samples)
    h = np.random.uniform(0.5, 3.2, num_samples)
    er = np.random.uniform(2.2, 10.2, num_samples)

    # Calculate effective dielectric constant (er_eff)
    # er_eff = (er + 1)/2 + (er - 1)/2 * (1 + 12*h/W)**-0.5
    er_eff = (er + 1) / 2 + (er - 1) / 2 * (1 + 12 * h / W)**-0.5

    # Calculate Resonant Frequency (fr) in GHz
    # fr = c0 / (2 * L * sqrt(er_eff))
    # Convert L from mm to meters (* 1e-3) and result to GHz (* 1e-9)
    fr = (c0 / (2 * (L * 1e-3) * np.sqrt(er_eff))) * 1e-9

    # Add some "simulated noise" to mimic EM solver variations
    fr += np.random.normal(0, 0.05, num_samples)

    # Create DataFrame
    df = pd.DataFrame({
        'W_mm': W,
        'L_mm': L,
        'h_mm': h,
        'er': er,
        'fr_GHz': fr
    })

    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Dataset generated with {num_samples} samples: {filename}")
    return filename

if __name__ == "__main__":
    generate_antenna_data()
