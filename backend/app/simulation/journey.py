from typing import List, Dict


def simulate_journey(profile: dict, need: dict) -> Dict:

    barriers: List[dict] = []
    steps: List[dict] = []

    # Consultation
    if need.get("consultation_required"):
        steps.append({
            "step": 1,
            "name": "Healthcare Consultation",
            "status": "required"
        })

    # Diagnostic test
    if need.get("diagnostic_required"):
        steps.append({
            "step": len(steps) + 1,
            "name": "Diagnostic Test",
            "status": "required",
            "test_type": need.get("diagnostic_type")
        })

    # Specialist
    if need.get("specialist_required"):
        steps.append({
            "step": len(steps) + 1,
            "name": "Specialist Consultation",
            "status": "required"
        })

    # Accessibility barrier
    if profile.get("mobility") == "limited":
        barriers.append({
            "type": "accessibility",
            "severity": "medium",
            "message": (
                "Patient has limited mobility. "
                "Facility accessibility should be verified."
            )
        })

    # Language barrier
    if profile.get("language") != "English":
        barriers.append({
            "type": "language",
            "severity": "low",
            "message": (
                f"Patient prefers {profile.get('language')}. "
                "Language support should be verified."
            )
        })

    # Caregiver barrier
    if not profile.get("caregiver_available"):
        barriers.append({
            "type": "caregiver",
            "severity": "medium",
            "message": (
                "No caregiver is available. "
                "Journey should minimize dependency on assistance."
            )
        })

    return {
        "steps": steps,
        "barriers": barriers,
        "barrier_count": len(barriers)
    }