from datetime import datetime
print("Current date:",datetime.utcnow())
date= datetime.utcnow() - datetime(1970, 1, 1)
print("Number of days since epoch:",date)
seconds =(date.total_seconds())
milliseconds = round(seconds*1000)
print("Milliseconds since epoch:",milliseconds)