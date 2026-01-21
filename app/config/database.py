from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config.settings import settings
from app.models.user import User
from app.models.task import Task

async def connect_db():
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(
        database=client[settings.DATABASE_NAME],
        document_models=[User, Task]
    )
    print("Connected to MongoDB")

async def close_db():
    print("Closed MongoDB connection")