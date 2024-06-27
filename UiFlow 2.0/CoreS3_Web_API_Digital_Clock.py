import os
import sys
import io
import M5
from M5 import *
import requests

label_time = None
label_date = None
label_day = None
wlan = None

def setup():
    global label_time, label_date, label_day, wlan

    M5.begin()
    Widgets.fillScreen(0x222222)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('Capgemini_4G', 'MN704116')

    label_time = Widgets.Label("Time: --:--:--", 20, 20, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu24)
    label_date = Widgets.Label("Date: YYYY-MM-DD", 20, 60, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu24)
    label_day = Widgets.Label("Day: -----", 20, 100, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu24)

def fetch_time_data():
    try:
        response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
        if response.status_code == 200:
            data = response.json()
            datetime_str = data['datetime']
            date_str = datetime_str.split('T')[0]
            time_str = datetime_str.split('T')[1].split('.')[0]
            day_str = data['day_of_week']
            return time_str, date_str, day_str
        else:
            return None, None, None
    except Exception as e:
        print("Error fetching time data:", e)
        return None, None, None

def get_day_name(day_index):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[day_index]

def loop():
    global label_time, label_date, label_day
    M5.update()

    time_str, date_str, day_index = fetch_time_data()
    if time_str and date_str and day_index is not None:
        day_name = get_day_name(day_index - 1)
        label_time.setText(f"Time: {time_str}")
        label_date.setText(f"Date: {date_str}")
        label_day.setText(f"Day: {day_name}")

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")
