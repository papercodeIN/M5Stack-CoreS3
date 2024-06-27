import os, sys, io
import M5
from M5 import *
from hardware import RTC

Hour = None
Seconds = None
COL_1 = None
Minute = None
COL_2 = None
SEP_1 = None
DD = None
MM = None
YYYY = None
SEP_3 = None
SEP_4 = None
SEP_2 = None
rtc = None
# label10 = None  # New label for day of the week

def setup():
    global Hour, Seconds, COL_1, Minute, COL_2, SEP_1, DD, MM, YYYY, SEP_3, SEP_4, SEP_2, rtc #, label0

    M5.begin()
    M5.Widgets.fillScreen(0x222222)
    
    # Labels for time display
    Hour = M5.Widgets.Label("00", 17, 9, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu56)
    Seconds = M5.Widgets.Label("00", 226, 9, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu56)
    COL_1 = M5.Widgets.Label(":", 93, 9, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu56)
    Minute = M5.Widgets.Label("00", 121, 9, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu56)
    COL_2 = M5.Widgets.Label(":", 198, 9, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu56)
    
    # Line separators
    SEP_1 = M5.Widgets.Line(22, 83, 300, 83, 0xffffff)
    SEP_2 = M5.Widgets.Line(22, 147, 300, 147, 0xffffff)
    
    # Labels for date display
    DD = M5.Widgets.Label("DD", 74, 103, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)
    MM = M5.Widgets.Label("MM", 129, 103, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)
    YYYY = M5.Widgets.Label("YYYY", 188, 103, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)
    SEP_3 = M5.Widgets.Label("-", 116, 103, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)
    SEP_4 = M5.Widgets.Label("-", 175, 103, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)

    # Label for day of the week
    # label10 = M5.Widgets.Label("Day", 22, 160, 1.0, 0xffffff, 0x222222, M5.Widgets.FONTS.DejaVu24)

    rtc = RTC()
    rtc.timezone('UTC+5:30')

# def format_day_of_week(day_index):
#     # Format day of the week based on the numeric index
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     if 0 <= day_index < len(days):
#         return days[day_index]
#     else:
#         return ""

def format_time_component(component):
    # Ensure single digit components are prefixed with '0'
    if component < 10:
        return f"0{component}"
    else:
        return str(component)
        
def loop():
    global Hour, Seconds, COL_1, Minute, COL_2, SEP_1, DD, MM, YYYY, SEP_3, SEP_4, SEP_2, rtc #, label0
    M5.update()
    datetime = rtc.datetime()

    # Format time components
    hour = format_time_component(datetime[4])
    minute = format_time_component(datetime[5])
    second = format_time_component(datetime[6])
    day = format_time_component(datetime[2])
    month = format_time_component(datetime[1])
    year = str(datetime[0])

    # Update labels
    Hour.setText(hour)
    Minute.setText(minute)
    Seconds.setText(second)
    DD.setText(day)
    MM.setText(month)
    YYYY.setText(year)


    # Update day of the week label
    # day_of_week = format_day_of_week(datetime[3])
    # label10.setText(day_of_week)


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
