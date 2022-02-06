# works with both python 2 and 3
from __future__ import print_function

import africastalking


class MOBILE:
    def __init__(self):
        # Set your app credentials
        self.username = "sandbox"
        self.api_key = "32274c0a9472cd5d07a9d60f9454d7e4b3bd4d5e448c4d7d08459211e9aab89f"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the payments service
        self.payment = africastalking.Payment

    def checkout(self):
        # Set the name of your Africa's Talking payment product
        productName = "ABC"

        # Set the phone number you want to send to in international format
        phoneNumber = "+254795388701"

        # Set The 3-Letter ISO currency code and the checkout amount
        currencyCode = "KES"
        amount = 100.50

        # Set any metadata that you would like to send along with this request.
        # This metadata will be included when we send back the final payment notification
        metadata = {"agentId": "654", "productId": "321"}

        # The provider channel the payment will be initiated from e.g a paybill number.
        provider_channel = '1122'

        # That's it hit send and we'll take care of the rest
        try:
            res = self.payment.mobile_checkout(
                productName, phoneNumber, currencyCode, amount, metadata)
            print(res)
        except Exception as e:
            print("Received error response:%s" % str(e))


if __name__ == '__main__':
    MOBILE().checkout()
