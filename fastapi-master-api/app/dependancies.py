from typing import Generator

from app.settings import Settings
from cryptography.fernet import Fernet
from fastapi import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Generator[Session, None, None]:
    db = request.app.state.session()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def encrypt_string(string_to_encrypt: str, settings: Settings) -> str:
    string_as_bytes = str.encode(string_to_encrypt)
    encrypt_client = Fernet(settings.HASH_SECRET)
    return encrypt_client.encrypt(string_as_bytes).decode()


def decrypt_string(string_to_decrypt: str, settings: Settings) -> str:
    string_as_bytes = str.encode(string_to_decrypt)
    encrypt_client = Fernet(settings.HASH_SECRET)
    return encrypt_client.decrypt(string_as_bytes).decode()
