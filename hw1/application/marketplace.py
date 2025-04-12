from managers.userManager import UserManager
from managers.listingManager import ListingManager
from managers.categoryManager import CategoryManager
from database.jsonDAO import Database 

class Marketplace:
    def __init__(self, db: Database):
        self.db = db
        self.user_manager = UserManager(db)
        self.listing_manager = ListingManager(db)
        self.category_manager = CategoryManager(db)

    def register_user(self, username):
        return self.user_manager.register_user(username)
    def create_listing(self, username, title, description, price, category):
        return self.listing_manager.create_listing(username, title, description, price, category)
    def delete_listing(self, username, listing_id):
        return self.listing_manager.delete_listing(username, listing_id)
    def get_listing(self, username, listing_id):
        return self.listing_manager.get_listing(username, listing_id)
    def get_category(self, username, category):
        return self.listing_manager.get_category(username, category)
    def get_top_category(self, username):
        return self.category_manager.get_top_category(username)