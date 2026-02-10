**BooksAndAuthors**

A simple, lightweight framework created for recruitment‑process tasks.

**Overview**

This repository provides a minimal codebase for working with books and authors endpoints from https://fakerestapi.azurewebsites.net/index.html.
Although simple, it can serve as a foundation for coding exercises, interviews, or small internal tools.

**Project structure**

BooksAndAuthors/
├── data/              # Input data used by the application
├── src/               # Source code (utils)
├── tests/             # Unit tests (pytest)
├── Dockerfile         # Containerization setup
├── Jenkinsfile        # CI/CD pipeline definition
├── requirements.txt   # Python dependencies
├── Pipfile / Pipfile.lock  # Alternative dependency management
└── pytest.ini         # Pytest configuration

**Prerequisites**

Python 3.x
Pip or Pipenv
(Optional) Docker
(Optional) Jenkins for CI/CD

**Using pip:**

pip install -r requirements.txt
**Using pipenv:**
pipenv install

**Running test cases**

pytest --html=report.html --self-contained-html
