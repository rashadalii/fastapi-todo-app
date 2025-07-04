import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]

@pytest.fixture
def test_user(client):
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "username": "testuser",
        "password": "testpass"
    }
    res = client.post("/api/v1/auth/register", json=user_data)
    assert res.status_code == 200
    return res.json()

@pytest.fixture
def test_user_token(client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpass"
    }
    res = client.post("/api/v1/auth/login", data=login_data)
    return res.json()