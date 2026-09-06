from langchain_google_genai import ChatGoogleGenerativeAI
from utils.state import data
from dotenv import load_dotenv
import os
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

structured_model=model.with_structured_output(data)