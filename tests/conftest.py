__author__ = "Christian Kongsgaard"
__license__ = 'MIT'

import pytest


@pytest.fixture
def repo_updates():
    yield r'C:\Users\ocni\PycharmProjects\swarm-ops'
