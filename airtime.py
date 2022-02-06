import africastalking

username = "sandbox"
api_key = "32274c0a9472cd5d07a9d60f9454d7e4b3bd4d5e448c4d7d08459211e9aab89f"

africastalking.initialize(username, api_key)

airtime = africastalking.Airtime

phone_number = "+254795388701"
currency_code = "KES"  # Change this to your country's code
amount = 900

try:
    response = airtime.send(phone_number=phone_number,
                            amount=amount, currency_code=currency_code)
    print(response)
except Exception as e:
    print(
        f"Encountered an error while sending airtime. More error details below\n {e}")
