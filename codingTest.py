from datetime import datetime

year = datetime.today().year       
month=datetime.today().month
day1=datetime.today().day        

print("%d-%02d-%02d" % (year, month, day1))
