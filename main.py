from fastapi import FastAPI
from fastapi import UploadFile, File
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
from pydantic import BaseModel
import chromadb
import os
load_dotenv()
app = FastAPI()
ai = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
client = chromadb.Client()
collection = client.create_collection(name="pdf_rag")
model = SentenceTransformer("all-MiniLM-L6-v2")

class Req(BaseModel):
    question : str


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename,"wb") as f:
        contents = await file.read()
        f.write(contents)

    reader = PdfReader(file.filename)
    text = ""
    
    for page in reader.pages:
        extracted_text = page.extract_text()
        
        if extracted_text:
            text += extracted_text
        
        chunks = text.split(".")
        chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
        
        embeddings = model.encode(chunks).tolist()
        
        for i, chunk in enumerate(chunks):
            collection.add(
                ids=[str(i)],
                documents=[chunk],
                embeddings=[embeddings[i]]
            )
        
        return{
            "message":"pdf uploaded successfully",
            "total chunks":len(chunks)
        }

@app.post("/chat")
def chat(request:Req):
    query = request.question
    query_embedding = model.encode([query]).tolist()[0]
    
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    context = "\n".join(result["documents"][0])
    
    prompt = f"""
        Answer the question using only the context below.
        context:
        {context} 
        question:
        {query}   
    """
    try:
        response = ai.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        answer = response.text
    except Exception as e:
        answer = str(e)
    
    return{
        "Question":query,
        "Context":context,
        "Answer": answer
    }