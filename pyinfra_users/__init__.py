# pyinfra users
# File: pyinfra_users/__init__.py
# Desc: export deploys and install/configure helper function

from pyinfra.api import deploy

from .users import add_user

from .defaults import DEFAULTS

@deploy('Deploy User dir')
def deploy_user(state, host, user, group="wheel"):
    add_user(state=state, host=host,user=user,group=group)
