from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from document_converter.route import router as document_converter_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


app.include_router(document_converter_router, prefix="", tags=["document-converter"])
