from fastapi import APIRouter


router = APIRouter(prefix="/api/link")


@router.get("/student")
async def get_student_link(name: str, group: str):
    print(name, group)


@router.get("/group")
async def get_group_link(group: str):
    print(group)


@router.get("/teacher")
async def get_teacher_link(name: str):
    print(name)
