import matplotlib.pyplot as plt
import numpy as np

name_dict = {'1': 1, '32': 2, '64': 3, '128': 4, '256': 5}
threads = [1, 2, 3, 4, 5]
# threads = [1, 32, 64, 128, 256]
cpu = [0.203837, 0.050556, 0.050278, 0.053056, 0.055000]
gpu = [0.342212, 0.209722, 0.215000, 0.217778, 0.224167]

X_axis = np.arange(len(cpu))

plt.bar(X_axis - 0.2, cpu, 0.4, label='CPU only')
plt.bar(X_axis + 0.2, gpu, 0.4, label='With GPU')


ax = plt.gca()
# print(name_dict.values())
# print(name_dict.keys())
# ax.set_xticks([1,2,3,4,5])
# ax.set_xticklabels([1,8,16,24,32])

plt.xticks(X_axis, [1,8,16,24,32])

plt.legend()
plt.ylabel('Execution time (hr)')
plt.xlabel('CPU thread count')
plt.show()