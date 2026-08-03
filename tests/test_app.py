import unittest

from fastapi.testclient import TestClient

from app.main import app


class AppEndpointsTest(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root_serves_ui(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Employee Attrition", response.text)

    def test_predict_endpoint_still_works(self):
        payload = {
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
            "YearsWithCurrManager": 3,
        }

        response = self.client.post("/predict", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())
        self.assertIn("probability", response.json())


if __name__ == "__main__":
    unittest.main()
