import datetime
import os

while 1>0:
    os.system("cls")
    Ftime = '2023-6-26 00:00'
    Stime = datetime.datetime.now()
    a=Stime.strftime('%Y-%m-%d %H:%M:%S')
    Finaltime = datetime.datetime.strptime(Ftime, "%Y-%m-%d %H:%M")
    b=Finaltime.strftime('%Y-%m-%d')
    print("当前时间为：",a)
    print("中考时间为：",b)
    print("距离中考还有：",Finaltime-Stime)
    input("回车刷新……")
    
