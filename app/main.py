from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import connect_db, close_db
from app.routers import auth, tasks

app = FastAPI(
    title="Smart ToDo API",
    description="A robust task management system with authentication",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Event handlers
@app.on_event("startup")
async def startup_event():
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Smart ToDo API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}