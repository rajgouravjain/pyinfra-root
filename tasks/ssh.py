from pyinfra.api import deploy
from pyinfra.operations import files, init, server, pip

from pyinfra import logger
from pyinfra import host

from utils import get_file_path
from utils import get_template_path
from utils import get_task_path

bash_profile_file = get_file_path('team_user_bash_profile')

files.put(
        src = bash_profile_file,
        dest = '{}/.bash_profile'.format(host.data.team_user_home),
        user=host.data.team_user,
        group=host.data.team_user,
        mode=755,
    )

files.directory(
        path = '{}/.ssh/'.format(host.data.team_user_home),
        present=True,
        assume_present=False, 
        user=host.data.team_user,
        group=host.data.team_user,
        mode=700,
        recursive=True,
    )

ssh_key_template = get_template_path("ssh_key.j2")

files.template(
        name='Create a public key file',
        src=ssh_key_template,
        dest='{}/.ssh/id_rsa.pub'.format(host.data.team_user_home),
        content=host.data.team_user_ssh_public_key,
    )
