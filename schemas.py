from pydantic import BaseModel

class StudentValidate(BaseModel):
    student_id: int
    student_name: str
    subject: str

