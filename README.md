```markdown
# "Lyric Match" - AI-Powered Song Guessing Game

This repository contains a full-stack web application with a Vite-powered React frontend and a Flask backend. Follow the steps below to set up the development environment for both the frontend and backend.

## Prerequisites

- [Node.js](https://nodejs.org/en/) (for frontend)
- [Python 3.8+](https://www.python.org/downloads/) (for backend)
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/Sparkonix11/LyricMatch.git
cd LyricMatch
```

### 2. Frontend Setup (Vite + React)

Navigate to the `frontend` folder, then install the frontend dependencies using `npm`.

```bash
cd frontend
npm install
```

Once the dependencies are installed, you can start the frontend development server:

```bash
npm run dev
```

This will start the Vite development server, and the frontend will be accessible at `http://localhost:5173`.

### 3. Backend Setup (Flask with Waitress)

Navigate to the `backend` folder and set up a virtual environment for the Flask backend.

```bash
cd backend
python3 -m venv venv
```

Activate the virtual environment:

- On **Windows**:

    ```bash
    .\venv\Scripts\activate
    ```

- On **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

Install the backend dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file inside the `backend` folder. Add the following environment variable to the `.env` file:

```
GOOGLE_API_KEY=your-google-api-key
```

Make sure to replace `your-google-api-key` with your actual Google API key.

### 5. Running the Backend with Waitress

Once the dependencies are installed and the `.env` file is set up, you can start the Flask backend server using `waitress-serve`:

```bash
waitress-serve --host 0.0.0.0 --port 8080 app:app
```

This will run the Flask app, and it will be accessible at `http://localhost:8080`.

### 6. Accessing the Application

- The frontend will be accessible at `http://localhost:5173`.
- The backend will be accessible at `http://localhost:8080`.

Make sure both servers are running to interact with the full application.