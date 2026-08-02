import os
import joblib

# Paths to the saved artifacts (place these files in the /model folder)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "attrition_model.pkl")
COLUMNS_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model_columns.pkl")


def load_model():
    """Load the trained XGBoost attrition model from disk."""
    return joblib.load(MODEL_PATH)


def load_model_columns():
    """Load the exact list/order of columns the model was trained on."""
    return joblib.load(COLUMNS_PATH)
