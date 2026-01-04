from utils.graph import brain


initial_state={
    'uploaded_file':"E:\Langraph\Sample_bill.jpg",
    'improvement':"NO"
}

result=brain.invoke(initial_state)
print(result['output'])
print(result['query'])