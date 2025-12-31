import argparse
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from generator import generate_antenna_data
from model import build_ann_model
from optimizer import run_inverse_design

def train(use_cv=False):
    # ... (existing train function)
    # Note: I'm keeping the original train function logic intact
    data_file = "antenna_dataset.csv"
    if not os.path.exists(data_file):
        generate_antenna_data()
    
    df = pd.read_csv(data_file)
    X = df[['W_mm', 'L_mm', 'h_mm', 'er']].values
    y = df['fr_GHz'].values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    if use_cv:
        print(f"Executing 5-Fold Cross Validation...")
        model_cv = build_ann_model()
        scores = cross_val_score(model_cv, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
        mse_scores = -scores
        print(f"CV MSE Scores: {mse_scores}")
        print(f"Mean MSE: {mse_scores.mean():.4f} (+/- {mse_scores.std():.4f})")
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = build_ann_model()
    print("Training the final MLP model...")
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- Model Performans Özeti ---")
    print(f"MSE: {mse:.4f}")
    print(f"MAE: {mae:.4f}")
    print(f"R² Skoru: {r2:.4f}")
    
    joblib.dump(model, 'antenna_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("\nModel and Scaler saved as antenna_model.pkl and scaler.pkl")
    
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='blue', label='Tahminler')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='İdeal Çizgi')
    plt.title('Hata Analizi: Gerçek vs Tahmin Edilen Rezonans Frekansı')
    plt.xlabel('Gerçek Frekans (GHz)')
    plt.ylabel('Tahmin Edilen Frekans (GHz)')
    plt.legend()
    plt.grid(True, alpha=0.3)
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
    print(f"\n[TAHMİN SONUCU]")
    print(f"Parametreler: W={W}, L={L}, h={h}, er={er}")
    print(f"Tahmin Edilen Rezonans Frekansı: {prediction[0]:.4f} GHz")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANN for Antenna Design CLI")
    parser.add_argument("--train", action="store_true", help="Modeli eğit")
    parser.add_argument("--cv", action="store_true", help="Cross-validation gerçekleştir")
    parser.add_argument("--predict", action="store_true", help="Frekans tahmini yap")
    parser.add_argument("--inverse", action="store_true", help="Tersine tasarım (frekanstan boyut tahmini) yap")
    parser.add_argument("--target_f", type=float, default=2.4, help="Hedef rezonans frekansı (GHz)")
    parser.add_argument("--W", type=float, default=40.0)
    parser.add_argument("--L", type=float, default=40.0)
    parser.add_argument("--H", type=float, default=1.6)
    parser.add_argument("--ER", type=float, default=4.4)
    
    args = parser.parse_args()
    
    if args.train:
        train(use_cv=args.cv)
    elif args.predict:
        predict(args.W, args.L, args.H, args.ER)
    elif args.inverse:
        run_inverse_design(args.target_f, args.H, args.ER)
    else:
        parser.print_help()
