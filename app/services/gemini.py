
from google import genai

from app.core.config import settings


client = genai.Client(
    api_key=settings.gemini_api_key
)


def generate_answer(
    question: str,
    context: str
) -> str:
    prompt = f"""
You are a helpful student database assistant.

Answer the user's question using only the
provided database context.

If the context does not contain enough
information, say that the information is
not available.

Do not invent student records.
Do not reveal private information that
is not necessary for the response.

Database context:
{context}

User question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text or "No response generated."