import configparser
import json
import os

from sdk.rai_credentials import RAICredentials

from pathlib import Path

class RAIConfig(object):
    def __init__(self, profile:str="default", config_path:str=str("{}/.rai/config".format(Path.home()))):
        self.profile = profile
        self.path = config_path

    def parse_config(self):
        if os.path.isfile(self.path):
            config = configparser.ConfigParser()
            config.read(self.path)

            self.region = config[self.profile]["region"]
            self.host = config[self.profile]["host"]
            self.port = config[self.profile]["port"]
            self.infra = config[self.profile]["infra"]

            private_key_filename = config[self.profile]["private_key_filename"]
            private_key_file_content = Path("{}/{}".format(Path(self.path).parent, private_key_filename)).read_text()

            private_key = json.loads(private_key_file_content)["sodium"]["seed"]
            access_key = config[self.profile]["access_key"]
            self.creds = RAICredentials(private_key=private_key, access_key=access_key)
        else:
            raise Exception("{} RAI configuration file not found.".format(self.path))
        return self