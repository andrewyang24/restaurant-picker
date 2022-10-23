import requests
import pandas as pd
import geocoder

# Import Yelp API key function
# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\andre\Desktop\My Comp Sci Projects\api-keys')
import YelpAPI

def business_search():

    url = 'https://api.yelp.com/v3/businesses/search'
    key = YelpAPI.get_my_key()
    headers = {'Authorization': 'bearer %s' % key}

    g = geocoder.ip('me')
    lat = g.lat
    lng = g.lng

    parameters = {'term': 'Food',
                'limit': 50,
                'latitude': lat,
                'longitude': lng,
                'open_now': True}

    response = requests.get(url, headers=headers, params=parameters)

    def queryToDf(query):
        results = {'Name': [], 'ID':[], 'Rating': [], 'Pricing': [], 'Reviews': [], 'Distance': []}
        for q in query:
            results['Name'].append(q['name'])
            results['ID'].append(q['id'])
            results['Rating'].append(q['rating'])
            try:
                results['Pricing'].append(q['price'])
            except:
                results['Pricing'].append(None)
            results['Reviews'].append(q['review_count'])
            results['Distance'].append(q['distance'])

        return pd.DataFrame(results)

    df = queryToDf(response.json()['businesses'])
    df.to_csv(r'C:\Users\andre\Desktop\My Comp Sci Projects\yelp-app\test.csv')