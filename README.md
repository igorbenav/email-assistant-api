
# LLM Powered API with FastAPI and FastCRUD

This project demonstrates how to create a personalized email writing assistant using FastAPI, OpenAI's API, and FastCRUD.

## Prerequisites

- **Python 3.9+**: Ensure you have Python 3.9 or a newer version installed.
- **Poetry**: A dependency manager for Python. Install it with `pip install poetry`.
- **OpenAI API Key**: Sign up and get an API key from OpenAI's website.
- **Access to a Terminal (macOS or Linux)**: Use the terminal for setting up the project and managing dependencies.

**Tip for Windows Users**: Use Windows Subsystem for Linux (WSL) to follow along with this tutorial.

## Project Setup

1. **Create a Project Folder**:
    ```bash
    mkdir email-assistant-api
    cd email-assistant-api
    ```

2. **Initialize a Poetry Project**:
    ```bash
    poetry init
    ```

3. **Add Dependencies**:
    ```bash
    poetry add fastapi fastcrud sqlmodel openai aiosqlite greenlet python-jose bcrypt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the `app` directory with the following content:
    ```plaintext
    OPENAI_API_KEY="your_openai_api_key"
    SECRET_KEY="your_secret_key"
    ```

## Project Structure

```
email_assistant_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # The main application file
│   ├── routes.py      # Contains API route definitions and endpoint logic
│   ├── database.py    # Database setup and session management
│   ├── models.py      # SQLModel models for the application
│   ├── crud.py        # CRUD operation implementations using FastCRUD
│   ├── schemas.py     # Schemas for request and response models
│   └── .env           # Environment variables
│
├── pyproject.toml     # Project configuration and dependencies
├── README.md          # Provides an overview and documentation
└── .gitignore         # Files to be ignored by version control
```

## Running the Application

To start the application, run:

```bash
poetry run uvicorn app.main:app --reload
```

Open a browser and navigate to `127.0.0.1:8000/docs` to access the API documentation.

## Connect with Me

If you have any questions, want to discuss tech-related topics, or share your feedback, feel free to reach out to me on social media:
- **GitHub**: [igorbenav](https://github.com/igorbenav)
- **Twitter**: [igorbenav](https://twitter.com/igorbenav)
- **LinkedIn**: [Igor](https://linkedin.com/in/igor)
