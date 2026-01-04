from langgraph.graph import StateGraph,START,END
from state import letter
from langchain_google_genai import ChatGoogleGenerativeAI
from nodes import create_prompt,image_url,processing
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

GRN=StateGraph(letter)

GRN.add_node("image",image_url)
GRN.add_node("prompt",create_prompt)
GRN.add_node("brain",processing)

GRN.add_edge(START,"image")
GRN.add_edge("image","prompt")
GRN.add_edge("prompt","brain")
GRN.add_edge("brain",END)

brain=GRN.compile()

initial_state={
    'uploaded_file':"E:\Langraph\Sample_bill.jpg"
}

result=brain.invoke(initial_state)
print(result['output'])

