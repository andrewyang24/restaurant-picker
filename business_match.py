import requests
from sentimentanalysis import sentiment_analsis
# Import Yelp API key function
# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\andre\Desktop\My Comp Sci Projects\api-keys')
import YelpAPI

def business_match():
    business_id = sentiment_analsis()

    # Define my API Key, My Endpoint, and My Header
    API_KEY = YelpAPI.get_my_key()
    ENDPOINT = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)
    HEADERS = {'Authorization': 'bearer %s' % API_KEY}

    response = requests.get(url = ENDPOINT,
                            headers = HEADERS)

    business_data = response.json()


    # Print restaurant details
    details = {
        'name': '',
        'location': '',
        'url': '',
        'phone': '', 
    }
    details['name'] = business_data['name']
    #print(name)
    details['location'] = business_data['location']['display_address']
    #print(location)
    details['url'] = business_data['url']
    #print(url)
    details['phone'] = business_data['phone']
    #print(phone)
    
    return details