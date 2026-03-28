from fastapi import FastAPI
from starlette.routing import Router
from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.resumes import router as resumes_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Resume Analyzer is running"}

app.include_router(auth_router, prefix="/auth", tags= ["auth"])
app.include_router(resumes_router, prefix="/resumes", tags=["resumes"])

