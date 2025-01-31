# Project 0

## Description
Project_0 is a web application that uses FastAPI for the backend and Vite with React for the frontend. This project send a get request to the backend using axios and display a json structured output of three keys which are email,current_datetime and github_url.

## Setup Instructions

### Backend (FastAPI)
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Black-fox17/project_IT
    cd project_0/backend
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```

### Frontend (Vite with React)
1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```

2. **Install dependencies:**
    ```bash
    npm install
    ```

3. **Run the development server:**
    ```bash
    npm run dev
    ```

## Backlink
[The backlink](https://hng.tech/hire/python-developers).
