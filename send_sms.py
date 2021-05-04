from twilio.rest import Client
import os

client = Client(os.environ['twilio_sid'], os.environ['twilio_auth_token'])

client.messages.create(to=os.environ['phone_num'],
                       from_="+13344543608",
                       body="test env")