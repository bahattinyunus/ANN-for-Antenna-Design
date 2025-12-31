import joblib
import numpy as np
from scipy.optimize import minimize
import os

class AntennaInverseOptimizer:
    def __init__(self, model_path='antenna_model.pkl', scaler_path='scaler.pkl'):
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            raise FileNotFoundError("Model or Scaler not found. Please train the model first.")
        
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def _cost_function(self, params, target_f, h, er):
        """
        Cost function to minimize: squared error between target frequency 
        and model prediction.
        params: [W, L]
        """
        W, L = params
        # Prepare input for the model: [W, L, h, er]
        input_data = np.array([[W, L, h, er]])
        input_scaled = self.scaler.transform(input_data)
        
        predicted_f = self.model.predict(input_scaled)[0]
        return (target_f - predicted_f)**2

    def optimize(self, target_f, h, er, initial_guess=[40.0, 40.0]):
        """
        Finds optimal W and L for a given target frequency and substrate.
        Bounds are set based on typical microstrip patch antenna dimensions.
        """
        # Bounds for W and L (in mm)
        bounds = [(10.0, 100.0), (10.0, 100.0)]
        
        result = minimize(
            self._cost_function, 
            initial_guess, 
            args=(target_f, h, er),
            bounds=bounds,
            method='L-BFGS-B'
        )
        
        if result.success:
            return result.x  # [W_opt, L_opt]
        else:
            raise ValueError("Optimization failed: " + result.message)

def run_inverse_design(target_f, h, er):
    optimizer = AntennaInverseOptimizer()
    print(f"\n[TERSİNE TASARIM BAŞLATILIYOR]")
    print(f"Hedef Frekans: {target_f} GHz")
    print(f"Sabit Parametreler: h={h} mm, er={er}")
    
    try:
        w_opt, l_opt = optimizer.optimize(target_f, h, er)
        print(f"\n[OPTIMİZASYON BAŞARILI]")
        print(f"Önerilen Genişlik (W): {w_opt:.4f} mm")
        print(f"Önerilen Uzunluk (L): {l_opt:.4f} mm")
        
        # Verify result
        predicted_f = optimizer.model.predict(optimizer.scaler.transform([[w_opt, l_opt, h, er]]))[0]
        print(f"Doğrulama Tahmini: {predicted_f:.4f} GHz (Hata: {abs(target_f-predicted_f):.6f})")
        
        return w_opt, l_opt
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None
