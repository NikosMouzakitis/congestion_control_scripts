import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sender-ss.csv", names=['time', 'sender', 'retx_unacked', 'retx_cum', 'cwnd', 'ssthresh', 'rtt'])

# exclude the "control" flow
s = df.groupby('sender').size()
df_filtered = df[df.groupby("sender")['sender'].transform('size') > 100]
time_min = df_filtered.time.min()

fig, axs = plt.subplots(2, sharex=True, figsize=(8,6))

axs[0].plot(df_filtered['time']-time_min, df_filtered['cwnd'], label="cwnd")
axs[0].plot(df_filtered['time']-time_min, df_filtered['ssthresh'], label="ssthresh")
axs[0].set_ylim([0,150])

axs[1].plot(df_filtered['time']-time_min, df_filtered['rtt'], label="rtt", color='purple')
axs[1].set_ylim([0, 1000])
axs[1].set_xlabel("Time (s)");

plt.tight_layout();
fig.legend(loc='upper right', ncol=2);

plt.savefig("cwnd-rtt.png")
