from dataclasses import dataclass, field

from angaa.entities.message_type import ChatMessageRole


@dataclass(frozen=True)
class DeveloperMessage:
    content: str | list[str]
    name: str | None = field(default=None)
    role: ChatMessageRole = field(default=ChatMessageRole.DEVELOPER, init=False)


@dataclass(frozen=True)
class SystemMessage:
    content: str | list[str]
    name: str | None = field(default=None)
    role: ChatMessageRole = field(default=ChatMessageRole.SYSTEM, init=False)


@dataclass(frozen=True)
class UserMessage:
    content: str | list[str]
    name: str | None = field(default=None)
    role: ChatMessageRole = field(default=ChatMessageRole.USER, init=False)
