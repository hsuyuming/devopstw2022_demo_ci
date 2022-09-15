FROM python:3.9.10

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock /code/

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y --allow-downgrades install lsb-release unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc libldap-2.4-2 zip unzip libpng-dev libaio1 libbz2-dev netcat vim

# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
RUN pip install --upgrade pip  && \ 
    pip install --no-cache-dir poetry && \ 
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi 

COPY . /code

RUN poetry build && \
    pip install dist/*.whl

EXPOSE 8081

CMD ["python", "-m", "uvicorn", "src.fastapi_demo.fastapi_demo:app", "--host", "0.0.0.0", "--port", "8081"]
