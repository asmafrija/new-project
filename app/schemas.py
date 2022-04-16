from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserOut(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    creation_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    is_confirmed: Optional[bool] = None
    message: Optional[str] = None
    status: Optional[int] = None

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    confirm_password: str

class UserConfirm(BaseModel):
    is_confirmed: bool

class UserResetPassword(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    message: Optional[str] = None
    status: Optional[int] = None
    user_id: Optional[int] = None
    user_name: Optional[str] = None

class TokenData(BaseModel):
    id: Optional[str] = None

class ForgotPassword(BaseModel):
    email: EmailStr

class ForgotPasswordOut(BaseModel):
    message: Optional[str] = None
    status: Optional[int] = None

class EmailSchema(BaseModel):
    email: List[EmailStr]

class ResetCodeCreate(BaseModel):
    email: EmailStr
    reset_code: str
    status: str

class ConfirmationCodeCreate(BaseModel):
    email: EmailStr
    confirmation_code: str
    status: str

class ResetPassword(BaseModel):
    reset_password_code: str
    new_password: str
    confirm_new_password: str

class ResetPasswordOut(BaseModel):
    message: str
    status: int

class SendConfirmationMail(BaseModel):
    email: EmailStr

class ConfirmAccount(BaseModel):
    confirmation_code: str

class ConfirmAccountOut(BaseModel):
    message: str
    status: int

class ReclamationCreate(BaseModel):
    longitude: float
    latitude: float
    photo_url: str
    description: Optional[str] = None

class ReclamationOut(BaseModel):
    id: Optional[str] = None
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    photo_url: Optional[str] = None
    owner_id: Optional[str] = None
    reclamation_status: Optional[str] = None
    description: Optional[str] = None
    creation_date: Optional[datetime] = None

class ReclamationsOut(BaseModel):
    list: List[ReclamationOut]
    message: Optional[str] = None
    status: Optional[int] = None