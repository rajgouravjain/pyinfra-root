from pyinfra import logger
from pyinfra import host
from pyinfra import local

logger.info("Host is {}:".format(host.fact.os))

local.include("tasks/ssh.py")
