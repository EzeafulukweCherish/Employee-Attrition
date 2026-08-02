# Employee Attrition Prediction API

A production-ready machine learning API that predicts whether an employee is
likely to leave a company, built with FastAPI and deployed on Render.

Built for the NITDEV AI/ML Engineering 2026 Continuous Assessment (Task 1).

## Project Overview

This project predicts employee attrition (Yes/No) using the
[IBM HR Analytics Employee Attrition & Performance dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).

- **Model:** XGBoost Classifier trained on SMOTE-balanced data
- **Class imbalance handling:** SMOTE oversampling applied to the training
  set only (not the test set), to avoid data leakage
- **Evaluation:** Precision, recall, F1-score, and confusion matrix, with
  particular attention to minority-class (attrition = Yes) performance
  rather than raw accuracy, given the dataset's ~84/16 class imbalance
- **API framework:** FastAPI, with Pydantic request validation
- **Deployment:** Dockerized and deployed on Render

## Project Structure

```
project/
├── app/
│   ├── main.py          # FastAPI app and endpoints
│   ├── model_loader.py  # Loads the trained model + column list
│   ├── inference.py     # Preprocessing + prediction logic
│   └── schemas.py       # Pydantic request/response schemas
├── model/
│   ├── attrition_model.pkl   # Trained XGBoost model
│   └── model_columns.pkl     # Column order used at training time
├── notebooks/            # EDA and model training notebook
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

## Installation & Local Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd project
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Ensure `attrition_model.pkl` and `model_columns.pkl` are present in the
   `model/` folder (see Notebook section below for how these are produced).

4. Run the API locally:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open the interactive Swagger docs at:
   ```
   http://localhost:8000/docs
   ```

## Running with Docker

```bash
docker build -t attrition-api .
docker run -p 8000:8000 attrition-api
```

## Deployment

This project is deployed on **Render** using the included `Dockerfile` and
`render.yaml`.

**Live API:** (https://employee-attrition-f2w0.onrender.com)
**Swagger docs:** https://employee-attrition-f2w0.onrender.com/docs`

## API Endpoints

| Method | Endpoint   | Description                          |
|--------|------------|---------------------------------------|
| GET    | `/`        | Health/welcome message                |
| GET    | `/health`  | Health check                          |
| POST   | `/predict` | Predict attrition for one employee    |

### Example Request

```json
POST /predict
{
  "Age": 35,
  "BusinessTravel": "Travel_Rarely",
  "DailyRate": 800,
  "Department": "Research & Development",
  "DistanceFromHome": 10,
  "Education": 3,
  "EducationField": "Life Sciences",
  "EnvironmentSatisfaction": 3,
  "Gender": "Male",
  "HourlyRate": 65,
  "JobInvolvement": 3,
  "JobLevel": 2,
  "JobRole": "Research Scientist",
  "JobSatisfaction": 3,
  "MaritalStatus": "Single",
  "MonthlyIncome": 6000,
  "MonthlyRate": 15000,
  "NumCompaniesWorked": 2,
  "OverTime": "No",
  "PercentSalaryHike": 13,
  "PerformanceRating": 3,
  "RelationshipSatisfaction": 3,
  "StockOptionLevel": 1,
  "TotalWorkingYears": 8,
  "TrainingTimesLastYear": 2,
  "WorkLifeBalance": 3,
  "YearsAtCompany": 5,
  "YearsInCurrentRole": 3,
  "YearsSinceLastPromotion": 1,
  "YearsWithCurrManager": 3
}
```

### Example Response

```json
{
  "prediction": "No",
  "probability": 0.93
}
```

## Model Development Summary

Several models and imbalance-handling strategies were compared:

| Approach                     | Class 1 Recall | Class 1 Precision | Class 1 F1 | Accuracy |
|-------------------------------|:--------------:|:------------------:|:-----------:|:---------:|
| Logistic Regression (unscaled)| 0.04           | 0.67                | 0.08        | 0.84      |
| Logistic Regression (scaled)  | 0.34           | 0.62                | 0.44        | 0.86      |
| Logistic Regression + SMOTE   | 0.55           | 0.22                | 0.32        | 0.62      |
| Random Forest (class_weight)  | 0.09           | 0.44                | 0.14        | 0.84      |
| Random Forest + SMOTE         | 0.26           | 0.41                | 0.32        | 0.82      |
| XGBoost                       | 0.30           | 0.50                | 0.37        | 0.84      |
| **XGBoost + SMOTE (final)**   | **0.40**        | **0.47**            | **0.44**    | **0.83**  |

**XGBoost + SMOTE** was selected as the final model. While Logistic
Regression (scaled) achieved a marginally higher F1-score, the difference
was negligible given the small minority class size (n=47) in the test set.
XGBoost + SMOTE was preferred for its stronger recall (more effectively
identifying at-risk employees — the more costly error to make in this use
case), its robustness to the skewed feature distributions and outliers
identified during EDA, and its alignment with the assignment's recommended
tree-based approaches.

SMOTE was applied only to the training set, after the train/test split, to
avoid data leakage and ensure the test set reflected the real-world class
distribution.
# Employee-Attrition
