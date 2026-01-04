import base64, mimetypes
from models import model
from state import letter
from langchain_core.messages import HumanMessage

def image_url(state : letter):
    uploaded_file=state['uploaded_file']
    with open(uploaded_file, "rb") as f:
            bytes_data = f.read()                
    b64_string = base64.b64encode(bytes_data).decode("utf-8")
    mime_type, _ = mimetypes.guess_type(uploaded_file)
    if not mime_type:
        mime_type = "image/jpeg" # Default fallback 
    image_data_url = f"data:{mime_type};base64,{b64_string}"
    return {'image':image_data_url}


def create_prompt(state : letter):
    image_data_url=state["image"]
    message = HumanMessage(
                        content=[
                            {"type": "text", "text": "What information is in this image? Provide a detailed summary."},
                            {"type": "image_url", "image_url": {"url": image_data_url}}
                        ]
                    )
    return {'prompt':message}

def processing(state : letter):
    prompt=state["prompt"]
    result=model.invoke([prompt])
    return {'output':result.content}