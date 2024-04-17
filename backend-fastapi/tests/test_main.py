# tests/test_user.py
import pytest
from httpx import AsyncClient
from app.main import app
from tests.conftest import create_user  # adjust the import path according to your project structure

@pytest.mark.asyncio
async def test_create_user(create_user):
    user = create_user
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.post("/users/add", json={"username": user[0], "email": user[1]})
    assert response.status_code == 200
    assert response.json()["username"] ==  user[0]
    
@pytest.mark.asyncio
async def test_update_user(create_user):
    user_id = 1  # assuming there is already a user with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.put(f"/users/{user_id}", json={"username": "updateduser", "email": "updated@example.com"})
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
    
    
# TODO: Complete o teste abaixo
@pytest.mark.asyncio
async def test_get_user_by_email(users_in_db):
   pass
    
# TODO: Crie um teste para listar todos os usuários no banco


# TODO: Complete o teste abaixo
@pytest.mark.asyncio
async def test_delete_user():
    user_id = 1  # assuming there is already a user with id 1
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["msg"] == "User deleted successfully"


# TODO: Crie teste de add Twite

# TODO: Crie teste de list_all_twite_from_user

# TODO: Crie teste de list_twite (por id) 