from utils.graph import brain
import streamlit as st
from utils.state import letter

st.set_page_config(page_title="GRN")
st.title("📄 Image Extractor with LangGraph")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    if st.button("Extract Information"):
        with st.spinner("Analyzing..."):
            try:
                initial_state={
                        'uploaded_file':"E:\Langraph\photo_2025-08-18_10-54-37.jpg",
                        'improvement':"NO"
                }
                result=brain.invoke(initial_state)

                st.subheader("Analysis Results:")
                st.markdown(result['output'])
                st.write("Fields are Successfully Inserted !!!!!!!!!!!!!")
            except:
                st.error(f"An error occurred: {e}")


# initial_state={
#     'uploaded_file':"E:\Langraph\photo_2025-08-18_10-54-37.jpg",
#     'improvement':"NO"
# }

# result=brain.invoke(initial_state)
# print(result['output'])
# print(result['query'])