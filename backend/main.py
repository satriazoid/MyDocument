from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import DocumentRequest, DocumentResponse
from generator import generate_doc

app = FastAPI(title="MyDocument API")

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=DocumentResponse)
def generate(request: DocumentRequest):
    file_path = generate_doc(
        request.title,
        request.author,
        request.institution,
        request.chapters
    )
    return {
        "status": "success",
        "file": file_path
    }
