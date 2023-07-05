from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

import imapclient
try:

    import pyzmail
except:
    import pyzmail36 as pyzmail
import webbrowser
import bs4
import os,json

# User input
user_email = os.environ.get("email")
user_pass = os.environ.get("password")




# Connects to IMAP Server
imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_obj.login(user_email, user_pass)
imap_obj.select_folder('INBOX', readonly=True)
UIDs = imap_obj.gmail_search('unsubscribe')

raw_messages = imap_obj.fetch(UIDs, ['BODY[]'])
data={}
for i in UIDs:
    # input("enter:")
    message = pyzmail.PyzMessage.factory(raw_messages[i][b'BODY[]'])

    raw_soup = message.html_part.get_payload().decode(message.html_part.charset)
    soup = bs4.BeautifulSoup(raw_soup, 'html.parser')
    for unsub in soup.find_all('a'):
        # print((unsub.text, unsub.get('href')))
        if 'unsubscribe' in unsub.text.lower():
            domain=urlparse(unsub.get('href')).netloc
            print(domain)
            print((unsub.text, unsub.get('href')))
            datapoop=None
            try:
                datapoop=data[domain]
            except:
                pass
            if  type(datapoop)== list:
                if not unsub.get('href') in data[domain] and bool(urlparse(unsub.get('href')).scheme):
                    data[domain].append(unsub.get('href'))
            else:
                data[domain]=[unsub.get('href')]


imap_obj.logout()

json.dump(data,open("data.json","w"));

unsubscribeAllOrCustome=input("unsubscribe All Or Custome write A for all and any thing for c: ")
openOneByOne=input("Open One By One default y/n (f)")
if openOneByOne.lower().startswith("y"):
    openOneByOne=True;
else:
    openOneByOne=False
if unsubscribeAllOrCustome.lower()=="a":
    for i in data.keys():
        webbrowser.open(data[i][-1])
else:
    print("Open view.html in you browser and select which you wanted to unsubscribe")
    print("After that run 'python3 unsubs.py'")