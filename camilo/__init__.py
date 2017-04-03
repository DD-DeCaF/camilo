import logging
import sys
from camilo import settings
from camilo.settings import metabolica_client
from camilo.services import list_experiments, get_model, maps

logger = logging.getLogger('camilo')
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.setLevel(logging.INFO)
