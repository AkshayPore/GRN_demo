from utils.graph import brain


initial_state={
    'uploaded_file':"E:\Langraph\photo_2025-08-18_10-54-37.jpg",
    'improvement':"NO"
}

result=brain.invoke(initial_state)
print(result['output'])
print(result['query'])