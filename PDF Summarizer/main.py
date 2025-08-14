import streamlit as st
from utils import summarizer

# --- CSS Styling ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8faff, #e6f0ff);
    font-family: 'Segoe UI', Tahoma, sans-serif;
}
h1 {
    color: #2b4eff;
    font-weight: bold;
}
.stButton > button {
    background-color: #2b4eff;
    color: white;
    font-weight: bold;
    padding: 0.6rem 1.4rem;
    border-radius: 12px;
    border: none;
    transition: 0.3s ease-in-out;
}
.stButton > button:hover {
    background-color: #1a3dd1;
    transform: scale(1.05);
}
.stFileUploader {
    border: 2px dashed #2b4eff;
    background-color: #f0f4ff;
    border-radius: 10px;
    padding: 10px;
}
.summary-box {
    background-color: white;
    padding: 15px 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    border-left: 5px solid #2b4eff;
}
hr {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #2b4eff, transparent);
}
.button-row {
    display: flex;
    gap: 10px;
}
.custom-btn {
    background-color: #ff6b6b;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}
.custom-btn:hover {
    background-color: #e85a5a;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="PDF Summarizer")
    st.title("📄 PDF Summarizing App")
    st.write("Upload a PDF and get a summary using a free Hugging Face model.")
    st.divider()

    # Upload PDF file
    pdf = st.file_uploader("📤 Upload your PDF Document", type='pdf')

    # Buttons row
    col1, col2 = st.columns(2)
    with col1:
        generate = st.button("🧠 Generate Summary")
    with col2:
        st.markdown('<button class="custom-btn">📥 Download Summary</button>', unsafe_allow_html=True)

    # Generate summary
    if generate and pdf:
        with st.spinner("Summarizing... Please wait ⏳"):
            response = summarizer(pdf)
            st.markdown('<div class="summary-box">', unsafe_allow_html=True)
            st.subheader("📝 Summary of the File:")
            st.write(response)
            st.markdown('</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
