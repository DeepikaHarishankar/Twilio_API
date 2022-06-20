import requests
from twilio.rest import Client

account_sid = "AC2aa777562e46e6f23069b9c9bf1e87ba"
auth_token = "ca019061e60b26762dc982789548b56e"
api_key = "25d9c8ec07493327924eadc2280eaae1"
weather_data = []
take_umbrella = False
parameters = {
    'lat': 12.58,
    'lon': 77.35,
    'appid': api_key,
    'exclude': 'current,minetely,daily,alerts'
}
# parameters = {
#     'lat': 33.946213,
#     'lon': -84.334648,
#     'appid': api_key,
#     'exclude': 'current,minetely,daily,alerts'
# }
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
hourly_data = response.json()['hourly']
twelve_hours_weather = [item['weather'][0]['id'] for item in hourly_data if hourly_data.index(item) < 12]
# twelve_hours = [item for item in hourly_data if hourly_data.index(item) < 12]
# twelve_hours_weather = [item['weather'][0]['id'] for item in twelve_hours]

for item in twelve_hours_weather:
    if item < 700:
        take_umbrella = True

if take_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="He may shower His blessings 🌧 , get an ☔️ if u go out !",
        from_='+19896569815',
        to='+17622172814'
    )
    print(message.status)
    print(twelve_hours_weather)
else:
    print(twelve_hours_weather)
