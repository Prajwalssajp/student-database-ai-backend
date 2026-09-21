
from langgraph.graph import StateGraph, START, END
from sqlalchemy.orm import Session

from app.chatbot.state import ChatbotState
from app.chatbot.tools import retrieve_student_context
from app.services.gemini import generate_answer


def build_chatbot_graph(db: Session):
    def retrieve_node(state: ChatbotState):
        context = retrieve_student_context(
            db,
            state["question"]
        )

        return {
            "context": context
        }

    def generate_node(state: ChatbotState):
        answer = generate_answer(
            question=state["question"],
            context=state["context"]
        )

        return {
            "answer": answer
        }

    graph_builder = StateGraph(ChatbotState)

    graph_builder.add_node(
        "retrieve",
        retrieve_node
    )

    graph_builder.add_node(
        "generate",
        generate_node
    )

    graph_builder.add_edge(START, "retrieve")
    graph_builder.add_edge("retrieve", "generate")
    graph_builder.add_edge("generate", END)

    return graph_builder.compile()