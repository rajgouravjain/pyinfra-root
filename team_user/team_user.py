from pyinfra.api import deploy
from pyinfra.operations import files, init, server, pip

from pyinfra import host
from pyinfra import logger
from pyinfra import local

from .utils import get_file_path
from .utils import get_template_path
from .utils import get_task_path

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

    bash_profile_file = get_file_path('team_user_bash_profile')

    files.put(
        src = bash_profile_file,
        dest = '{}/.bash_profile'.format(host.data.team_user_home),
        user=host.data.team_user,
        group=host.data.team_user,
        mode=755,
        host=host,
	state=state,
    )

    files.directory(
        path = '{}/.ssh/'.format(host.data.team_user_home),
        present=True,
        assume_present=False, 
        user=host.data.team_user,
        group=host.data.team_user,
        mode=700,
        recursive=True,
        host=host,
	state=state,
    )

    ssh_key_template = get_template_path("ssh_key.j2")

    files.template(
        name='Create a public key file',
        src=ssh_key_template,
        dest='{}/.ssh/id_rsa.pub'.format(host.data.team_user_home),
        content=host.data.team_user_ssh_public_key,
        user=host.data.team_user,
        group=host.data.team_user,
        mode=644,
        host=host,
	state=state,
    )
