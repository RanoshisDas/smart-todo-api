from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Token
from app.utils.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter(tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    try:
        # Normalize email
        email = user.email.lower().strip()

        # Check if user already exists
        existing_user = await User.find_one(User.email == email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Hash password and create user
        hashed_password = get_password_hash(user.password)
        new_user = User(
            email=email,
            username=user.username,
            hashed_password=hashed_password
        )
        await new_user.insert()  # Beanie async insert

        return UserResponse(**new_user.dict())

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # OAuth2PasswordRequestForm uses 'username' field for email
        email = form_data.username.lower().strip()
        user = await User.find_one(User.email == email)

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Create JWT token
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(days=7)
        )

        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    try:
        return UserResponse(**current_user.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")
