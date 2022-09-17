import time
import requests
from bs4 import BeautifulSoup
import random
from spoofmac.util import *
from spoofmac.interface import *

random_sleep_time=random.randint(10,15)

total_balance=[]

for i in range(32):   

 
 emails=[]#write your emails here
 
 total_emails=len(emails)
 print('Total emails:',total_emails)

 for xmail in emails:
  def get_tor_session():
     session = requests.session()
    
     session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
     return session


  session = get_tor_session()
  print(session.get("http://httpbin.org/ip").text)



  #print(requests.get("http://httpbin.org/ip").text) 
 

  mac_address=random_mac_address()
  print ('changed mac address:',mac_address,'\n')
  
  index=emails.index(xmail)
  
  email = xmail
  password = "####"#write your password here
 

  r = requests.Session()
  content = r.get("https://presearch.com").content

  soup = BeautifulSoup(content, 'html.parser')
  token = soup.find("input", {
  "name": "_token"
})["value"]

  payload = "_token={}&login_form=1&email={}&password={}".format(token, email, password)
  headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

  login = r.post("https://presearch.com/api/auth/login", data = payload, headers = headers)

  for x in range(1):
    words = random.choice(["apple", "life", "hacker", "facebook", "instagram", "twitter", "youtube", "money", "banana", "lemon", "rice", "chiken", "home", "street", "food", "winter", "pubg", "bot", "love", "freelancing", "presearch", "token", "abuse", "hindi", "translator", "pubg", "horse", "dollar", "india", "china", "earning", "summer", "football", "ronaldo", "messi", "cricket", "python", "java", "perl", "ruby", "free", "swift", "table", "chair", "lamp", "pen", "book", "bed", "donkey", "cow", "cat", "pencil", "class", "school", "oxford", "university", "abs", "gym", "bird", "billioner"])
    payload = "term={}&provider_id=98&_token={}".format(words, token)
    r.post("https://presearch.com/search", data = payload, headers = headers)
    print((i+1),(index+1),"Term:{} Search done!".format(words),xmail)
   # print(session.get("http://httpbin.org/ip").text)
    time.sleep(1)
  r = r.get("https://presearch.com/")
  soup = BeautifulSoup(r.content, 'html.parser')
  balance = soup.find("span", {
  "class": "number ajax balance"
})
  print("                                      Your Balance: {} PRE \n\n".format(balance.text))
 
  
  int_balance=float(balance.text)
  total_balance.append(int_balance)
print('TOTAL BALANCE:',sum(total_balance),'PRE')
