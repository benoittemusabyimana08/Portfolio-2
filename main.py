from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Benoitte - Portfolio")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Portfolio data
PORTFOLIO_DATA = {
    "name": "Benoitte",
    "role": "Full-Stack Software Engineer & Python Developer",
    "bio": (
        "Passionate software developer focused on building scalable, modern web "
        "applications, high-performance APIs with FastAPI, and responsive user interfaces."
    ),
    "profile_image": "/static/images/alinafe.jpg",
    "contact": {
        "email": "benoitte@example.com",
        "phone": "+265 999 000 000",
        "location": "Lilongwe, Malawi",
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "twitter": "https://twitter.com"
    },
    "skills": [
        {"name": "Python & FastAPI", "level": 92, "category": "Backend"},
        {"name": "JavaScript / TypeScript", "level": 85, "category": "Frontend"},
        {"name": "HTML5 & Modern CSS", "level": 90, "category": "Frontend"},
        {"name": "PostgreSQL & SQLite", "level": 82, "category": "Database"},
        {"name": "RESTful APIs & Microservices", "level": 90, "category": "Backend"},
        {"name": "Git & GitHub", "level": 88, "category": "DevOps"},
        {"name": "Docker & Deployment", "level": 78, "category": "DevOps"},
        {"name": "Tailwind & Bootstrap", "level": 86, "category": "Design"}
    ],
    "projects": [
        {
            "title": "FastAPI Web Ecosystem",
            "description": "High-throughput asynchronous REST API built with FastAPI, Pydantic data validation, and Jinja2 template rendering.",
            "tech": ["Python", "FastAPI", "Uvicorn", "Jinja2"],
            "category": "Backend",
            "link": "#"
        },
        {
            "title": "Interactive Client Portfolio",
            "description": "Clean, glassmorphism dark-themed portfolio featuring real-time interactive sections, animated skill bars, and a contact form.",
            "tech": ["HTML5", "CSS3", "JavaScript"],
            "category": "Frontend",
            "link": "#"
        },
        {
            "title": "Database Management System",
            "description": "Full relational data engine with automated migrations, connection pooling, and secure JWT authentication endpoints.",
            "tech": ["Python", "SQLAlchemy", "PostgreSQL"],
            "category": "Database",
            "link": "#"
        },
        {
            "title": "Task Automation CLI",
            "description": "Python-powered command-line automation tool streamlining backups, data scraping, and file transformations.",
            "tech": ["Python", "AsyncIO", "Click"],
            "category": "Automation",
            "link": "#"
        }
    ],
    "experience": [
        {
            "role": "Software Developer",
            "company": "Tech Solutions",
            "period": "2024 - Present",
            "description": "Architecting clean REST APIs with FastAPI, designing responsive frontends, and maintaining relational databases."
        },
        {
            "role": "Junior Backend Developer",
            "company": "Innovation Labs",
            "period": "2023 - 2024",
            "description": "Built core service integrations, optimized database query execution times, and automated deployment pipelines."
        }
    ],
    "services": [
        {
            "icon": "code",
            "title": "API Development",
            "description": "High-performance, secure asynchronous APIs using FastAPI and Pydantic with automated OpenAPI / Swagger documentation."
        },
        {
            "icon": "layout",
            "title": "Full-Stack Web Apps",
            "description": "Responsive, intuitive frontends coupled with resilient backend servers built to provide seamless user experiences."
        },
        {
            "icon": "database",
            "title": "Database Architecture",
            "description": "Relational data schema design, query optimization, migrations, and caching mechanisms."
        },
        {
            "icon": "zap",
            "title": "Performance Optimization",
            "description": "Async execution, server-side caching, image compression, and streamlined network payloads."
        }
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # request must be the first positional argument for the installed Starlette
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"portfolio": PORTFOLIO_DATA},
    )

@app.get("/api/profile")
async def get_profile():
    return PORTFOLIO_DATA

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
