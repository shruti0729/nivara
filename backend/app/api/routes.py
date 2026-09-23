from fastapi import APIRouter

from app.models.schemas import JourneyRequest
from app.simulation.journey import simulate_journey


router = APIRouter()


@router.post("/simulate")
def simulate_journey_api(request: JourneyRequest):

    patient = request.patient.model_dump()
    healthcare_need = request.healthcare_need.model_dump()

    result = simulate_journey(
        patient,
        healthcare_need
    )

    return {
        "project": "NIVARA",
        "patient_profile": patient,
        "healthcare_need": healthcare_need,
        "journey": result
    }