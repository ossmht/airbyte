import sys

from destination_sftp_json import DestinationSftpJson


def run():
    DestinationSftpJson().run(sys.argv[1:])

if __name__ == "__main__":
    run()