import requests

url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?'

# start_time = input('Enter the start date: ')
# end_time = input('Enter the end time: ')
# min_magnitude = input('Magnitude: ')
# latitude = input('Enter the latitude of the center point of the circle: ')
# longitude = input('Enter the longitude of the center point of the circle: ')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    "format": "geojson",
    'starttime': "04/01/2022",
    'endtime': "05/01/2022",
    'minmagnitude': "2.5",
    "longitude": "-118.2437",
    "latitude": "34.0522",
    "maxradiuskm": "100"
})

data = response.json()

earthquake_list = data['features']
count = 0
for earthquake in earthquake_list:
    count = +1
    print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}\r\n\n")
