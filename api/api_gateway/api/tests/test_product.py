from django.test import TestCase
from .product_test_helper import create_product
from .login_test_helper import registrate_new_user, login_user
import json

default_name = "test1234"
default_fk_vendor = 1
default_price = '10.0'
default_photo = 'www.google.com'
default_description = 'description'

# Create your tests here.
class ProductTest(TestCase):
    def test_product_creation_with_valid_params(self):
        email = 'teste123@teste.com'
        
        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        login_token = loginResponseJson["token"]
        fk_vendor = loginResponseJson["user"]["pk"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response = self.client.post('/api/create_product/', data=data)

        self.assertEqual(response.status_code, 200)

    def test_product_creation_with_invalid_params(self):
        email = 'teste124@teste.com'

        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        fk_vendor = loginResponseJson["user"]["pk"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description)
        response = self.client.post('/api/create_product/', data=data)

        self.assertEqual(response.status_code, 403)

    def test_all_products_with_valid_params(self):
        # product from user 1
        email = 'teste125@teste.com'
        
        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        fk_vendor = loginResponseJson["user"]["pk"]
        login_token = loginResponseJson["token"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response = self.client.post('/api/create_product/', data=data)

        # product from user 2
        email2 = 'teste126@teste.com'
        
        responseJson2 = registrate_new_user(email2)
        loginResponseJson2 = login_user(email2)

        fk_vendor2 = loginResponseJson2["user"]["pk"]
        login_token2 = loginResponseJson2["token"]

        data2 = create_product(default_name, fk_vendor2, default_price, default_photo, default_description, login_token2)
        response2 = self.client.post('/api/create_product/', data=data2)

        # retriving all products
        data3 = {'token': login_token}
        response3 = self.client.post('/api/all_products/', data=data3)

        # checking pertinent data
        self.assertEqual(response3.data[0]["fk_vendor"], data["fk_vendor"])
        self.assertEqual(response3.data[1]["fk_vendor"], data2["fk_vendor"])
        self.assertEqual(response3.status_code, 200)

    def test_all_products_with_invalid_params(self):
        response = self.client.post('/api/all_products/', data = {'token': None})

        self.assertEqual(response.status_code, 403)

    def test_my_products_screen_with_valid_params(self):
        # product from user 1
        email = 'teste127@teste.com'
        
        responseJson = registrate_new_user(email)
        loginResponseJson = login_user(email)

        fk_vendor = loginResponseJson["user"]["pk"]
        login_token = loginResponseJson["token"]

        data = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response = self.client.post('/api/create_product/', data=data)

        data2 = create_product(default_name, fk_vendor, default_price, default_photo, default_description, login_token)
        response2 = self.client.post('/api/create_product/', data=data2)

        # retriving all products
        data3 = {'user_id': fk_vendor,'token': login_token}
        response3 = self.client.post('/api/my_products_screen/', data=data3)

        self.assertEqual(response3.data[0]["fk_vendor"], fk_vendor)
        self.assertEqual(response3.data[1]["fk_vendor"], fk_vendor)
        self.assertEqual(response3.status_code, 200)

    def test_my_products_screen_with_invalid_params(self):
        data = {'user_id': default_fk_vendor, 'token': None}
        response = self.client.post('/api/my_products_screen/', data=data)

        self.assertEqual(response.status_code, 403)