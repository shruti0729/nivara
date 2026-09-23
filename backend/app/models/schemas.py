from pydantic import BaseModel
from typing import Optional


class PatientProfile(BaseModel):
    age: int
    language: str = "English"
    mobility: str = "normal"
    budget: str = "moderate"
    caregiver_available: bool = True
    location: str


class HealthcareNeed(BaseModel):
    consultation_required: bool = True
    diagnostic_required: bool = False
    diagnostic_type: Optional[str] = None
    specialist_required: bool = False


class JourneyRequest(BaseModel):
    patient: PatientProfile
    healthcare_need: HealthcareNeed