class Restaurant:
    def __init__(self, name, restid, rating, reviews, distance, location, url, phone, image):
        self.name = name
        self.id = restid
        self.rating = rating
        self.reviews = reviews
        self.distance = distance
        self.location = location
        self.url = url
        self.phone = phone
        self.image = image
        self.score = 0