# agentic-web-scraper/src/data_models.py
from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    """
    Data model for a scraped product.
    Using dataclasses for clean and explicit data representation.
    """
    name: str
    price: str
    description: str = None
    url: str = None
    image_url: str = None
    # Add more fields as needed based on your config and target site

    def to_dict(self):
        """Converts the Product dataclass instance to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        """Creates a Product instance from a dictionary."""
        return cls(**data)

# You can add other data models here if your agent scrapes different types of entities
# For example, @dataclass class Article: ...
