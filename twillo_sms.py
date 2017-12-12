from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3f0931dee2fb0698409a1185a150fe86"
# Your Auth Token from twilio.com/console
auth_token  = "369e82850dd35b2f5c577ae2c57d95bc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19512839806", 
    from_="+15622739442",
    body="Hello from Python!")

print(message.sid)
