from datetime import datetime   
try:
    from playsound import playsound # type: ignore
except ModuleNotFoundError:
    print("The playsound module is not installed. Please install it using 'pip install playsound'.")
    exit()
import re

def validate_time_format(time_str):
    return re.match(r'^\d{2}:\d{2}:\d{2} (AM|PM)$', time_str) is not None

alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")
while not validate_time_format(alarm_time):
    print("Invalid time format. Please try again.")
    alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    try:
                        playsound('audio.mp3')
                    except Exception as e:
                        print(f"Error playing sound: {e}")
                    break