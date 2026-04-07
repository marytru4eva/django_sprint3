from http import HTTPStatus

import pytest
from django.apps import apps
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer as _mixer

try:
    from blog.models import Category, Location, Post
except ImportError:
    raise AssertionError(
        'В приложении `blog` опишите '
        'модели `Post, Category, Location`'
    )
except RuntimeError:
    registered_apps = set(app.name for app in apps.get_app_configs())
    need_apps = {'blog': 'blog', 'pages': 'pages'}
    if not set(need_apps.values()).intersection(registered_apps):
        need_apps = {
            'blog': 'blog.apps.BlogConfig', 'pages': 'pages.apps.PagesConfig'
        }

    for need_app_name, need_app_conf_name in need_apps.items():
        if need_app_conf_name not in registered_apps:
            raise AssertionError(
                f'Убедитесь, что зарегистрировано приложение {need_app_name}'
            )


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def user():
    User = get_user_model()
    return User.objects.create_user(username='testuser')


@pytest.fixture
def author():
    User = get_user_model()
    return User.objects.create_user(username='author')


@pytest.fixture
def category(mixer):
    return mixer.blend(Category)


@pytest.fixture
def location(mixer):
    return mixer.blend(Location)


@pytest.fixture
def post(mixer, author, category, location):
    return mixer.blend(Post, author=author, category=category, location=location)


@pytest.fixture
def client():
    from django.test.client import Client
    return Client()
