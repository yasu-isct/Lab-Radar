from fastapi import APIRouter

from backend.app.models.schemas import MatchRequest, MatchResponse
from backend.app.services.matching import MatchingService

router = APIRouter(prefix="/recommendations", tags=["recommendations"])
matching_service = MatchingService()


@router.post("/match", response_model=MatchResponse)
def match_professors(request: MatchRequest) -> MatchResponse:
    return matching_service.match(request)
