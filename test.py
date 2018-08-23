import re
import requests
from bs4 import BeautifulSoup

r = requests.get("http://soauniversity.ac.in/iter")
soup = BeautifulSoup(r.text, "html.parser")


def check_ip(address):
    prog = re.compile(
        '^http[s]?:\/\/((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])')
    if prog.match(address):
        return True
    else:
        return False


for link in soup.find_all('a'):
    if check_ip(link.get('href')) == True:
        print(link.get('href'))
