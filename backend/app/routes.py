from fastapi import APIRouter
from app.models.schemas import JDRequest
from app.services.project_generator import generate_projects

router = APIRouter()

@router.post("/generate")
async def generate(data: JDRequest):
    return generate_projects(data.jd)