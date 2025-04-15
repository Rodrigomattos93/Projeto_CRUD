FROM python:3.12
RUN pip install poetry
COPY . /src 
WORKDIR /src 
RUN poetry install --no-root
ENTRYPOINT ["poetry", "run", "python", "app/main.py"]