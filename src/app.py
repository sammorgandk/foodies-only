from flask import Flask
import requests
import csv
import math


app = Flask(__name__)


def getLatLong(address):

    # TODO: Remove API key
    api_key = 'AIzaSyCS-tQJH7xwxuleC376r_TlZmAhk1pngVc'
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    url =  f'{base_url}address={address}&key={api_key}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the status is "OK"
            if data['status'] == 'OK':
                # Extract the latitude and longitude
                location = data['results'][0]['geometry']['location']
                usr_latitude = location['lat']
                usr_longitude = location['lng']
                print(f'Your latitude: {usr_latitude}')
                print(f'Your longitude: {usr_longitude}')
                return usr_latitude, usr_longitude
            else:
                print(f'Geocoding API returned status: {data["status"]}')
        else:
            print(f'Request failed with status code: {response.status_code}')
    except Exception as e:
        print(f'Error: {e}')


def haversineDistance(usr_latitude, usr_longitude, truck_lat, truck_long):

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    usr_latitude = math.radians(usr_latitude)
    usr_longitude = math.radians(usr_longitude)
    truck_lat = math.radians(truck_lat)
    truck_long = math.radians(truck_long)

    # Subtract latitudes and longitudes
    diff_lat = truck_lat - usr_latitude
    diff_long = truck_long - usr_longitude

    # Haversine formula which calculates distances between two points on the surface of a sphere
    a = math.sin(diff_lat/2)**2 + math.cos(usr_latitude) * math.cos(truck_lat) * math.sin(diff_long/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance (radius of the earth times result of Haversine formula)
    distance = R * c

    return distance


@app.route('/')
def hello():
    return 'Welcome to the exclusive Foodies Only web service! Type an address at route address/ to find the closest SF food truck to you. Example: address/397 Arguello Blvd, San Francisco, CA 94118'


@app.route('/address/<address>')
def findFoodTruck(address):
    usr_latitude, usr_longitude = getLatLong(address)

    if usr_latitude and usr_longitude:
        closest_truck = None
        closest_distance = float('inf')

        with open('Mobile_Food_Facility_Permit.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                truck_lat = float(row['Latitude'])
                truck_long = float(row['Longitude'])
                distance = haversineDistance(usr_latitude, usr_longitude, truck_lat, truck_long)
                
                if distance < closest_distance:
                    closest_truck = row
                    closest_distance = distance

        return f"Closest food truck is: {closest_truck['Applicant']}, which is {closest_distance} km away."
    else:
        return "Error: Unable to retrieve coordinates for the provided address."
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
