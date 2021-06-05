from pyinfra.api import deploy
from pyinfra.operations import files, init, server, pip
from pyinfra import local

from pyinfra import logger

from .defaults import DEFAULTS


@deploy('Setup user account', data_defaults=DEFAULTS)
def setup_app(
   state,host,ex_settings=None
   ):
   logger.info("ex_settings initial value : {}".format(ex_settings))
   if (not ex_settings) and host.data.settings:
      ex_settings = host.data.settings

   logger.info("ex_settings after value : {}".format(ex_settings))
   
