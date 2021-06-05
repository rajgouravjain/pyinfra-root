
from pyinfra import logger
from pyinfra import host

from team_user.team_user import setup_user
from demo_app.demo_app import setup_app

logger.info(host.fact.os)
setup_user()
setup_app(ex_settings=False)
