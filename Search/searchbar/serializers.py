from searchbar.models import ProductDetail
from rest_framework import serializers

from json import dumps, loads, JSONEncoder, JSONDecoder



def api_data_serialize(data):
    api_dict = dict()
    if data:
        for current_obj in data:
            api_dict[f'product_{current_obj.id}'] = {'product_name': current_obj.product_name, 'product_url': current_obj.product_url, 'product_image': current_obj.product_image, 'product_price': current_obj.product_price}
    
    return dumps(api_dict)

    

