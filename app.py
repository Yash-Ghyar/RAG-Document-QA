import os
import PyPDF2
from flask import Flask, render_template, request
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Flask app
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)

# LLM (Groq)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

prompt_template = """
I will provide you a question and document chunks containing answers.
Answer the question in 2 lines ONLY.
If answer not found, say: "Don't Know Answer".

Question: {question}

Document: {document}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["question", "document"]
)

parser = StrOutputParser()


# ------------------------------
# HOME PAGE
# ------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ------------------------------
# PDF UPLOAD
# ------------------------------
@app.route("/upload", methods=["POST"])
def upload_pdf():
    file = request.files["pdf"]

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text
    reader = PyPDF2.PdfReader(file_path)
    data = ""
    for page in reader.pages:
        data += "\n" + page.extract_text()

    # Chunking
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(data)

    docs = [Document(page_content=c) for c in chunks]

    # Create vector DB
    db = Chroma.from_documents(
        documents=docs,
        embedding=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"),
        persist_directory="./chroma_db"
    )

    db.persist()

    return render_template("index.html", msg="PDF Uploaded & Processed Successfully!")


# ------------------------------
# ASK QUESTION
# ------------------------------
@app.route("/ask", methods=["POST"])
def ask_question():
    question = request.form["question"]

    # Load previous DB
    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    )

    similar_docs = db.similarity_search(question)
    merged = "\n\n".join([d.page_content for d in similar_docs])

    chain = prompt | llm | parser
    answer = chain.invoke({"question": question, "document": merged})

    return render_template("result.html", question=question, answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
