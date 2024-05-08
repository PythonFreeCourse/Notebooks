from datetime import datetime, timedelta
import random

def no_vinnigrete(date_src, date_dst):
    # also excepts non-zero padded days and months. to achieve only zero padded we can use helper bool func with regex
    date_format = "%Y-%m-%d"
    delta = (datetime.strptime(date_dst, date_format) - datetime.strptime(date_src, date_format)).days
    if delta < 0:
        print("Didn't figure how to turn time backwards yet...")
        return
    date_middle = datetime.strptime(date_src,date_format) + timedelta(days = random.randint(0,delta))
    day = date_middle.strftime("%A")
    if day == "Monday":
        print("Ain't gettin' no vinaigrette today :(")
    else:
        print(date_middle.strftime(date_format))

def main():
    no_vinnigrete("2024-05-06", "2024-05-06") # certainly monday
    no_vinnigrete("1994-03-24", "1996-04-27") # some day
    no_vinnigrete("1996-04-27", "1994-03-24") # back to the future

if __name__ == '__main__':
    main()