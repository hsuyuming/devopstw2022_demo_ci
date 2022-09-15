"""
demo code
"""
from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

fake_data = pd.DataFrame.from_dict(
    {"id": [1, 2, 3, 4], "student_name": ["Jay", "William", "Lucas", "Oliver"]}
)

jobs_mapping = {
    "micon": [
        "Solution Architect",
        "Data Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Industry I4.0 Analyst",
        "Global OI - Scheduling and Simulation Engineer"
    ]
}

def hello_student(student_id: int) -> str:
    """get student name by id, then generate "Hello, <student_name>"

    Parameters
    ----------
    student_id : id
        student's id.

    Returns
    -------
    str
       concat Hello with student's name

    Examples
    --------
    >>> hello_student(1)
    """
    # data = fake_data.where(fake_data["id"]== student_id).iloc[0]
    data = fake_data[fake_data["id"] == student_id].iloc[0]
    return f"Hello, {data.student_name}"


@app.get("/")
async def hello_devopstw():
    """Return {"Hello": "devopstw"}
    Parameters
    ----------

    Returns
    -------
    dict
        {"Hello": "devopstw"}

    """
    # return {"Hello": "devopstw"}
    return {"加入美光": "人生發光"}


@app.get("/students/{student_id}")
async def roll_call(student_id: int):
    """roll_call by student_id
    Parameters
    ----------
    student_id : id
        student's id.
    Returns
    -------
    str


    """
    return hello_student(student_id)

@app.get("/job/{company_name}")
async def job(company_name: str):
    """list all of jobs
    Parameters
    ----------
    company_name : str
        company name
    Returns
    -------
    list

    """
    return jobs_mapping.get(company_name)



@app.get("/ping")
async def ping():
    """Return {"ping": "pong"}
    Parameters
    ----------

    Returns
    -------
    dict
        {"ping": "pong"}

    """
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run(
        app="src.fastapi_demo.fastapi_demo:app",
        host="0.0.0.0",
        port=8081,
        reload=True,
        debug=True,
    )
