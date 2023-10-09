import http.client
import random
import requests
from hisay import settings


def send_sms_code(data, code):
    sms_conn = http.client.HTTPSConnection(settings.SMS_BASE_URL)
    payload1 = "{\"messages\":" \
               "[{\"from\":\"" + settings.SMS_SENDER + "\"" \
                                                       ",\"destinations\":" \
                                                       "[{\"to\":\"" + data['phone_number'].replace('+', '') + "\"}]," \
                                                                                                               "\"text\":\"" + \
               str(code) + "\"}]}"
    print(settings.SMS_API_KEY)
    headers = {
        'Authorization': settings.SMS_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # url = 'https://' + settings.SMS_BASE_URL + "/sms/2/text/advanced"
    sms_conn.request("POST", "/sms/2/text/advanced", payload1, headers)

    # requests.post(url, data=payload1, headers=headers)
    res = sms_conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def generate_code():
    return ''.join(random.sample([f"{i}" for i in range(10)], 6))


"""
phone_number
fullname
is_service
"""

"""
verification_code
"""

"""
{
"phone_number": "+998973445350",
"fullname": "",
"is_service": true
}
"""
