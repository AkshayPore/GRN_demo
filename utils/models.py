from langchain_google_genai import ChatGoogleGenerativeAI
from utils.state import data
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash'
)

structured_model=model.with_structured_output(data)