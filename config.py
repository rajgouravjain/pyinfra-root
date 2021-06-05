# config.py or top of deploy.py

# SSH connect timeout
CONNECT_TIMEOUT = 1

# Fail the entire deploy after 10% of hosts fail
FAIL_PERCENT = 10

REQUIRE_PACKAGES = 'requirements.txt'  # path relative to the deploy
REQUIRE_PACKAGES = [
    'pyinfra',
    'pyinfra-docker',
   ]
