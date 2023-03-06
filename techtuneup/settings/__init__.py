import os
import json
from pathlib import Path


file_path = Path(__file__).absolute().parent
CONFIG_FILE = "/etc/techtuneup_config.json"
<<<<<<< HEAD
=======

>>>>>>> fix_recaptcha
try:
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        config['PROD']
    from .prod import *


except KeyError:
    from .dev import *

SECRET_KEY = config['SECRET_KEY']
