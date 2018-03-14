import requests

def get_loc_info():
	return requests.get("https://freegeoip.net/json/").json()

if __name__ == '__main__':
	print(get_loc_info())