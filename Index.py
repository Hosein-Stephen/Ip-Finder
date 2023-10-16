import requests

def get_location(ip):
    
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    location = {
        "IP": data.get("ip"),
        "City": data.get("city"),
        "Region": data.get("region"),
        "Country": data.get("country_name"),
        "Latitude": data.get("latitude"),
        "Longitude": data.get("longitude"),
        "network": data.get("network"),
        "time": data.get("timezone"),
        "Phone Contry Code": data.get("country_calling_code"),
        "country_tld":data.get("country_tld"),
        "Platform":data.get("org")
    }
    return location

ip_address = '0.0.0.0'
location = get_location(ip_address)

for key, value in location.items():
    print(f"{key}: {value}")
