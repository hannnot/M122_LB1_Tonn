# M122_LB1_Tonn
##	Betriebsdokumentation
### Betriebsanleitung (only Windows)
1. Erstellen Sie ein .txt Dokument. 
    *  Das Dokument darf nur eine E-Mail Addresse enthalten
    * Die E-Mail Addresse muss gültig sein

2. Erstellen Sie ein .pdf Dokument
3. Clonen Sie das Projekt aus nachfolgendem Repo
    *   https://github.com/hannnot/M122_LB1_Tonn.git
4. Erstellen Sie eine `config.ini` Datei mit folgenden Attributen: <br>
[EMAILFILE]  
path = path_to_your_email_TXT_file/email.txt
[ATTACHMENTFILE] <br>
path = path_to_your_PDF_attachment_file/attachment.pdf <br> <br>
[OUTPUTFILE] <br>
path = C:\Users\path_to_your_desired_output_location <br> <br>
[GMAILCONFIG]<br>
email = your@gmail.com<br>
pwd = yourpassword <br> <br>
[FTPCONFIG]<br>
host = your.ftp.server.com <br>
user = yourFTPusername<br>
pwd = yourFTPpassword <br>
<br>
<b>WICHTIG:<br>Im `[GMAILCONFIG]` muss eine GMail Adresse angegeben werden</b><br>
das config.ini file speichern Sie im Ordner des zuvor geclonten Projekts

5. Überprüfen Sie Ihren Computer auf eine vorhandene Python installation in dem sie nachfolgenden Befehl in ein Windows Terminal eingeben:
`python`
    *  falls Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) bereits installiert ist gehen Sie bei Punkt 6 weiter
    * falls nicht installieren Sie python über die Entwicklerseite <br>
    https://www.python.org/downloads/windows/ <br>
    und installieren Sie den Python 3
6. Öffnen Sie einen Windwos Terminal und geben Sie folgenden Befehl ein: <br>
`pip install yagmail`

7. Falls Sie python zu Ihren Umgebungsvariabeln hinzugefügt haben:

    * öffnen Sie ein Windows Terminal im Ordner des geclonten Projekts und geben Sie folgenden Befehl ein: <br>
    `python main.py`
    
    falls nicht:

    * öffnen Sie einen Windwos Explorer und navigieren Sie in den Installationsordner von Python, kopieren Sie den Pfad (incl. \python.exe)
    * öffnen Sie ein Windows Terminal im Ordner des geclonten Projekts und geben Sie folgenden Befehl ein: <br>
    `path_to_your\python.exe main.py`



