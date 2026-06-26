from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

students = {
    1: 'Rupesh',
    2: 'Rahul'
}

class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.student_id = student_id

@app.exception_handler(StudentNotFoundException)
async def student_not_found_handler(request: Request, exe: StudentNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            'message': f'Student with ID {exe.student_id} not found'
        }
    )
@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise StudentNotFoundException(student_id)
    return {
        "id": student_id,
        "name": students[student_id]
    }