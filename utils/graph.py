from langgraph.graph import StateGraph,START,END
from utils.state import letter
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.nodes import create_prompt,image_url,processing,improvement,query_generator
from dotenv import load_dotenv
load_dotenv()

GRN=StateGraph(letter)

GRN.add_node("image",image_url)
GRN.add_node("prompt",create_prompt)
GRN.add_node("brain",processing)
GRN.add_node("query",query_generator)

GRN.add_edge(START,"image")
GRN.add_edge("image","prompt")
GRN.add_edge("prompt","brain")
GRN.add_conditional_edges("brain",improvement,{"proceed":"query","recheck":"brain"})
GRN.add_edge("query",END)

brain=GRN.compile()


