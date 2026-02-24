import requests

API_URL = "http://ip-api.com/json/{}"

def lookup_ip(ip):
    """Fetch geolocation data for an IP address."""
    url = API_URL.format(ip)
    response = requests.get(url)
    return response.json()

def display_info(data):
    """Print geolocation info in a readable format."""
    if "error" in data:
        print("❌ Invalid IP address or lookup failed.")
        return

    print("\n🌍 IP Geolocation Results")
    print(f"IP:        {data.get('ip')}")
    print(f"Country:   {data.get('country_name')}")
    print(f"Region:    {data.get('region')}")
    print(f"City:      {data.get('city')}")
    print(f"Latitude:  {data.get('latitude')}")
    print(f"Longitude: {data.get('longitude')}")
    print(f"Timezone:  {data.get('timezone')}")
    print(f"ISP:       {data.get('org')}")

def main():
    print("=== IP Geolocation Lookup Tool ===")
    ip = input("Enter an IP address: ")
    data = lookup_ip(ip)
    display_info(data)

if __name__ == "__main__":
    main()
