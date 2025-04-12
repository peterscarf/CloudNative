from model.models import Listing
from database.jsonDAO import Database
from managers.categoryManager import CategoryManager

class ListingManager:
    def __init__(self, db: Database):
        self.db = db
        self.data = self.db.load()
        self.category_manager = CategoryManager(db)
    
    def create_listing(self, username, title, description, price, category):
        self.data = self.db.load()
        if username.lower() not in self.data["users"]:
            return "Error - unknown user"
        listing_id = self.data["parameters"]["next_listing_id"]
        listing = Listing(username, title, description, price, category, listing_id)
        self.data["listings"][listing_id] = listing.__dict__
        self.data["parameters"]["next_listing_id"] += 1
        self.db.save(self.data)

        self.category_manager.add_category(category, listing_id, username.lower())
        return listing_id
    
    def delete_listing(self, username, listing_id):
        self.data = self.db.load()
        if listing_id not in self.data["listings"]:
            return "Error - listing does not exist"
        listing = self.data["listings"][listing_id]
        if listing["username"] != username.lower():
            return "Error - listing owner mismatch"
        c = self.data["listings"][listing_id]["category"]
        self.category_manager.delete_category(c, listing_id, username.lower())
        self.data = self.db.load()
        del self.data["listings"][listing_id]
        self.db.save(self.data)

        return "Success"

    def get_listing(self, username, listing_id):
        self.data = self.db.load()
        if username.lower() not in self.data["users"]:
            return "Error - unknown user"
        if listing_id not in self.data["listings"]:
            return "Error - not found"
        listing = self.data["listings"][listing_id]
        return f"{listing['title']}|{listing['description']}|{listing['price']}|{listing['created_at']}|{listing['category']}|{listing['username']}"

    def get_category(self, username, category):
        self.data = self.db.load()
        u = username.lower()
        if u not in self.data["users"]:
            return "Error - unknown user"
        listings = [l for l in self.data["listings"].values() if l["category"] == category]
        if not listings:
            return "Error - category not found"
        sorted_listings = sorted(listings, key=lambda l: l["created_at"], reverse=True)
        return "\n".join(
            f"{l['title']}|{l['description']}|{l['price']}|{l['created_at']}|{l['category']}|{l['username']}" for l in sorted_listings
        )
        