import requests 
import twilio
from twilio.rest import Client

End_point = "Your End Point"
latitude = "Your Latitude"
longitude = "Your Longitude"
API_key = "Your Api_Key"
account_sid = "Your Account_Sid"
auth_token = "Your Auth_Token"
parameter = {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : API_key,
    "exclude" : "current,minutely,daily"
}
response = requests.get(url= End_point ,params= parameter)
data = response.json()
response.raise_for_status()
print(response)
rain = False
for i in range(0 , 12):
    wheather_id = data["hourly"][i]["weather"][0]["id"]
    if wheather_id < 700:
       rain = True
if rain:
    
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                body="It's going to be rain,Please take your Umbrella" ,
                from_='+14058967291',
                to='Your Phone Number'
    )
    print(message.status)

else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                body="No Rain today,You can go without Umbrella" ,
                from_='+14058967291',
                to='Your Phone Number'
    )
    print(message.status)
    
    
    
    