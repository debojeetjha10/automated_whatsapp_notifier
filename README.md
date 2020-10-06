___
# automated_whatsapp_notifier
<img src = "img/python.jpeg"
height = "100px"
weidth = "100px"
alt = "python logo"
title = "python">
<img src = "img/whatsapp.jpeg"
height = 100px
weidth = 100px
alt = "whatsapp logo"
title = "whatsapp">
<img src = "img/twilio.png"
height = 100px
weidth = 100px
alt = "twilio logo"
title = "twilio">
___
## How It Works
This python script fetches data from the pickled files of data and send notification in your whasapp at the time of online class using the [twilio api](https://www.twilio.com/).
## Technologies used
1.Restful api

2.python3

3.pickling methode of python

4.SDK of twilio

___
## some key points to know.
1. To use this script you will need the auth_token and account_sid of [twilio](https://www.twilio.com/), login into your account and puth them in the [.env](.env) file.
2. Update the numbers pickle file with [update.py](update.py)

*to know how to update the data goto [how_to_update.md](class_list/how_to_update_data.md)*
___
## How to run the script
<b>you system need to have the following this installed</b>

  1.[python3](https://www.python.org/)
  
  2.[twilio sdk](https://pypi.org/project/twilio/) for python3
  
  3.[dotenv module](https://pypi.org/project/dotenv/) of python3
  
   [click here to see other requirements]("requirement.txt")
  ___
  
  <h4> To run the script enter the following commands in the terminal </h4>
  
  ```bash
  git clone https://github.com/debojeetjha10/automated_whatsapp_notifier.git
  
  cd automated_whatsapp_notifier 
  
  python3 main.py
  ```
  ___
<p align = "middle" > <a href = "mailto:debojeetjha@gmail.com">email me</p>
