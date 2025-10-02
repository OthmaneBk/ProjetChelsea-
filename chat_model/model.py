from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from chat_model.prompt import promptAI

# Charger les variables d'environnement (par ex. GOOGLE_API_KEY dans .env)
load_dotenv()

# Initialiser le modèle
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

def get_ai_response(query: str) -> str:

    # Messages au format LangChain
    messages = [
        SystemMessage(content=promptAI),
        HumanMessage(content=query)
        ]

    ai_msg = llm.invoke(messages)
    return ai_msg.content
