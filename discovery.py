import requests

site = input('Site: ')
wordList = input('WordList(abs path): ')

file = open(wordList)

for d in file.readlines():
   request_ = requests.get(site + '/' + d.replace('\n',''))

   if str(request_.status_code) != "404":
      print(request_.url + "status=>" + str(request_.status_code))
