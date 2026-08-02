import pandas as pd

# Categorical columns that were one-hot encoded during training
# (must match exactly what was used in the training notebook)
CATEGORICAL_COLS = [
    "BusinessTravel",
    "Department",
    "EducationField",
    "Gender",
    "JobRole",
    "MaritalStatus",
    "OverTime",
]


def preprocess_input(employee_dict: dict, model_columns: list) -> pd.DataFrame:
    """
    Convert a single employee's raw input (as a dict) into the exact
    one-hot encoded feature vector the trained model expects.

    Steps:
      1. Build a single-row DataFrame from the input.
      2. One-hot encode the categorical columns the same way training did.
      3. Reindex to match the training column order exactly, filling any
         missing dummy columns with 0 (e.g. a category not seen in this
         particular request).
    """
    input_df = pd.DataFrame([employee_dict])

    input_encoded = pd.get_dummies(input_df, columns=CATEGORICAL_COLS)

    # Ensure the final frame has exactly the same columns, same order,
    # as what the model was trained on. Any column the model expects
    # that wasn't produced here gets filled with 0.
    input_final = input_encoded.reindex(columns=model_columns, fill_value=0)

    return input_final


def predict_attrition(employee_dict: dict, model, model_columns: list) -> dict:
    """Run a prediction for a single employee and return a clean result dict."""
    features = preprocess_input(employee_dict, model_columns)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # P(Attrition = Yes)

    return {
        "prediction": "Yes" if prediction == 1 else "No",
        "probability": round(float(probability), 4),
    }
