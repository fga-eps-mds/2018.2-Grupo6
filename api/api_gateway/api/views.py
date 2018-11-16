from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.conf import settings
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR
)
import requests
from .login_views import verify_token
from .response_helper import default_response

@api_view(["POST"])
def get_name(request):
    return default_response(settings.LOGIN + '/api/users/get_name/', request)

@api_view(["POST"])
def orders_screen(request):
    verify = verify_token(request.data)
    if verify.status_code != 200:
        return verify

    user_products = get_user_products(request.data)
    #Convert to JSon
    if user_products.status_code != 200:
        return Response(data=user_products.json(), status=user_products.status_code)
    #List to store all user orders
    all_user_orders = get_user_orders(user_products.json())
    if all_user_orders == 500:
        return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                            status=HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data=all_user_orders, status=HTTP_200_OK)

def get_user_products(data):
    try:
        user_products = requests.post(settings.PRODUCTS + '/api/user_products/', data=data)
        return user_products
    except:
        return 500

def get_user_orders(user_products):
    all_user_orders = []
    for product in user_products:
        try:
            product_orders = requests.post(settings.ORDER + '/api/user_orders/', data={'product_id':product['id']})
        except:
            return Response({'error': 'Não foi possível se comunicar com o servidor.'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)
        orders = product_orders.json()
        all_user_orders += get_product_orders(orders)
    return all_user_orders

def get_product_orders(orders):
    ORDER_CLOSED = 1
    all_user_orders = []
    for order in orders:
        if(order['status'] != ORDER_CLOSED):
            all_user_orders.append(order)
    return all_user_orders