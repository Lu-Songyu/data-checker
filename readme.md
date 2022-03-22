# :iphone:Data-checker with Selenium and Twilio

## Intro
#### I am horrible at saving data and I alwasy run out of data before the end of the month. So I made this quick automation tool to check my data usage from ATT and send me reminders once in a while. Python and Selenium is used to access my ATT account and retrive that information, and Twilio is used to send that information to me via :calling: SMS message.

### To use
#### make a python file called `credential.py` and follow the format

```
credentials = {
    'att_userID': "To-Fill",
    'att_password': "To-Fill",
    'twilio_sid': "To-Fill",
    'twilio_token': "To-Fill",
    'mynumber': "To-Fill",
    'toNumber': "To-Fill"

}
```

Enjoy and don't use this to spam your friend:grin:





