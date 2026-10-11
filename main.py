
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from extraction_service import extract_enquiry

app = FastAPI()


class EnquiryRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "running"}
@app.get("/version")
def version_check():
    return {"version" : "1.0.0"}

@app.post("/extract")
def extract_endpoint(request: EnquiryRequest):
    try:
        result = extract_enquiry(request.message)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail="Enquiry extraction failed. Please try again."
        ) from e