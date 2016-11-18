import os
import configparser
RC_FILE = os.path.expanduser('~/.camilorc')
config = configparser.ConfigParser()

if os.path.exists(os.path.expanduser(RC_FILE)):
    config.read(RC_FILE)

ILOOP_API = os.environ.get('ILOOP_API') or config.get('defaults', 'api', fallback=None)
ILOOP_TOKEN = os.environ.get('ILOOP_TOKEN') or config.get('defaults', 'token', fallback=None)
API_ADDRESS = 'http://api.dd-decaf.eu/model/modify/genotype'

default_models = {
    'ECO': 'iJO1366',
    'SCE': 'iMM904',
    'CHO': 'iMM1415',
    'COG': 'iNJ661',
}
