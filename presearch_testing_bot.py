import requests
from bs4 import BeautifulSoup
import random
import time


for i in range(10):   

 
 emails= ['b.on.a.s.4.15.0@gmail.com','b.onas.41.50@gmail.com','b.o.na.s41.5.0@gmail.com','b.onas4.1.5.0@gmail.com','b.o.na.s.4.1.5.0@gmail.com','b.o.nas4.1.5.0@gmail.com','bonas41.50@gmail.com','b.on.as4.1.50@gmail.com','bo.n.a.s.4.1.5.0@gmail.com','b.on.as.415.0@gmail.com','bonas.4.15.0@gmail.com','bo.n.a.s41.50@gmail.com','b.o.n.a.s4.150@gmail.com','bon.a.s415.0@gmail.com','b.o.n.a.s41.5.0@gmail.com','bon.as41.50@gmail.com','b.onas4.1.50@gmail.com','b.o.n.a.s.41.5.0@gmail.com','bonas4.1.50@gmail.com','b.o.nas.4150@gmail.com','bon.as41.5.0@gmail.com','bo.na.s41.5.0@gmail.com','bo.n.a.s41.5.0@gmail.com','bonas4.150@gmail.com','bona.s41.5.0@gmail.com','b.ona.s4150@gmail.com','b.on.a.s4.15.0@gmail.com','bon.a.s.4150@gmail.com','bona.s4.1.5.0@gmail.com','bo.na.s4.15.0@gmail.com','b.o.nas4.15.0@gmail.com','bon.as.41.5.0@gmail.com','bona.s.4.15.0@gmail.com','b.on.as4.150@gmail.com','bon.as.415.0@gmail.com','bon.a.s.415.0@gmail.com','bonas.4150@gmail.com','bon.as4.150@gmail.com','b.on.a.s41.50@gmail.com','bo.nas4.15.0@gmail.com','b.onas4150@gmail.com','b.onas41.50@gmail.com','bonas41.5.0@gmail.com','b.ona.s.41.5.0@gmail.com','b.o.n.a.s.4.15.0@gmail.com','b.onas.4150@gmail.com','b.on.as.4.15.0@gmail.com','b.ona.s4.1.50@gmail.com','bo.n.as41.50@gmail.com','b.o.n.as.4150@gmail.com','b.o.n.as.4.1.50@gmail.com','bon.as.4.1.5.0@gmail.com','bo.n.a.s.41.5.0@gmail.com','bo.nas.41.5.0@gmail.com','b.o.na.s.4.150@gmail.com','bo.na.s4.150@gmail.com','b.o.n.a.s.4.1.5.0@gmail.com','b.ona.s.4.150@gmail.com','b.onas41.5.0@gmail.com','b.o.n.a.s.4.1.50@gmail.com','b.o.n.as.4.150@gmail.com','bo.na.s.4.150@gmail.com','b.o.n.a.s4150@gmail.com','bo.n.a.s4.1.50@gmail.com','b.onas.41.5.0@gmail.com','b.ona.s41.5.0@gmail.com','b.on.a.s.415.0@gmail.com','bo.nas4.1.5.0@gmail.com','bo.nas4.1.50@gmail.com',
 'b.o.nas415.0@gmail.com','b.o.n.as4.1.5.0@gmail.com','b.onas.4.1.5.0@gmail.com','bo.nas.41.50@gmail.com','b.onas4.15.0@gmail.com','bo.n.a.s.4.150@gmail.com','bon.as4.1.50@gmail.com','b.ona.s4.1.5.0@gmail.com','b.ona.s415.0@gmail.com','bon.a.s.4.150@gmail.com','bo.n.as.4150@gmail.com','bona.s4.15.0@gmail.com','b.o.n.as.4.1.5.0@gmail.com','b.o.na.s.4.15.0@gmail.com','bon.a.s.4.15.0@gmail.com','bo.n.as4.1.50@gmail.com','b.o.n.a.s415.0@gmail.com','b.on.a.s4.1.50@gmail.com','b.ona.s.4.1.50@gmail.com','bo.n.as.415.0@gmail.com','bo.n.a.s4.150@gmail.com','bonas.4.150@gmail.com','bo.nas41.50@gmail.com','b.on.a.s4.1.5.0@gmail.com','bo.na.s415.0@gmail.com','b.o.na.s4.15.0@gmail.com','bo.nas.4.150@gmail.com','bo.n.a.s415.0@gmail.com','bo.na.s.415.0@gmail.com','b.o.n.a.s4.1.50@gmail.com','b.o.n.a.s41.50@gmail.com','b.ona.s4.150@gmail.com','bon.as.4.15.0@gmail.com','bo.nas4150@gmail.com','b.ona.s.4.1.5.0@gmail.com','bo.n.a.s.4.1.50@gmail.com','b.onas.4.150@gmail.com','bonas.41.50@gmail.com','bo.n.a.s.41.50@gmail.com','b.onas.415.0@gmail.com','b.on.a.s.4.1.5.0@gmail.com','b.onas.4.15.0@gmail.com','b.on.as.41.5.0@gmail.com','b.o.nas.415.0@gmail.com','bo.na.s4150@gmail.com','b.o.nas.4.150@gmail.com','bona.s.415.0@gmail.com','bon.as.4.1.50@gmail.com','b.o.nas.4.15.0@gmail.com','b.ona.s.415.0@gmail.com','b.o.nas.4.1.5.0@gmail.com','b.o.nas.41.50@gmail.com','b.o.n.as4.150@gmail.com','b.o.nas41.5.0@gmail.com','bo.n.as.4.15.0@gmail.com','bo.n.a.s4.1.5.0@gmail.com','bona.s.41.5.0@gmail.com','bona.s.4.1.50@gmail.com','bon.as.41.50@gmail.com','b.o.na.s.415.0@gmail.com','bon.a.s.4.1.5.0@gmail.com','b.o.na.s.4150@gmail.com','b.on.as41.5.0@gmail.com','bon.a.s.41.50@gmail.com','b.on.a.s41.5.0@gmail.com','bo.n.as.4.1.50@gmail.com','b.o.na.s.41.50@gmail.com','bonas.41.5.0@gmail.com','b.o.na.s41.50@gmail.com','b.o.nas4.150@gmail.com','b.o.n.a.s.415.0@gmail.com','b.on.a.s4.150@gmail.com','b.on.a.s.4150@gmail.com','b.o.n.as.415.0@gmail.com','bona.s4.1.50@gmail.com','bo.n.as41.5.0@gmail.com','bo.n.as.41.50@gmail.com','b.o.na.s4.150@gmail.com','b.o.na.s.4.1.50@gmail.com','b.on.a.s4150@gmail.com','b.onas.4.1.50@gmail.com','b.o.n.a.s.4150@gmail.com',
 'b.o.n.a.s4.15.0@gmail.com','b.onas4.150@gmail.com','b.on.as.4150@gmail.com','b.on.as.4.1.50@gmail.com','bon.a.s.4.1.50@gmail.com','b.ona.s.4.15.0@gmail.com','b.o.nas.4.1.50@gmail.com','bo.na.s41.50@gmail.com','b.o.nas41.50@gmail.com','bon.a.s4.1.5.0@gmail.com','bon.a.s41.50@gmail.com','b.o.n.as4150@gmail.com','bon.a.s4.1.50@gmail.com','bo.nas.4150@gmail.com','bon.as4150@gmail.com','bo.n.a.s4150@gmail.com','bon.as415.0@gmail.com','b.o.n.a.s.41.50@gmail.com','bo.n.as4.150@gmail.com','bo.n.as.4.1.5.0@gmail.com','bo.n.as4150@gmail.com','bon.as4.1.5.0@gmail.com','bonas.4.1.50@gmail.com','bo.na.s.4.1.5.0@gmail.com','b.on.as415.0@gmail.com','b.o.n.as.4.15.0@gmail.com','bo.na.s4.1.5.0@gmail.com','bo.n.as.41.5.0@gmail.com','bona.s41.50@gmail.com','bo.nas.4.1.50@gmail.com','b.o.n.a.s4.1.5.0@gmail.com','bonas.4.1.5.0@gmail.com','b.onas415.0@gmail.com','bo.na.s.41.5.0@gmail.com','b.ona.s41.50@gmail.com','b.on.as.41.50@gmail.com','bo.nas.4.1.5.0@gmail.com','bon.as4.15.0@gmail.com','bo.n.as4.1.5.0@gmail.com','b.on.a.s.4.150@gmail.com','b.on.a.s.41.5.0@gmail.com',"b.o.n.as41.50@gmail.com","b.o.nas.41.5.0@gmail.com"]

 total_emails=len(emails)
 print('Total emails:',total_emails)

 for xmail in emails:
  
  
  index=emails.index(xmail)
  
  email = xmail
  password = "Zayanto@2018"
 

  r = requests.Session()
  content = r.get("https://www.presearch.org").content

  soup = BeautifulSoup(content, 'html.parser')
  token = soup.find("input", {
  "name": "_token"
})["value"]

  payload = "_token={}&login_form=1&email={}&password={}".format(token, email, password)
  headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

  login = r.post("https://www.presearch.org/api/auth/login", data = payload, headers = headers)

  for x in range(1):
    words = random.choice(["apple", "life", "hacker", "facebook", "instagram", "twitter", "youtube", "money", "banana", "lemon", "rice", "chiken", "home", "street", "food", "winter", "pubg", "bot", "love", "freelancing", "presearch", "token", "abuse", "hindi", "translator", "pubg", "horse", "dollar", "india", "china", "earning", "summer", "football", "ronaldo", "messi", "cricket", "python", "java", "perl", "ruby", "free", "swift", "table", "chair", "lamp", "pen", "book", "bed", "donkey", "cow", "cat", "pencil", "class", "school", "oxford", "university", "abs", "gym", "bird", "billioner"])
    payload = "term={}&provider_id=98&_token={}".format(words, token)
    r.post("https://www.presearch.org/search", data = payload, headers = headers)
    print((i+1),(index+1),"Term:{} Search done!".format(words),xmail)
   
    time.sleep(2)
  r = r.get("https://www.presearch.org/")
  soup = BeautifulSoup(r.content, 'html.parser')
  balance = soup.find("span", {
  "class": "number ajax balance"
})
  print("                                      Your Balance: {} PRE \n\n".format(balance.text))
 
  
  #int_balance=float(balance.text)
  #total_balance.append(int_balance)
#print('TOTAL BALANCE:',sum(total_balance),'PRE')