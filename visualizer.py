import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import joblib
import os

def visualize_3d_parameter_surface():
    """
    Generates a 3D surface plot showing how W and L affect fr (Frequency).
    """
    if not os.path.exists('antenna_model.pkl') or not os.path.exists('scaler.pkl'):
        print("Error: No trained model or scaler found. Run 'python main.py --train' first.")
        return

    model = joblib.load('antenna_model.pkl')
    scaler = joblib.load('scaler.pkl')

    # Create grid for W and L
    W_vals = np.linspace(20, 60, 50)
    L_vals = np.linspace(20, 60, 50)
    W_grid, L_grid = np.meshgrid(W_vals, L_vals)
    
    # Constant parameters for the slice
    h_fixed = 1.6
    er_fixed = 4.4
    
    # Prepare input for prediction
    # Reshape to (2500, 4)
    grid_points = np.column_stack([
        W_grid.ravel(), 
        L_grid.ravel(), 
        np.full_like(W_grid.ravel(), h_fixed), 
        np.full_like(W_grid.ravel(), er_fixed)
    ])
    
    # Scale and predict
    grid_points_scaled = scaler.transform(grid_points)
    fr_pred = model.predict(grid_points_scaled)
    fr_grid = fr_pred.reshape(W_grid.shape)

    # Plotting
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surface = ax.plot_surface(W_grid, L_grid, fr_grid, cmap='viridis', edgecolor='none', alpha=0.8)
    
    ax.set_title(f'Anten Boyutları ve Rezonans Frekansı İlişkisi (h={h_fixed}, er={er_fixed})', pad=20)
    ax.set_xlabel('Width (W) [mm]')
    ax.set_ylabel('Length (L) [mm]')
    ax.set_zlabel('Frequency (fr) [GHz]')
    
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='Frekans (GHz)')
    
    plt.savefig('3d_parameter_surface.png')
    print("3D parameter surface plot saved as 3d_parameter_surface.png")
    plt.close()

if __name__ == "__main__":
    visualize_3d_parameter_surface()
