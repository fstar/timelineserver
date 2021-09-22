from pathlib import Path
from dataclasses import dataclass
from yamldataclassconfig.config import YamlDataClassConfig
from yamldataclassconfig import create_file_path_field

print(Path(__file__).parent / 'configs' / 'server.yml')


@dataclass
class ServerConfig(YamlDataClassConfig):
    SQLALCHEMY_DATABASE_URI: str = None  # pylint: disable=C0103

    FILE_PATH: str = create_file_path_field(Path(__file__).parent / 'configs' / 'server.yml')


server_config = ServerConfig()
server_config.load()
