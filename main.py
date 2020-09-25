from twilio.rest import Client
import time
import os
from dotenv import load_dotenv
load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
my_number = os.getenv('my_phone_number')
from time import sleep
import pickle
client = Client(account_sid, auth_token)
day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
number_file = open('numbers','rb')
numbers = pickle.load(number_file)
number_file.close()
while True:
    TIME = time.localtime()
    day = day_list[TIME.tm_wday]
    if TIME.tm_wday<5:
        classfile = open('class_list/'+day,'rb')
        classlist = pickle.load(classfile)
        classfile.close()
        total_class = len(classlist)
        for i in range(total_class):
            if classlist[i]['start_hour'] == time.localtime().tm_hour and classlist[i]['start_mint'] == time.localtime().tm_min:
                message_body = f"you have a {classlist[i]['type']} class starting from {classlist[i]['start_hour']}:{classlist[i]['start_mint']} .The class info is : {classlist[i]['class_info']}"
                for number in numbers:
                    message = client.messages.create(
                       from_=f"whatsapp:{my_number}",
                      body=message_body,
                      to=f"whatsapp:{number}")
                TIME = time.localtime()
                if i == total_class -1:
                    sleep((classlist[min(i+1,total_class-1)]['start_hour'] - classlist[i]['start_hour']-1)*3600+(classlist[min(i+1,total_class-1)]['start_mint'] - classlist[i]['start_mint']+60)*60)
                else:
                    if TIME.tm_wday == 2 or TIME.tm_wday ==3:
                        sleep(((24 - classlist[total_class-1]['start_hour']-1)*3600)+(60-classlist[total_class-1]['start_mint'])*60 + 10*3600 + 1)
                    else:
                        sleep(((24 - classlist[total_class-1]['start_hour']-1)*3600)+(60-classlist[total_class-1]['start_mint'])*60 + 9*3600 +1)
    else:
        if TIME.tm_wday == 5:
            TIME = time.localtime()
            sleep((23 - TIME.tm_hour)*3600 + (60-TIME.tm_min)*60 + 33*3600)
        else:
            sleep((23 - TIME.tm_hour)*3600 + (60-TIME.tm_min)*60 + 9*3600)