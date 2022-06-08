import pytest
from django.contrib.auth.models import User, Permission

from rest_api_app.models import Book, Author

@pytest.fixture
def user():
    user = User.objects.create_user(username='gosia', password='gosia', is_superuser=True)
    return user

@pytest.fixture
def book():
    return Book.objects.create(title="Books")

@pytest.fixture
def author():
    return Author.objects.create(title="Xxx")