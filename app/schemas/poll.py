from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class SubmitPollRequest(BaseModel):
    q1_modules_count: str | None = None
    q2_overall_progress: str | None = None
    q3_ready_independent: str | None = None
    q4_need_1on1: str | None = None
    q5_biggest_challenges: list[str] = Field(default_factory=list)
    q6_daily_hours: str | None = None
    q7_meeting_goals: str | None = None
    q8_internship_rating: str | None = None
    q9_tech_stack_comfort: str | None = None
    q10_docs_rating: str | None = None
    q11_improvements: list[str] = Field(default_factory=list)
    q12_overall_feeling: str | None = None
    q13_open_feedback: str | None = None


class PollResponseOut(SubmitPollRequest):
    id: UUID
    submitted_at: datetime

    model_config = {"from_attributes": True}


class PollSummary(BaseModel):
    total_responses: int
    q1_modules_count: dict[str, int]
    q2_overall_progress: dict[str, int]
    q3_ready_independent: dict[str, int]
    q4_need_1on1: dict[str, int]
    q5_biggest_challenges: dict[str, int]
    q6_daily_hours: dict[str, int]
    q7_meeting_goals: dict[str, int]
    q8_internship_rating: dict[str, int]
    q9_tech_stack_comfort: dict[str, int]
    q10_docs_rating: dict[str, int]
    q11_improvements: dict[str, int]
    q12_overall_feeling: dict[str, int]
    open_feedback: list[str]
