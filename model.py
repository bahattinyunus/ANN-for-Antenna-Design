from sklearn.neural_network import MLPRegressor

def build_ann_model():
    """
    Builds a Multilayer Perceptron (MLP) for frequency prediction using Scikit-learn.
    """
    model = MLPRegressor(
        hidden_layer_sizes=(128, 64, 32),
        activation='relu',
        solver='adam',
        max_iter=500,
        random_state=42
    )
    return model

if __name__ == "__main__":
    # Test initialization
    m = build_ann_model()
    print("Scikit-learn MLPRegressor initialized successfully.")
