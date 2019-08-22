import sys
import configparser
import os
import getpass

config = configparser.RawConfigParser()
config_file = os.path.expanduser('~/.twitter.conf')
config.read(config_file)

APPLICATION_ID = config.get('aylien', 'APPLICATION_ID')
APPLICATION_KEY = config.get('aylien', 'APPLICATION_KEY')
