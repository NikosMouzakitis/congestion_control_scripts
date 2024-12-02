import re # for regex expressions
import pandas as pd
import matplotlib.pyplot as plt

def extract_vals(line):
    cwnd_match = re.search(r'cwnd:(\d+)',line)
    ssthresh_match = re.search(r'ssthresh:(\d+)',line)

    cwnd = int(cwnd_match.group(1) ) if cwnd_match else 0
    ssthresh = int(ssthresh_match.group(1) ) if ssthresh_match else 0

    return cwnd, ssthresh



##dictionary for each of the streams

data = { 42008: {'timestamp': [], 'cwnd': [], 'ssthresh': [] },
         42010: {'timestamp': [], 'cwnd': [], 'ssthresh': [] },
         42012: {'timestamp': [], 'cwnd': [], 'ssthresh': [] } }


#use file produced earlier

with open('stage1.txt', 'r') as file:
    for line in file:

        ##tmst
        timestamp = line.split()[0]

        port_match = re.search(r'\b(42008|42010|42012)\b',line)

        if port_match:
            port = int(port_match.group(0))
            cwnd, ssthresh = extract_vals(line)
            data[port]['timestamp'].append(timestamp)
            data[port]['cwnd'].append(cwnd)
            data[port]['ssthresh'].append(ssthresh)

df_1 = pd.DataFrame(data[42008])
df_2 = pd.DataFrame(data[42010])
df_3 = pd.DataFrame(data[42012])

fig,axs = plt.subplots(3,1,figsize=(12,8),sharex=True)

axs[0].plot(df_1['timestamp'], df_1['cwnd'], label='cwnd', color = 'b')
axs[0].plot(df_1['timestamp'], df_1['ssthresh'], label='ssthesh', color = 'r')
axs[0].set_title('tcp reno flow 1')
axs[0].set_xlabel("time(s)")
axs[0].set_ylabel("value")
axs[0].legend(fontsize='small')

axs[1].plot(df_2['timestamp'], df_2['cwnd'], label='cwnd', color = 'b')
axs[1].plot(df_2['timestamp'], df_2['ssthresh'], label='ssthesh', color = 'r')
axs[1].set_title('tcp reno flow 2')
axs[1].set_xlabel("time(s)")
axs[1].set_ylabel("value")
axs[1].legend(fontsize='small')

axs[2].plot(df_3['timestamp'], df_3['cwnd'], label='cwnd', color = 'b')
axs[2].plot(df_3['timestamp'], df_3['ssthresh'], label='ssthesh', color = 'r')
axs[2].set_title('tcp reno flow 3')
axs[2].set_xlabel("time(s)")
axs[2].set_ylabel("value")
axs[2].legend(fontsize='small')

fig.suptitle('CWND-SSHTRHESH per FLOW')
plt.tight_layout()
plt.show()
