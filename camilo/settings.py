import os
import configparser
from functools import lru_cache
from potion_client import Client
from potion_client.auth import HTTPBearerAuth
import requests

RC_FILE = os.path.expanduser('~/.camilorc')
config = configparser.ConfigParser()

if os.path.exists(os.path.expanduser(RC_FILE)):
    config.read(RC_FILE)


class Default(object):
    M8A_API = os.environ.get('METABOLICA_API') or config.get(
        'defaults', 'metabolica_api', fallback=None)
    M8A_TOKEN = os.environ.get('METABOLICA_TOKEN') or config.get(
        'defaults', 'token', fallback=None)
    M8A_BIOSUSTAIN = 'https://iloop.biosustain.dtu.dk/api'
    API_ADDRESS = os.environ.get('DECAF_API') or config.get(
        'defaults', 'decaf_api', fallback=None)
    NOT_PUBLIC = {'NPC'}
    headers = {'Authorization': M8A_TOKEN} if M8A_TOKEN else {}


@lru_cache(128)
def metabolica_client():
    """Get a client for metabolica.
    """
    requests.packages.urllib3.disable_warnings()
    return Client(
        Default.M8A_API,
        auth=HTTPBearerAuth(Default.M8A_TOKEN),
        verify=False
    )
