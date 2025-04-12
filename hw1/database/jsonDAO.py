from pathlib import Path
import json

class Database:
    def __init__(self, filename="database"):
        database_path = Path("data") / f"{filename}.json"
        database_path.parent.mkdir(parents=True, exist_ok=True)
        self.file = database_path

        if not self.file.exists():
            with self.file.open("w") as f:
                json.dump({"users": {}, "listings": {}, "categories": {}, "parameters":{"next_listing_id":100001}}, f)
    
    def load(self):
        with self.file.open("r") as f:
            return json.load(f)
    
    def save(self, data):
        with self.file.open("w") as f:
            json.dump(data, f)