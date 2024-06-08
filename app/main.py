from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.pdf_extractor import extract_first_30_lines
from app.email_sender import send_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_pdf(file: UploadFile, email: str = Form(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    content = await file.read()
    try:
        extracted_text = extract_first_30_lines(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text from PDF: {str(e)}")

    try:
        send_email(email, extracted_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {str(e)}")

    return JSONResponse(content={"success": True, "message": f"The email has been successfully sent to {email}"})

