# from datetime import timezone
from datetime import datetime
import datetime
from dateutil.parser import parse


def parse_date_convert(date, fmt=None):
    if fmt is None:
        fmt = '%Y-%m-%d %H:%M:%S' # Defaults to : 2022-08-31 07:47:30
    get_date_obj = parse(str(date))
    return str(get_date_obj.strftime(fmt))
    
### example for testing     
example_arrival_timestamp = '2022-10-17T00:29:23Z'

def get_time_difference(arrival_time):

    ### convert timestamp into a date string. Example: '2022-10-16T18:52:27Z' => 2022-10-16 18:52:27 <class 'str'>
    converted_arrival_timestamp = parse_date_convert(arrival_time)

    ### convert the string which is now in a new format back into a date object
    converted_arrival_date = datetime.datetime.strptime(converted_arrival_timestamp, '%Y-%m-%d %H:%M:%S')

    now = datetime.datetime.now()   
    
    ### Testing specific now date
    ### examples formats: "2022-10-17T02:01:55Z"   2022-10-17 02:01:55
    # test_date = "2022-10-17 01:57:55"
    # test_converted_now_timestamp  = parse_date_convert(test_date)
    # test_converted_now_date = datetime.datetime.strptime(test_converted_now_timestamp, '%Y-%m-%d %H:%M:%S')
    # now_minute = test_converted_now_date.minute

    now_minute = now.minute
    arrival_minute = converted_arrival_date.minute
    
    if arrival_minute < now_minute:
        print('minute rollover')
        print("pre arrival_minute: ", arrival_minute)
        print("pre now_minute: ", now_minute)
        arrival_minute += 60
        print("post arrival_minute: ", arrival_minute)
        print("post now_minute: ", now_minute)

  
    next_bus = arrival_minute - now_minute
    return next_bus

