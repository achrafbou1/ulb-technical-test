# 🚀 Partie 1

This repository contains the implementation of the API interacting with the *universite_demo* database.
## ✨ Tools & Libraries

- **FastAPI** for asynchronous API implementation and documentation
- **SQLAlchemy 2.0** as an ORM layer to interact with the database securely
- **Pydantic** for input validation of requests and responses and environment settings
- **Pytest** for unit and integration tests
- **Ruff & Black** for code quality, error detection and PEP8 standard adherence
- **Docker** for containerization
- **Makefile** for automating common and useful commands
- **DeepSeek AI** for documentation and best practices

## 🏗️ Project Structure

```bash
ulb-technical-test/
├── partie-1/
│ ├── controllers/ --> API endpoints and request handling logic
│ ├── schemas/ --> Request and response validation DTOs
│ ├── services/ --> Business logic & database calls
│ ├── models/ --> Database models definition
├── db.py --> Database session initialization 
├── dependencies.py --> Dependency injection support
├── settings.py --> Constants and environment variables
```
## 🚀 Getting started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Make](https://www.gnu.org/software/make/)
- [Docker Compose](https://docs.docker.com/compose/install/) 

### Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:achrafbou1/ulb-technical-test.git
   cd ulb-technical-test/partie-1
   ```
2. **Build**
    ```bash
   make build
   ```
3. **Run**
    ```bash
   make run
   ```
## 📚 API Documentation
- **Swagger UI**: http://localhost:8000/docs

- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing
**Run tests**

```bash
   make test
   ```

## General comments 

- There is repeated code in the controllers which can be refactored into a base class, however it would introduce more cognitive complexity so duplicating the code should be fine

- Since tables already exist in the database, we could also use sqlalchemy reflection to get the schemas dynamically, but in a production setting defining models with data types and constraints is preferrable and was used.

- ChatGPT and DeepSeek were used mainly to provide documentation and best practices to enhance code quality, most of the code should be self-documented
