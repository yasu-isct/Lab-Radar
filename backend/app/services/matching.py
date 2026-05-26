from uuid import uuid4

from backend.app.models.schemas import MatchReason, MatchRequest, MatchResponse


class MatchingService:
    """Boundary for the future SOP-to-professor retrieval pipeline."""

    def match(self, request: MatchRequest) -> MatchResponse:
        _ = request
        return MatchResponse(
            query_id=str(uuid4()),
            matches=[],
            retrieval_strategy="placeholder",
        )

    @staticmethod
    def build_reason(summary: str, aligned_research_areas: list[str]) -> MatchReason:
        return MatchReason(
            summary=summary,
            aligned_research_areas=aligned_research_areas,
        )
