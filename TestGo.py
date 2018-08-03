
import psutil
Host=[r"\\172.16.119.30\C$",r"\\172.16.119.30\D$",r"\\172.16.119.30\E$"]
for x in Host:
    str=psutil.disk_usage(x)
    print(str.percent)
    if str.percent>73.5:
        print("大了",x)
    else:
        print("小了")
    # print(x)
