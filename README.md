# 📚 Books CRUD Project - FastAPI & SQLite

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A complete CRUD system for managing books, developed with FastAPI and SQLite, Docker-ready.

## Features

-  Full CRUD operations (Create, Read, Update, Delete)
-  Data validation with Pydantic
-  SQLite database
-  Logging with Loguru
-  Automatic documentation (Swagger UI and Redoc)
-  Ready for containerization with Docker

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- SQLite
- Poetry
- Docker
- Loguru
- Git

## Getting started

### Prerequisites

- Python 3.12+
- Poetry (Dependency manager)
- Docker (optional)

### Installation

```bash
git clone https://github.com/Rodrigomattos93/projeto_crud.git
cd projeto_crud
```

### Running the Project

Locally:
```bash
poetry install --no-root
poetry env activate
uvicorn app.main:app --reload
```

With Docker:
```bash
docker build -t livro-crud .
docker run -d --name livro-crud -p 8000:8000 livro-crud
```
### Documentation

The API documentation will be available at:
```markdown
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`
```

### API Endpoints

| Método HTTP | Endpoint         | Descrição                          |
|-------------|------------------|------------------------------------|
| `GET`       | `/books/`        | List all books                     |
| `GET`       | `/books/{id}`    | Gets a specific book               |
| `POST`      | `/books/`        | Creates a new book                 |
| `PUT`       | `/books/{id}`    | Update an existing book            |
| `DELETE`    | `/books/{id}`    | Delete a book                      |

### Data Model
```python
class BookModel(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer, nullable=True)
    genre = Column(String, nullable=True)
    publisher = Column(String, nullable=True)
    page_count = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    is_avaiable = Column(Boolean)
    created_at = Column(DateTime, default=func.now())
```

### Project Structure
```projeto-crud/
├── app/
│   ├── controllers.py    # Lógica de negócios
│   ├── db.py             # Configuração do banco
│   ├── logger_config.py  # Configuração de logs
│   ├── main.py           # Ponto de entrada
│   ├── models.py         # Modelos do banco
│   ├── routers.py        # Endpoints
│   └── schemas.py        # Validação
├── Dockerfile            # Config Docker
├── pyproject.toml        # Dependências
├── books.db              # Banco de dados
└── README.md             # Documentação
```