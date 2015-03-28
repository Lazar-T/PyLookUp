import time
import re
import sys
import urllib
from bs4 import BeautifulSoup
from PySide.QtCore import *
from PySide.QtGui import *
from twilio.rest import TwilioRestClient


app = QApplication(sys.argv)

url_of_page = raw_input("Enter address that needs to be searched: ")
search_text = raw_input("Enter phrase to be found: ")


def find_test():
    page = urllib.urlopen(url_of_page)
    soup = BeautifulSoup(page)

    foundedText = soup.find('a', text=re.compile(search_text))

    if not foundedText:
        print "Nothing founded, searching again in 5 minutes."
    else:
        link_to_page = foundedText.get("href")
        # Opening web page in browser
        label = QLabel("<font color=green size=72>" + "Phrase is found, opening web page now." + "</font>")
        openPage = QDesktopServices.openUrl(QUrl(link_to_page))
        label.setWindowFlags(Qt.SplashScreen)
        label.show()
        QTimer.singleShot(7000, app.quit)
        app.exec_()
        # Sending SMS to phone
        account_sid = ""
        auth_token = ""
        client = TwilioRestClient(account_sid, auth_token)
        message = (client.sms.messages.create(body="" +
        link_to_page, to="", from_=""))
        exit()


while True:
    find_test()
    time.sleep(300)
