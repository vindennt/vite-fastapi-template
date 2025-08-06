import uuid

from sqlmodel import Field, SQLModel

# Base model for tables owned by a user
class UserOwnedBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner_id: uuid.UUID = Field(
        foreign_key="auth.users.id", nullable=False, ondelete="CASCADE"
    )