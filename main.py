import configparser
from helper import openEmailFile, sendMail, uploadFileFTP

# This is the main file of this program, here the config file is beeing read 
# and the methods sendMail and uploadFile are beeing called
config = configparser.ConfigParser()
config.read('config.ini')

sendMail(config, openEmailFile(config))
uploadFileFTP(config)