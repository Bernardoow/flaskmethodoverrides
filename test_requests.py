# -*- coding: utf-8 -*-
import pytest

from app_flask import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_patch_function(client):
    """Start with a blank database."""

    rv = client.patch('/')
    assert b'PATCH Return' in rv.data


def test_patch_method_view(client):
    """Start with a blank database."""

    rv = client.patch('/tests/')
    assert b'MethodView PATCH Return' in rv.data


def test_post_function_with_header_patch(client):
    """Start with a blank database."""

    rv = client.post('/', headers={'X_HTTP_METHOD_OVERRIDE': 'PATCH'})
    assert b'PATCH Return' in rv.data


def test_post_method_view_with_header_patch(client):
    """Start with a blank database."""

    rv = client.post('/tests/', headers={'X_HTTP_METHOD_OVERRIDE': 'PATCH'})
    assert b'MethodView PATCH Return' in rv.data
