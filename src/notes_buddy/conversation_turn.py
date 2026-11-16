from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class ConversationTurn:
    text: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))
    role: str = field(init=False)


@dataclass(frozen=True, kw_only=True)
class UserInput(ConversationTurn):
    role: str = field(default="user", init=False)


@dataclass(frozen=True, kw_only=True)
class LLMResponse(ConversationTurn):
    role: str = field(default="assistant", init=False)
