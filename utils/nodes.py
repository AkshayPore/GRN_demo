import base64, mimetypes
from utils.models import model, structured_model
from utils.state import letter
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
                            {"type": "text", "text": """Extract all the information from  the below image.Give only invoice number , invoice date, vendor_name & total from the bill.
                             ###Respond only in structured format-
                                invoice_number : int
                                invoice_data : str
                                vendor_name : str
                                total_amount : int"""},
                            {"type": "image_url", "image_url": {"url": image_data_url}}
                        ]
                    )
    return {'prompt':message}

def processing(state : letter):
    prompt=state["prompt"]
    result=structured_model.invoke([prompt])
    return {'output':result}

def improvement(state : letter):
    if state["improvement"]=="YES":
        return "recheck"
    else:
        return "proceed"
    

def query_generator(state : letter):
    data=state["output"]
    message = HumanMessage(
                        content=[
                            {"type": "text", "text": "You are an expert SQL query writer. Your task is to write an SQL query from the schema/data provoded by user. Do not write any query other than insert query. Do not create delete/drop/truncate/update/alter query. Return only sql query dont return code block. "}, 
                            {"type": "text", "text": f"Here is schema:{data}"}
                        ]
                    )
    result=model.invoke([message])
    return {'query':result.content}
