from pyinfra.api import deploy
from pyinfra.operations import files, init, server, pip
from pyinfra import local

from pyinfra import logger

from utils import get_file_path
from utils import get_template_path
from utils import get_task_path

from .defaults import DEFAULTS


@deploy('Setup user account', data_defaults=DEFAULTS)
def setup_app(
    state,host
    ):
    pass
