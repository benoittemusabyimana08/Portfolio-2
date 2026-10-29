# Benoitte - Developer Portfolio (FastAPI)

A modern, responsive personal developer portfolio web application built with **FastAPI**, **Jinja2 Templates**, and custom modern CSS with glassmorphism design.

## Features
- **FastAPI backend**: Fast async server with static asset mounting and JSON API endpoints.
- **Dynamic Jinja2 templating**: Data-driven portfolio rendering (Hero, About, Skills, Services, Projects, Experience, Contact).
- **Personal Photo**: Linked to `static/images/alinafe.jpg`.
- **Responsive design**: Mobile-first navigation, smooth scrolling, interactive cards, and skill progress bars.

## Project Structure
```
Portfolio 2/
├── main.py                 # FastAPI application and route endpoints
├── requirements.txt        # Python package dependencies
├── templates/
│   └── index.html          # Jinja2 portfolio template
├── static/
│   ├── css/
│   │   └── style.css       # Custom modern dark UI styling
│   ├── js/
│   │   └── main.js         # Interactive navigation & animations
│   └── images/
│       └── alinafe.jpg     # Benoitte's profile image
└── README.md
```

## Setup & Run

1. **Activate virtual environment** (or create one):
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI application**:
   ```bash
   python main.py
   # or with uvicorn directly:
   uvicorn main:app --reload --port 8000
   ```

4. **Open your browser**:
   - Web Portfolio: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Interactive API Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
