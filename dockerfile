FROM python:3.12
RUN pip install poetry
COPY . /src 
WORKDIR /src 
RUN poetry install --no-root
ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
