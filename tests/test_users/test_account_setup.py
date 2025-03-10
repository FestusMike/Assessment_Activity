import pytest
from rest_framework.reverse import reverse
from users.models import UserAccount
from faker import Faker

faker = Faker()

@pytest.mark.django_db
def test_create_user(api_client, db):
    url = reverse("users-create-user")
    data = {"email": faker.email()}
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data["success"] is True
    assert UserAccount.objects.filter(email=data["email"]).exists()

@pytest.mark.django_db
def test_create_user_duplicate_email(api_client, user, db):
    url = reverse("users-create-user")
    data = {"email": user.email}
    response = api_client.post(url, data)
    assert response.status_code == 400
    assert response.data["success"] is False
    assert "User with this email already exists" in response.data["details"][0]["detail"]

@pytest.mark.django_db
def test_update_user(api_client, user, db):
    url = reverse("users-update-user")
    data = {
        "email": user.email,
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "age": faker.random_int(min=1, max=100)
    }
    response = api_client.patch(url, data)
    assert response.status_code == 200
    assert response.data["success"] is True
    user.refresh_from_db()
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert user.age == data["age"]

@pytest.mark.django_db
def test_update_user_not_found(api_client, db):
    url = reverse("users-update-user")
    data = {
        "email": faker.email(),
        "first_name": faker.first_name()
    }
    response = api_client.patch(url, data)
    assert response.data["success"] is False
    assert "User not found. Complete signup first" in response.data["details"][0]["detail"]

@pytest.mark.django_db
def test_partial_update_user(api_client, user, db):
    url = reverse("users-update-user")
    data = {"email": user.email, "age": faker.random_int(min=1, max=100)}
    response = api_client.patch(url, data)
    assert response.status_code == 200
    user.refresh_from_db()
    assert user.age == data["age"]
