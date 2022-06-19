import matplotlib.pyplot as plt
import numpy as np

# name_dict = {'1': 1, '32': 2, '64': 3, '128': 4, '256': 5}
# threads = [1, 2, 3, 4, 5]
# threads = [1, 32, 64, 128, 256]
cpu = [0.003138, 0.005464, 0.012608, 0.149415, 1.004396, 7.811107]
gpu = [0.003586, 0.007852, 0.014832, 0.053753, 0.094673, 0.158172]

X_axis = np.arange(len(cpu))

plt.bar(X_axis - 0.2, cpu, 0.4, label='CPU only')
plt.bar(X_axis + 0.2, gpu, 0.4, label='With GPU')

ax = plt.gca()
# print(name_dict.values())
# print(name_dict.keys())
# ax.set_xticks([1,2,3,4,5])
# ax.set_xticklabels([1,8,16,24,32])
# ax.set_yscale('log')
plt.xticks(X_axis, [100,500,1000,5000,10000,20000])

plt.legend()
plt.ylabel('Execution time (hr) in logarithm')
plt.xlabel('Input read length')
plt.show()