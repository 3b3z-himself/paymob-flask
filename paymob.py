import requests
from random import randint

class Paymob():
    def __init__(self):
        pass

    def auth(api_key):
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "api_key": api_key
        }
        auth_key = requests.post(
            "https://accept.paymob.com/api/auth/tokens", json=data, headers=headers)
        return auth_key

    def place_order(auth_token:str, delivery_needed:bool=False, amount_cents:int=0, currency:str="EGP", merchant_order_id:str=f"{randint(10,9999)}", items:list=[]):

        data = {
            "auth_token": auth_token,
            "delivery_needed": str(delivery_needed).lower(),
            "amount_cents": str(amount_cents),
            "currency": currency,
            "merchant_order_id": str(merchant_order_id),
            "items": items
        }
        order_placement = requests.post(
            "https://accept.paymob.com/api/ecommerce/orders", json=data, headers={"Content-Type": "application/json",})
        
        return order_placement
    
    def place_payment(auth_token:str, amount_cents:int=0, expiration:int=3600, order_id:int=0, billing_data:dict={}, currency:str="EGP", integration_id:int=4184129):
        data = {
            "auth_token": auth_token,
            "amount_cents": str(amount_cents),
            "expiration": expiration,
            "order_id": str(order_id),
            "billing_data": billing_data,
            "currency": currency,
            "integration_id": integration_id
        }
        order_placement = requests.post(
            "https://accept.paymob.com/api/acceptance/payment_keys", json=data, headers={"Content-Type": "application/json",})
        
        return order_placement