# Code adapted from https://github.com/AtticusZeller/fastapi_supabase_template/

import logging
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from supabase import AsyncClientOptions
from supabase._async.client import AsyncClient, create_client

from app.core.config import settings
from app.db.schemas.auth import UserIn

# Get the client for supabase database
async def get_super_client() -> AsyncClient:
    """for validation access_token init at life span event"""
    super_client = await create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY,
        options=AsyncClientOptions(
            postgrest_client_timeout=10, storage_client_timeout=10
        ),
    )
    if not super_client:
        raise HTTPException(status_code=500, detail="Super client not initialized")
    return super_client


# Dependency for the database client
SuperClient = Annotated[AsyncClient, Depends(get_super_client)]

# auto get token from header
reusable_oauth2 = OAuth2PasswordBearer(
    # tokenUrl=f"{settings.API_V_STR}/login/access-token"
    tokenUrl=f"/login/access-token"
)
TokenDep = Annotated[str, Depends(reusable_oauth2)]

# get current user from token and validate same time
async def get_current_user(token: TokenDep, super_client: SuperClient) -> UserIn:
    """get current user from token and  validate same time"""
    user_response = await super_client.auth.get_user(jwt=token)
    if not user_response:
        logging.error("User not found")
        raise HTTPException(status_code=404, detail="User not found")
    return UserIn(**user_response.user.model_dump(), access_token=token)