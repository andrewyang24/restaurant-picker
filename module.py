class Restaurant:
    def __init__(self, name, restid, rating, reviews, distance, location, url, phone):
        self.name = name
        self.id = restid
        self.rating = rating
        self.reviews = reviews
        self.distance = distance
        self.location = location
        self.url = url
        self.phone = phone
        self.score = 0