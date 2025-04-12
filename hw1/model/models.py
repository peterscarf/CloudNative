from datetime import datetime, timezone

class User:
    def __init__(self, username):
        self.username = username.lower()

class Listing:
    def __init__(self, username, title, description, price, category, listing_id):
        self.listing_id = listing_id
        self.title = title
        self.description = description
        self.price = price
        self.username = username.lower()
        self.category = category
        self.created_at = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

class Category:
    def __init__(self, name, listing_id):
        self.name = name
        self.listing_num = 1
        self.listing_ids = [listing_id]