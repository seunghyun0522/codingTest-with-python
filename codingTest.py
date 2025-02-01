from datetime import datetime

year = datetime.today().year       
month=datetime.today().month
day=datetime.today().day        

print("%d-%02d-%02d" % (year, month, day))
