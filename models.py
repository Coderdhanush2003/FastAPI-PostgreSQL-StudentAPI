from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Student(Base):
    __tablename__ = "student"
    student_id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str]
    subject: Mapped[str]

