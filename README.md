# 📚 Projeto CRUD de Livros - FastAPI & SQLite

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Um sistema CRUD completo para gerenciamento de livros, desenvolvido com FastAPI e SQLite, pronto para Docker.

## Funcionalidades

-  Operações CRUD completas (Create, Read, Update, Delete)
-  Validação de dados com Pydantic
-  Banco de dados SQLite
-  Logs com Loguru
-  Documentação automática (Swagger UI e Redoc)
-  Pronto para containerização com Docker

## Tecnologias utilizadas

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

## Começando

### Pré-requisitos

- Python 3.12+
- Poetry (gerenciador de dependências)
- Docker (opcional)

### Instalação

```bash
git clone https://github.com/Rodrigomattos93/projeto_crud.git
cd projeto_crud
```

### Execução

Localmente:
```bash
poetry install
poetry env activate
uvicorn app.main:app --reload
```

Com Docker:
```bash
docker build -t livro-crud .
docker run -d --name livro-crud -p 8000:8000 livro-crud
```
### Documentação

A documentação da API estará disponível em:
```markdown
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`
```

### Endpoints da API

| Método HTTP | Endpoint         | Descrição                          |
|-------------|------------------|------------------------------------|
| `GET`       | `/books/`        | Lista todos os livros              |
| `GET`       | `/books/{id}`    | Obtém um livro específico          |
| `POST`      | `/books/`        | Cria um novo livro                 |
| `PUT`       | `/books/{id}`    | Atualiza um livro existente        |
| `DELETE`    | `/books/{id}`    | Remove um livro                    |

### Modelo de Dados
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

### Estrutura do Projeto
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