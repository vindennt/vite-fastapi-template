from gotrue import User, UserAttributes  # type: ignore
from pydantic import BaseModel

# Edit these files for finetuned control over models returned

# Basic Token properties
class Token(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None


# Inject a fill user into a route
class UserIn(Token, User):
    pass


# Supabase handles the user attributes
class UserCreate(BaseModel):
    pass


# Updating usser attributes
class UserUpdate(UserAttributes):
    pass


# User's Base DB model
class UserInDBBase(BaseModel):
    pass


# User output model
class UserOut(Token):
    pass


# All properties stored in DB
class UserInDB(User):
    pass
