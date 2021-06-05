from pyinfra.api import deploy
from pyinfra.operations import files, init, server, pip

from pyinfra import logger
from pyinfra import local

from utils import get_file_path
from utils import get_template_path
from utils import get_task_path

from .defaults import DEFAULTS


@deploy('Setup team user account', data_defaults=DEFAULTS)
def setup_user(
    state, host,
    ):
    server.user(
        name='Create a team user',
        user=host.data.team_user,
        shell='/bin/bash',
        home=host.data.team_user_home,
        ensure_home=True,
        system=False,
        public_keys=None,
        host=host,
	state=state,
    )
    ##Include ssh setup task
    ssh_task_file = get_task_path("team_user/tasks/ssh.py")
    local.include(ssh_task_file)
