
from typing import TypedDict


class ChatbotState(TypedDict):
    question: str
    context: str
    answer: str