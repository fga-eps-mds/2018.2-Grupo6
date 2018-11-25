from django.conf import settings
import requests

def create_product(name = None, fk_vendor = None, price = None, photo = None, description = None, token = None):

    data = {
        'fk_vendor': fk_vendor,
        'name': name,
        'price': price,
        # 'photo': photo,   # Removed because of Cloudinary, API will add a default.
        'description': description,
        'token': token
    }

    return data