from get_date import return_time
import time
import sys
import os

start_time = time.time()
try:
    while True:
        # print('tick')
        return_time()
        time.sleep(os.environ['seconds_sleep'] - ((time.time() - start_time) % os.environ['seconds_sleep']))

except KeyboardInterrupt:
    sys.exit(0)