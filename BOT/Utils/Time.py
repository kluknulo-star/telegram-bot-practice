from datetime import datetime

MOUNTH_TIME = 2629753
WEEK_TIME = 604810
DAY_TIME = 86410
HOUR_TIME = 3610

def get_time(mounth = 0, week = 0, day = 0 ,hour = 0):
    current_datetime = (datetime.now()).timestamp()
    res_time = current_datetime - mounth * MOUNTH_TIME - week * WEEK_TIME - day * DAY_TIME - hour * HOUR_TIME
    return res_time