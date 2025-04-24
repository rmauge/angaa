from enum import Enum


class ChatMessageRole(Enum):
    DEVELOPER = "developer"
    SYSTEM = "system"
    USER = "user"


class MessageRole(Enum):
    ASSISTANT = "assistant"
    TOOL = "tool"
    FUNCTION = "function"
