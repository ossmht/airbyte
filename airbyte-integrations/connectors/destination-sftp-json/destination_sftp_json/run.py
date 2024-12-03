import sys

from airbyte_cdk.entrypoint import launch
from destination_sftp_json import DestinationSftpJson


def run():
    destination = DestinationSftpJson()
    launch(destination, sys.argv[1:])
