from twilio.rest import Client
import sys

account_sid = 'AC243b6bf72a5f72f513194f2ebd6b498a'
auth_token = '256fbe6649f4f920bfbc9a2c42a11948'

client = Client(account_sid, auth_token)

twilio_number = '+18334751562'

if len(sys.argv) < 3:
    print("Usage: python3 script.py <recipient> <message>")
    sys.exit(1)

target_number = sys.argv[1]
message_body = ' '.join(sys.argv[2:])

message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to=target_number
)

print("Message SID:", message.sid)
print("Message Body:", message.body)
