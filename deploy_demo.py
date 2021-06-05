from team_user.team_user import setup_user
from demo_app.demo_app import setup_app
from pyinfra import logger
from pyinfra import host

logger.info("Host is {}:".format(host.fact.os))

setup_user()
setup_app()
