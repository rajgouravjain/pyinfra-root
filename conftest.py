import pytest
import subprocess
import os
import testinfra
import logging
DOCKER_IMAGE_NAME = 'ubuntu:20.04'

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='class')
def server(request):
    instance = "docker_instance"
    logging.warning(request)  # will print a message to the console
    
    host = testinfra.get_host("docker://"+instance)
    request.cls.host = host
    yield
