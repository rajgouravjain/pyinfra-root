# pyinfra_users 
# File: pyinfra_users/add_user.py
# Desc: creates dirs for each user

from pyinfra.api import deploy
from pyinfra.operations import files, init, server

from .defaults import DEFAULTS


@deploy('Add User', data_defaults=DEFAULTS)
def add_user(
    state,
    host,
    user,
    group="wheel"
):

    files.directory(
        name='Ensure dirs for each user',
        path='{}/{}/{}'.format("/Users/rajgouravj/",group, user),
        state=state,
        host=host,
    )
