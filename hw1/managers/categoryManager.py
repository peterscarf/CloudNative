from model.models import Category
from database.jsonDAO import Database 

class CategoryManager:
    def __init__(self, db):
        self.db = db
        self.data = self.db.load()
    
    def add_category(self, category_name, listing_id, username):
        self.data = self.db.load()
        if category_name in self.data["categories"]:
            self.data["categories"][category_name]["listing_num"] += 1
            self.data["categories"][category_name]["listing_ids"].append(listing_id)
        else:
            category = Category(category_name, listing_id)
            self.data["categories"][category_name] = category.__dict__
        self.db.save(self.data)

    def delete_category(self, category_name, listing_id, username):
        self.data = self.db.load()
        if category_name in self.data["categories"]:
            self.data["categories"][category_name]["listing_num"] -= 1
            self.data["categories"][category_name]["listing_ids"].remove(int(listing_id))
        self.db.save(self.data)

    def get_top_category(self, username):
        self.data = self.db.load()
        if username.lower() not in self.data["users"]:
            return "Error - unknown user"
        categorys = [c for c in self.data["categories"].values()]
        max_listing_num = max(c["listing_num"] for c in categorys)
        top_categories = [c for c in categorys if c["listing_num"] == max_listing_num]
        sorted_categorys = sorted(top_categories, key=lambda c: c["name"])

        return "\n".join(
            f"{category['name']}" for category in sorted_categorys
        )