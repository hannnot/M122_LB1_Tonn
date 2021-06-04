from configparser import ConfigParser
import yagmail
from datetime import datetime
from ftplib import FTP_TLS


# This method is preparing and sending an email to the email which is
# extracted from a file
def sendMail(config: ConfigParser, receiver: str):
    yag = yagmail.SMTP(config['GMAILCONFIG']['email'],
                       config['GMAILCONFIG']['pwd'])
    yag.send(
        to=receiver,
        subject="Hello from your python program",
        contents="This is a test e-mail. In the attachment you'll find a pdf document.",
        attachments=config['ATTACHMENTFILE']['path'],
    )

# This function reads a given .txt file and extracts the email
# address in it. From this function the email address is returned as string
def openEmailFile(config: ConfigParser):
    file = open(config['EMAILFILE']['path'], 'r')
    email = file.read()
    return email


# This function is creation a new .txt file with the current datetime as filename
# from this function the file name is returned as string and the file is stored in the
# location specified in the config file
def writeFile(config: ConfigParser):
    timestamp = datetime.now()
    fileName = timestamp.strftime("%d%m%Y%H%M%S.txt")
    with  open(config['OUTPUTFILE']['path']+fileName, "a") as file :
        file.write(timestamp.strftime("%d.%m.%Y at %H:%M:%S") + " : " + openEmailFile(config))
    return fileName


# This function is responsible for uploading the file to a certain FTP-Server
# specified in the config file.
def uploadFileFTP(config: ConfigParser):
    session = FTP_TLS(config['FTPCONFIG']['host'],
                      config['FTPCONFIG']['user'], config['FTPCONFIG']['pwd'])
    session.cwd('m122')
    fileName = writeFile(config)
    path = config['OUTPUTFILE']['path'] + fileName
    with open(path, "rb") as file:
        session.storbinary('STOR ' + fileName, file)
    session.quit()
 
