import configparser
import json

from sdk.rai_credentials import RAICredentials

from pathlib import Path

class RAIConfig(object):
    def __init__(self, profile:str="default", config_path:str=str("{}/.rai/config".format(Path.home()))):
        self.parse_config(profile=profile, config_path=config_path)

    def parse_config(self, profile:str="default", config_path:str=str("{}/.rai/config".format(Path.home()))):
        config = configparser.ConfigParser()
        config.read(config_path)

        self.region = config[profile]["region"]
        self.host = config[profile]["host"]
        self.port = config[profile]["port"]
        self.infra = config[profile]["infra"]

        private_key_filename = config[profile]["private_key_filename"]
        private_key_file_content = Path("{}/{}".format(Path(config_path).parent, private_key_filename)).read_text()

        private_key = json.loads(private_key_file_content)["sodium"]["seed"]
        access_key = config[profile]["access_key"]
        self.creds = RAICredentials(private_key=private_key, access_key=access_key)
