from django.shortcuts import render
import re
from .helper import *
import requests
import json
import itertools
from .models import ProductDetail
from .serializers import api_data_serialize
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

def search_bar(request):
    kwargs = dict()
    data_list = None
    product_obj = None
    if request.method == 'POST':
        from searchbar.helper import api_response_from_url
        search_value = request.POST.get('search').strip()
        data_save_to_db = []
        api_data = []
        
        paytm_url = "https://search.paytm.com/v2/search?userQuery={}&page_count={}&items_per_page=30"
        
        shopclues_url = "http://api.shopclues.com/api/v11/search?q={}&z=1&key=d12121c70dda5edfgd1df6633fdb36c0&page={}"
        
        tatacliq_url = "https://www.tatacliq.com/marketplacewebservices/v2/mpl/products/serpsearch?type=category&channel=mobile&pageSize=20&typeID=al&page={}&searchText={}&isFilter=false&isTextSearch=true"
        
        if len(search_value) == 0:
            messages.warning(
                request, f'Please Enter Keyword')
            return HttpResponseRedirect(request.path_info)
        
        request.session['search_value'] = search_value

        t1 = Thread(target=api_response_from_url, args=(paytm_url, search_value, api_data))
        t2 = Thread(target=api_response_from_url, args=(shopclues_url, search_value, api_data))
        t3 = Thread(target=api_response_from_url, args=(tatacliq_url, search_value, api_data))
        t1.start()
        t2.start()
        t3.start()
        # time.sleep(2)
        
        while True:
            time.sleep(1)
            if len(api_data) > 50:
                # data_save_to_db = api_response[-50:]
                data_save_to_db = api_data[-50:]
                break
          
        
        # print("@@@@@@", len(data_save_to_db))
        for data in data_save_to_db:
            for data_val in data.values():
                if (data_val.get('product_name')):
                    data_val['name'] = search_value
                    try:
                        obj = ProductDetail(**data_val)
                        obj.save()
                    except Exception as e:
                        pass
        
        try:
            product_obj = ProductDetail.objects.all().filter(name=search_value).order_by(
                '-created_at')[::1][:(len(data_save_to_db)-1)]
        except Exception as e:
            product_obj = None
        
        return render(request, 'searchbar/search.html', {'product_obj': product_obj})
    
    
    return render(request,'searchbar/search.html')


def product_detail_api(request):
    search_kwd = request.GET.get('query_param')
    try:
        prod_api = ProductDetail.objects.all().filter(
            name=search_kwd)[::1]
    except Exception as e:
        prod_api = None
    
    if prod_api:
        return_api_json_data = api_data_serialize(prod_api)
        return HttpResponse(return_api_json_data, content_type='application/json')
    else:
        return_api_json_data = {'error': 'No record Found'}
        return JsonResponse(return_api_json_data)

def product_detail_api_full(request):
    try:
        prod_api = ProductDetail.objects.all()[::1]
    except Exception as e:
        print(e)
        prod_api = None

    if prod_api:
        return_api_json_data = api_data_serialize(prod_api)
        return HttpResponse(return_api_json_data, content_type='application/json')
    else:
        return_api_json_data = {'error':'No record Found'}
        return JsonResponse(return_api_json_data)
