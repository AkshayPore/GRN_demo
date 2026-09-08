from langchain_google_genai import ChatGoogleGenerativeAI
from utils.state import data
from dotenv import load_dotenv
import os
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    max_retries=3
    )


structured_model=model.with_structured_output(data)