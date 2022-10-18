import requests
import urllib3
import pyfiglet

banner = pyfiglet.figlet_format("-=D1SC0V3RY=-")
print(banner)

site = input('Site: ')
wordList = input('WordList(abs path): ')

file = open(wordList)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for d in file.readlines():
   request_ = requests.get(site + '/' + d.replace('\n',''), verify = False)

   if str(request_.status_code) != "404":
      print(request_.url + "status=>" + str(request_.status_code))
