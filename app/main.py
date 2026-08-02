from fastapi import FastAPI, HTTPException
from app.schemas import EmployeeInput, PredictionResponse
from app.model_loader import load_model, load_model_columns
from app.inference import predict_attrition

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="Predicts whether an employee is likely to leave the company, "
    "based on the IBM HR Analytics Employee Attrition dataset.",
    version="1.0.0",
)

# Load the trained model and column list once, at startup,
# rather than on every request (much faster).
model = load_model()
model_columns = load_model_columns()


@app.get("/")
def root():
    return {
        "message": "Employee Attrition Prediction API is running.",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(employee: EmployeeInput):
    try:
        employee_dict = employee.dict()
        result = predict_attrition(employee_dict, model, model_columns)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
