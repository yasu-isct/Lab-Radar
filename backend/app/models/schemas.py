from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl


class HealthResponse(BaseModel):
    status: str


class LanguageCode(StrEnum):
    ja = "ja"
    en = "en"
    zh = "zh"


class Publication(BaseModel):
    title: str
    abstract: str | None = None
    year: int | None = Field(default=None, ge=1900, le=2100)
    url: HttpUrl | None = None


class ProfessorProfile(BaseModel):
    id: str
    name: str
    university: str
    department: str | None = None
    lab_name: str | None = None
    title: str | None = None
    research_areas: list[str] = Field(default_factory=list)
    profile_text: str
    publications: list[Publication] = Field(default_factory=list)
    email: str | None = None
    homepage_url: HttpUrl | None = None
    source_urls: list[HttpUrl] = Field(default_factory=list)
    language: LanguageCode = LanguageCode.ja


class SopDocument(BaseModel):
    id: str | None = None
    title: str | None = None
    text: str = Field(min_length=20)
    language: LanguageCode | None = None
    target_fields: list[str] = Field(default_factory=list)


class MatchRequest(BaseModel):
    sop: SopDocument
    top_k: int = Field(default=10, ge=1, le=50)
    min_score: float = Field(default=0.0, ge=0.0, le=1.0)


class MatchReason(BaseModel):
    summary: str
    aligned_research_areas: list[str] = Field(default_factory=list)
    suggested_contact_angle: str | None = None


class ProfessorMatch(BaseModel):
    professor: ProfessorProfile
    score: float = Field(ge=0.0, le=1.0)
    reason: MatchReason


class MatchResponse(BaseModel):
    query_id: str
    matches: list[ProfessorMatch]
    retrieval_strategy: str
