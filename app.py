from flask import Flask, request, jsonify, redirect
import requests
from paymob import Paymob
app = Flask(__name__)


paymob_api_key = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2T0RrMU1EZ3pMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuZ3AzY2VNTko0VGd5YlVXdlZDTDJNTU10cWZaQmJMal95OGxkcFpMcHRacjBmdThuU1pWUWZsdm45WlVFbnNFT0lQaXpGT0swV3BmMnRBLTNXaGZXVXc="


@app.route('/', methods=['GET'])
def index():
    auth_response = Paymob.auth(api_key=paymob_api_key)

    auth_data = auth_response.json()
    token = auth_data.get("token")
    amount_cents = 2000000
    place_order_response = Paymob.place_order(auth_token=token, amount_cents=amount_cents, items=[{
        "name": "ASC1515",
        "amount_cents": "500000",
        "description": "Smart Watch",
        "quantity": "1"
    },]).json()
    print(place_order_response)
    order_placement = Paymob.place_payment(auth_token=token, amount_cents=amount_cents, order_id=place_order_response.get('id'), billing_data={
        "apartment": "803",
        "email": "claudette09@exa.com",
        "floor": "42",
        "first_name": "Clifford",
        "street": "Ethan Land",
        "building": "8028",
        "phone_number": "+86(8)9135210487",
        "shipping_method": "PKG",
        "postal_code": "01898",
        "city": "Jaskolskiburgh",
        "country": "CR",
        "last_name": "Nicolas",
        "state": "Utah"
    }).json()
    order_token = order_placement.get('token')
    if order_token:
        return redirect(f"https://accept.paymob.com/api/acceptance/iframes/786277?payment_token={order_token}")
    else:
        return "Couldn't complete your order successfully :'("

if __name__ == '__main__':
    app.run()
