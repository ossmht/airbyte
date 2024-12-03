import sys

from airbyte_cdk.entrypoint import launch
from destination_sftp_json import DestinationSftpJson


def run():
    destination = DestinationSftpJson()
    launch(sodestinationurce, sys.argv[1:])