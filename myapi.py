from fastapi import FastAPI
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name': 'john',
        'age': 17,
        'class': 'year 12'
    }
}

@app.get('/')
def index():
    return {'name': 'First Data'}


@app.get('/get-student/{student_id}')

# def get_student(student_id: int):
#     return students[student_id]


@app.get('/get-by-name{student_id}')
def get_student(student_id: int, test: int, name : Optional[str] = None):

    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]

    return {'Data': 'Not found'}

if __name__ == '__main__':
    print(get_student(1, 2, 'ann'))