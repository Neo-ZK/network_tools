import matplotlib.pyplot as plt
import sys
import pandas as pd
from datetime import datetime
import time

file = sys.argv[1]
time_arr = []
rtt_arr = []
link_able_arr = []
burst = 1
exit_tag = 0

f = open(file)
start_line = 0

for i in range(1, start_line):
    line1 = f.readline()
    if not line1:
        print("out of file index")
        exit()

for i in range(1, 149593):
    line1 = f.readline()
    if not line1:
        exit_tag = 1
        break
    info_arr_1 = line1.split(" ")
    seq_1 = info_arr_1[8].split("=")[1]
    seq_1 = seq_1.strip('\n')
    time_record = info_arr_1[1].split(",")[0]
    time_arr.append(time_record)


    line2 = f.readline()
    if not line2:
        exit_tag = 1
        break
    info_arr_2 = line2.split(" ")
    try:
        seq_2 = info_arr_2[8].split("=")[1]
        seq_2 = seq_2.strip(',')
    except:
        seq_2 = "timeout"

    if seq_1 != seq_2:
        print(seq_1, seq_2)
        link_able_arr.append(0)
        print("seq_1:%d is loss:" % (int(seq_1)))
        rtt_arr.append(rtt_arr[len(rtt_arr) - 1])
    else:
        link_able_arr.append(1)
        rtt = info_arr_2[9].split("=")[1]
        rtt = float(rtt[:len(rtt)-3])
        rtt_arr.append(rtt)

f.close()

start_time_string = time_arr[0]
end_time_string = time_arr[len(time_arr) - 1]
axis_x = pd.date_range(start=start_time_string, end=end_time_string, periods = len(time_arr))

#axis_x = axis_x.strftime('%H:%M:%S')

#plt.ylim(200, 400)
#plt.plot(axis_x, rtt_arr)
#plt.ylabel('ms')
#plt.xlabel('format: day hour:min')
#plt.axis([0, axis_x[len(axis_x)-1], 200, 400])

plt.plot(axis_x, link_able_arr)
plt.show()
