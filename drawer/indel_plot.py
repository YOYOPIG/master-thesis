import matplotlib.pyplot as plt
import numpy as np

name_dict = {'1': 1, '32': 2, '64': 3, '128': 4, '256': 5}
threads = [1, 2, 3, 4, 5]
# threads = [1, 32, 64, 128, 256]
gpu = [0.342212, 0.013313]
# gpu = [0.203837/0.342212, 0.026067/0.013313]
cpu = [0.203837, 0.026067]

X_axis = np.arange(len(cpu))

plt.bar(X_axis - 0.2, cpu, 0.4, label='CPU only')
plt.bar(X_axis + 0.2, gpu, 0.4, label='With GPU')

ax = plt.gca()
# print(name_dict.values())
# print(name_dict.keys())
# ax.set_xticks([1,2,3,4,5])
# ax.set_xticklabels([1,8,16,24,32])

plt.xticks(X_axis, [0,1])

plt.legend()
plt.ylabel('Time (hr)')
plt.xlabel('Threshold')
plt.show()