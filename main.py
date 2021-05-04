from get_date import return_time,datetime
from datetime import timedelta
from send_sms import *
from weather import *

import time
import sys
import os



def main():
    start_time = time.time()
    try:
        while True:
            message = get_weather(os.environ['city'])
            send_text(message,os.environ['phone_num'])


            time.sleep(float(os.environ['seconds_sleep']) - ((time.time() - start_time) % float(os.environ['seconds_sleep'])))

    except KeyboardInterrupt:
        sys.exit(0)




if __name__ == "__main__":
    main()