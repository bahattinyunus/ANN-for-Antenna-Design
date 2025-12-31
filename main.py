import argparse
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from generator import generate_antenna_data
from model import build_ann_model

def train():
    # 1. Generate/Load Data
    data_file = "antenna_dataset.csv"
    if not os.path.exists(data_file):
        generate_antenna_data()
    
    df = pd.read_csv(data_file)
    
    # 2. Preprocessing
    X = df[['W_mm', 'L_mm', 'h_mm', 'er']].values
    y = df['fr_GHz'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 3. Build & Train Model
    model = build_ann_model()
    print("Training the MLP model (this may take a few moments)...")
    model.fit(X_train_scaled, y_train)
    
    # 4. Evaluation
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Test Loss (MSE): {mse:.4f}")
    print(f"Test MAE: {mae:.4f}")
    
    # 5. Save Model & Scaler
    joblib.dump(model, 'antenna_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Model and Scaler saved as antenna_model.pkl and scaler.pkl")
    
    # 6. Plotting (Simplified since sklearn doesn't provide loss history in the same way by default)
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.title('Actual vs Predicted Resonant Frequency')
    plt.xlabel('Actual (GHz)')
    plt.ylabel('Predicted (GHz)')
    plt.grid(True)
    plt.savefig('prediction_plot.png')
    print("Prediction plot saved as prediction_plot.png")

def predict(W, L, h, er):
    if not os.path.exists('antenna_model.pkl') or not os.path.exists('scaler.pkl'):
        print("Error: No trained model or scaler found. Run with --train first.")
        return

    model = joblib.load('antenna_model.pkl')
    scaler = joblib.load('scaler.pkl')
    
    inputs = np.array([[W, L, h, er]])
    inputs_scaled = scaler.transform(inputs)
    
    prediction = model.predict(inputs_scaled)
    print(f"\nPredicted Resonant Frequency for W={W}, L={L}, h={h}, er={er}:")
    print(f"--> {prediction[0]:.4f} GHz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANN for Antenna Design CLI")
    parser.add_argument("--train", action="store_true", help="Train the model")
    parser.add_argument("--predict", action="store_true", help="Predict frequency")
    parser.add_argument("--W", type=float, default=40.0)
    parser.add_argument("--L", type=float, default=40.0)
    parser.add_argument("--H", type=float, default=1.6)
    parser.add_argument("--ER", type=float, default=4.4)
    
    args = parser.parse_args()
    
    if args.train:
        train()
    elif args.predict:
        predict(args.W, args.L, args.H, args.ER)
    else:
        parser.print_help()
