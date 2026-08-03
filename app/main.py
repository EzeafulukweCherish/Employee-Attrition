from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.inference import predict_attrition
from app.model_loader import load_model, load_model_columns
from app.schemas import EmployeeInput, PredictionResponse

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

BASE_DIR = Path(__file__).resolve().parent.parent
UI_HTML_PATH = BASE_DIR / "attrition_test_form.html"


@app.get("/", response_class=HTMLResponse)
def root():
    return HTMLResponse(content=UI_HTML_PATH.read_text(encoding="utf-8"), status_code=200)


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
