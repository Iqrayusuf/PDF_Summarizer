import os
from transformers import pipeline
from PyPDF2 import PdfReader

# ✅ Redirect Hugging Face cache to D: drive
os.environ["HF_HOME"] = "D:/huggingface_cache"

# ✅ Load summarization model (no sentencepiece needed)
summarizer_pipeline = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)

def local_summarizer(text):
    """
    Summarize the given text using the bart-large-cnn Hugging Face model.
    Handles long text by chunking.
    """
    max_chunk_size = 1024
    overlap = 100
    chunks = []

    for i in range(0, len(text), max_chunk_size - overlap):
        chunk = text[i:i + max_chunk_size]
        chunks.append(chunk)

    summaries = []
    for chunk in chunks:
        result = summarizer_pipeline(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(result[0]['summary_text'])

    return " ".join(summaries)

def summarizer(pdf):
    """
    Read the uploaded PDF and summarize its content using Hugging Face.
    """
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            return "No text could be extracted from the PDF."

        return local_summarizer(text)
