from fastapi import APIRouter


router = APIRouter(prefix="/api/schedule")


@router.get("/student")
async def get_student_schedule(id: int):
    pass


@router.get("/group")
async def get_group_schedule(id: int):
    pass


@router.get("/teacher")
async def get_teacher_schedule(id: int):
    pass
