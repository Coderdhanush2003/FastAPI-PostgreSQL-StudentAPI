from database import Base, DB_source
from models import Student
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException
from schemas import StudentValidate

app = FastAPI()

Base.metadata.create_all(DB_source)

@app.post('/students')
def addStudent(studentValidate:list[StudentValidate]):
    with Session(DB_source) as session:
        data = [Student(**s.model_dump()) for s in studentValidate]
        session.add_all(data)
        session.commit()
        return {"Message" : "Created Succesfully..."}

        

@app.get('/students',response_model=list[StudentValidate])
def getAllStudent():
    with Session(DB_source) as session:
        data = session.query(Student).all()
        if data is None:
            raise HTTPException(404,"Data Not Found...")
        return data
    
@app.get('/students/{id}',response_model=StudentValidate)
def getStudent(id:int):
    with Session(DB_source) as session:
        data = session.query(Student).get(id)
        if data is None:
            raise HTTPException(404,"Id Not Found...")
        return data

@app.delete('/students/{id}')
def delStudent(id:int):
    with Session(DB_source) as session:
        st = session.get(Student,id)
        if st is None:
            raise HTTPException(404,"Id Not Found...")
        session.delete(st)
        session.commit()
        return {"Message" : "Deleted Succesfully..."}
    
@app.put('/students/{id}')
def updateStudent(id:int,studentValidate:StudentValidate):
    with Session(DB_source) as session:
        st = session.get(Student,id)
        if st is None:
            raise HTTPException(404,"Id Not Found...")
        data = studentValidate.model_dump()
        st.student_id = id
        st.student_name = data['student_name']
        st.subject = data['subject']
        session.commit()
        return {"Message" : "Updated Successfully"}

