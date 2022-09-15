from src.fastapi_demo import fastapi_demo 

def test_hello_student_expected_name():
    data = fastapi_demo.hello_student(1)
    assert data == "Hello, Jay"