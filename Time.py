import time

# timespan =time.strftime("%H:%M:%S")
# print(timespan)
# timespan = time.strftime("%H")
# print(int(timespan))
# timespan = time.strftime("%M")
# print(int(timespan))
# timespan = time.strftime("%S")
# print(int(timespan))


T = time.localtime()
Formated_tme = time.strftime("%Y-%d-%m %H:%M:%S %p %A %B",T)
print(Formated_tme)
Time = time.strftime("%c",T)
print(Time)
