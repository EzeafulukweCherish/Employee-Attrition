from pydantic import BaseModel, Field


class EmployeeInput(BaseModel):
    """
    Input schema for a single employee attrition prediction request.
    Field names match the original dataset columns.
    """
    Age: int = Field(..., ge=18, le=70, example=35)
    BusinessTravel: str = Field(..., example="Travel_Rarely")
    Department: str = Field(..., example="Research & Development")
    DistanceFromHome: int = Field(..., ge=0, example=10)
    Education: int = Field(..., ge=1, le=5, example=3)
    EducationField: str = Field(..., example="Life Sciences")
    EnvironmentSatisfaction: int = Field(..., ge=1, le=4, example=3)
    Gender: str = Field(..., example="Male")
    HourlyRate: int = Field(..., ge=0, example=65)
    JobInvolvement: int = Field(..., ge=1, le=4, example=3)
    JobLevel: int = Field(..., ge=1, le=5, example=2)
    JobRole: str = Field(..., example="Research Scientist")
    JobSatisfaction: int = Field(..., ge=1, le=4, example=3)
    MaritalStatus: str = Field(..., example="Single")
    MonthlyIncome: int = Field(..., ge=0, example=6000)
    MonthlyRate: int = Field(..., ge=0, example=15000)
    NumCompaniesWorked: int = Field(..., ge=0, example=2)
    OverTime: str = Field(..., example="No")
    PercentSalaryHike: int = Field(..., ge=0, example=13)
    PerformanceRating: int = Field(..., ge=1, le=4, example=3)
    RelationshipSatisfaction: int = Field(..., ge=1, le=4, example=3)
    StockOptionLevel: int = Field(..., ge=0, le=3, example=1)
    TotalWorkingYears: int = Field(..., ge=0, example=8)
    TrainingTimesLastYear: int = Field(..., ge=0, example=2)
    WorkLifeBalance: int = Field(..., ge=1, le=4, example=3)
    YearsAtCompany: int = Field(..., ge=0, example=5)
    YearsInCurrentRole: int = Field(..., ge=0, example=3)
    YearsSinceLastPromotion: int = Field(..., ge=0, example=1)
    YearsWithCurrManager: int = Field(..., ge=0, example=3)

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 35,
                "BusinessTravel": "Travel_Rarely",
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
                "YearsWithCurrManager": 3,
            }
        }


class PredictionResponse(BaseModel):
    prediction: str
    probability: float
