import logging
import sys
from potion_client import Client
from potion_client.auth import HTTPBearerAuth
import requests
from . import settings


logger = logging.getLogger('camilo')
logger.addHandler(logging.StreamHandler(stream=sys.stdout))  # Logspout captures logs from stdout if docker containers
logger.setLevel(logging.INFO)


def iloop_client(api=settings.ILOOP_API, token=settings.ILOOP_TOKEN):
    requests.packages.urllib3.disable_warnings()
    return Client(
        api,
        auth=HTTPBearerAuth(token),
        verify=False
    )
