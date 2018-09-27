from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
import requests
import json

host_ip = 'http://192.168.0.10'
login_microservice_port = ':8000'
order_microservice_port = ':8001'
product_microservice_port = ':8002'

# Create your views here.
@api_view(["POST"])
def delete_product(request):
    try:
        response = Response(requests.post(host_ip + product_microservice_port + '/api/delete_product', data= request.data))
        return response
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_order(request):
    try:
        response = Response(requests.post(host_ip + order_microservice_port + '/api/create_order', data=request.data))
        return response
    except:
        return Response({'error': 'Nao foi possivel se comunicar com o servidor'},
                                status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def orders_screen(request):
    user_id = request.data.get('user_id')
    user_products = requests.post(host_ip + product_microservice_port + '/api/user_products', data={'user_id':user_id})
    #Convert to JSon
    user_products_response = Response(data=json.loads(user_products.content))

    #List to store all user orders
    all_user_orders = []

    for product in user_products_response.data:
        product_orders = requests.post(host_ip + order_microservice_port + '/api/user_orders', data={'product_id':product['id']})
        orders = json.loads(product_orders.content)
        for order in orders:
            if(order['closed'] == False):
                all_user_orders.append(order)

    response = Response(data=all_user_orders)
    return response