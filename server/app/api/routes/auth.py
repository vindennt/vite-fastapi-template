from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from supabase import create_client, Client, AuthApiError

from app.core.auth import SuperClient

import logging

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

# Helper function to format the authentication response
def format_auth_response(session, message: str):
    if not session:
        raise HTTPException(status_code=401, detail="Authentication failed")

    return {
        "session": {
            "access_token": session.access_token,
            "refresh_token": session.refresh_token,
            "expires_in": session.expires_in,
            "token_type": session.token_type,
            "user": {
                "id": session.user.id,
                "email": session.user.email,
            }
        },
        "message": message
    }

# Signup endpoint
@router.post("/signup")
async def auth_signup(super_client: SuperClient, payload: AuthRequest):
    try:
        response = await super_client.auth.sign_up({
            "email": payload.email,
            "password": payload.password,
        })

        return format_auth_response(response.session, "Signup & signin successful")

    except AuthApiError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error during signup")
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))

# Signin endpoint
@router.post("/signin")
async def auth_signin(super_client: SuperClient, payload: AuthRequest):
    try:
        response = await super_client.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password,
        })
        return format_auth_response(response.session, "Signin successful")

    except AuthApiError as e:
        raise HTTPException(status_code=401, detail="Authentication failed: " + str(e))
    except Exception as e:
        logger.exception("Unexpected error during signin")
        raise HTTPException(status_code=500, detail="Unexpected error: " + str(e))