import requests
import pandas as pd
import geocoder
import module

# Import Yelp API key function
# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\andre\Desktop\My Comp Sci Projects\api-keys')
import YelpAPI



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

def queryToObjects(query):
    results = {'Name': [], 'ID':[], 'Rating': [], 'Pricing': [], 'Reviews': [], 'Distance': [], "Url": [], "Location": [], "Phone": []}
    restaurants = []
    for n, q in enumerate(query):
        temp = module.Restaurant(q['name'],q['id'],q['rating'],q['review_count'], q['distance'], q['location']['display_address'], q['url'], q['phone'])
        score = 0
        score += q['rating'] * 5
        score += q['review_count'] *.02
        try:
            if q['price'] == "$":
                score +=3
            elif q['price'] == "$$":
                score +=2
            elif q['price'] == "$$$":
                score +=1
            else:
                score +=0.5
        except:
            pass
        score -= q['distance'] * .0005
        temp.score = score
        restaurants.append(temp)

    return restaurants

df = queryToObjects(response.json()['businesses'])
print(df[0].name)
print(df[2].name)
print(df[0].score)
print(df[2].score)
def get_score(restaurant):
    return restaurant.score
sorteddf = sorted(df, key=get_score, reverse=True)
print(sorteddf[0].name)
print(sorteddf[2].name)
print(sorteddf[0].score)
print(sorteddf[2].score)