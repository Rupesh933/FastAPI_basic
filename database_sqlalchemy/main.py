from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal, get_db
from schemas import StudentCreate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# create student
@app.post('/student')
def create_stuent(stuent: StudentCreate, db: Session = Depends(get_db)):
    student = models.Student(name=stuent.name, age=stuent.age)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {
        'message': "Student created succussfully",
        'student': student
    }

# display all student
@app.get('/students')
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return {
        "message": "Getting all data succssfully",
        "students": students
    }

@app.get('/student/{student_id}')
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        return{
            'message': 'Student Not found',
            'student': None
        }
    return {
        'message': 'student finding successfully',
        'student': student
    }

@app.put('/student/{student_id}')
def update_student(student_id: int, updated_student: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail = f'Student with {student_id} not found',
        )
    student.name = updated_student.name
    student.age = str(updated_student.age)
    db.commit()
    db.refresh(student)
    return {
        'message': 'Student data updated successfully',
        'student': student
    }
    
@app.delete('/student/{student_id}')
def delete_student(student_id: int, db:Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail = 'Student Not found'
        )
    db.delete(student)
    db.commit()
    return {
        'message': 'student delete successfully',
        'student': student
    }