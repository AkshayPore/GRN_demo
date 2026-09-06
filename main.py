# # image_path = r"E:\Grn demo\recipet.jpg"

# # initial_state={
# #     'uploaded_file':image_path,
# #     'improvement':"NO"
# # }

# # result=brain.invoke(initial_state)
# # print(result['output'])
# # print(result['query'])




import os
import streamlit as st
from PIL import Image
from utils.graph import brain
# from utils.state import letter

st.set_page_config(page_title="GRN")
st.title("📄 Image Extractor with LangGraph")

uploaded_file = st.file_uploader("Upload Receipt", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Display the image (using use_container_width as use_column_width is deprecated)
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Extract Information"):
        with st.spinner("Analyzing..."):
            try:
                # 2. Save the uploaded file temporarily so your graph can read the path
                temp_dir = "temp_images"
                os.makedirs(temp_dir, exist_ok=True)
                temp_path = os.path.join(temp_dir, uploaded_file.name)
                
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # 3. Pass the valid temporary file path to your graph state
                initial_state = {
                    'uploaded_file': temp_path,
                    'improvement': "NO"
                }
                
                result = brain.invoke(initial_state)

                # 4. Output results
                st.subheader("Analysis Results:")
                st.write("Extracted Fields:")
                st.markdown(result.get('output', 'No output found.'))
                
                # st.write("Generated SQL Query:")
                # st.markdown(result.get('query', 'No query found.'))
                
            except Exception as e:
                # Print the actual error message to help you debug if it fails
                st.error(f"An error occurred during processing: {e}")
                
            finally:
                # 5. Clean up by deleting the temporary image
                if os.path.exists(temp_path):
                    os.remove(temp_path)