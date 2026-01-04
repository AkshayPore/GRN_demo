from typing import TypedDict, Literal
from pydantic import BaseModel

class data(BaseModel):
    invoice_number : int
    invoice_data : str
    vendor_name : str
    total_amount : int


class letter(TypedDict):
    uploaded_file : any
    image : str
    prompt: str
    improvement : Literal['YES','NO']
    output : str
    query : str