
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.chatbot.graph import build_chatbot_graph

router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"]
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    print("========== CHAT REQUEST ==========")
    print("Question:", request.message)

    # Handle greetings directly
    greetings = {
        "hi",
        "hello",
        "hey",
        "hii",
        "good morning",
        "good afternoon",
        "good evening"
    }

    message = request.message.strip().lower()

    if message in greetings:
        return ChatResponse(
            response=(
                "Hello! 👋 I am your Student Database Assistant. "
                "You can ask me about student records, departments, "
                "or the total number of students."
            )
        )


    try:
        graph = build_chatbot_graph(db)

        result = graph.invoke({
            "question": request.message,
            "context": "",
            "answer": ""
        })

        print("Chatbot result received")

        return ChatResponse(
            response=result["answer"]
        )

    except Exception as e:
        print("========== CHATBOT ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("===================================")

        raise