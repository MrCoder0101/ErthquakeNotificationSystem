import requests
import os
from twilio.rest import Client
ertquake_endpoint = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
response = requests.get(url=ertquake_endpoint)
response.raise_for_status()
result=response.json()
print("{:<24} {:<39} {:<12} {:<12}".format("Date","location","mag","depth"))
for eartquake in result["result"]:
    if eartquake["mag"] > 4:
        """print("{:<24} {:<39} {:<12} {:<12}".format(eartquake["date"], eartquake["title"],
                                                   eartquake["mag"], eartquake["depth"]))"""
        twilioclent=Client(os.environ["account_sid"],os.environ["auth_token"])
        twilioclent.messages.create(to=os.environ["phone_number"], from_=os.environ["twilio_number"],
                                    body=f"Subject:Earthquake\n\n{eartquake['date']}\n\n{eartquake['title']}\n\n{eartquake['mag']}\n\neartquake['depth']")
