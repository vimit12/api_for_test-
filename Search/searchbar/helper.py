from threading import *
import time
import requests
import json,re

# api_response = []
key_list = []

def api_response_from_url(base,val,api_data):
    j = 0
    while True:
        j = j+1
        
        if re.findall(r'tatacliq',base):
            BASE_URL = base.format(j, val)
            result = requests.get(BASE_URL)
        else:
            BASE_URL = base.format(val,j)
            result = requests.get(BASE_URL)
        
        if result.status_code == 400:
            break
        
        paytm_data_dict = result.json().get('grid_layout')
              
        
        shopclues_data_dict = result.json().get('products')
        
        tatacliq_data_dict = result.json().get('searchresult')
        
        if paytm_data_dict:
            for i in paytm_data_dict:
                response = dict()
                if (i.get('name') not in key_list):
                    key_list.append(i.get('name'))
                    response[i.get('name')] = {'product_name': i.get(
                        'name'), 'product_url': i.get('url'), 'product_image': i.get('image_url'), 'product_price': i.get('offer_price')}
                else:
                    continue
                if len(api_data) <= 50:
                    api_data.append(response)
        
        if shopclues_data_dict:
            for i in shopclues_data_dict:
                response = dict()
                if (i.get('product') not in key_list):
                    key_list.append(i.get('product'))
                    response[i.get('product')] = {'product_name': i.get(
                        'product'), 'product_url': i.get('product_url'), 'product_image': i.get('image_url'), 'product_price': i.get('price')}
                else:
                    continue
                if len(api_data) <= 50:
                    api_data.append(response)
            
        if tatacliq_data_dict:
            for i in tatacliq_data_dict:
                response = dict()
                if (i.get('productname') not in key_list):
                    key_list.append(i.get('productname'))
                    response[i.get('productname')] = {'product_name': i.get(
                        'productname'), 'product_url': i.get('url'), 'product_image': i.get('imageURL'), 'product_price': i.get('mrpPrice')['value']}
                else:
                    continue
                if len(api_data) <= 50:
                    api_data.append(response)
