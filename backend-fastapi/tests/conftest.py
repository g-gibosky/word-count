from typing import List
import pytest
from app.main import app
from app.domain.models import User
from app.infrastructure.database import SessionLocal
from faker import Faker

@pytest.fixture(scope="session", autouse=True)
def users_in_db(n=5):
    fake = Faker()
    users = []
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        # Add user to database
        db = SessionLocal()
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        db.close()
        users.append(user)
    yield users  # Provide the list of user objects to the tests
    # #clean up the database after the tests
    db = SessionLocal()
    for user in users:
        db.delete(user)
    db.commit()
    db.close()
    
@pytest.fixture
def create_user():
    fake = Faker()
    username = fake.user_name()
    email = fake.email()
    return [username,email]

@pytest.fixture
def create_multiple_users(qtd: int = 5) -> List:
    users = []
    for _ in range(qtd):
        fake = Faker()
        username = fake.user_name()
        email = fake.email()
        users.append([username,email])
    return users