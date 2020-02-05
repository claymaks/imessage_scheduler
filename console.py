import os
from datetime import datetime as dt

#Phone Number
e1 = "12345678901"

#os.system(cmd)
#[MSG, dt(year,month,day,hour,minute,second)]
text_list = [
    ["8:50", dt(2020, 2, 5, 1, 59, 00)],
    ["8:51 and a half", dt(2019, 8, 15, 8, 51, 30)],
    ["9:00", dt(2019, 8, 15, 9, 00, 00)]
]

for t,d in text_list:
    e = (d - dt.now())
    while e.seconds + e.days * 86400 > 0:
        e = (d - dt.now())
        pass
    cmd = "osascript sendText.scpt " + e1 + " \"" + t + "\""
    os.system(cmd)
