import matplotlib.pyplot as plt
import matplotlib
name_dict = {'1': 1, '32': 2, '64': 3, '128': 4, '256': 5}
threads = [1, 2, 3, 4, 5]
# threads = [1, 32, 64, 128, 256]
a = [0.363213,0.351147,0.350840,0.349051,0.346477]

b = [0.364184, 0.342212, 0.345006, 0.344206, 0.344719]

c=[0.353136, 0.353382, 0.347007, 0.349023, 0.345956]

d=[0.354095 & 0.353936, 0.352839, 0.349773, 0.349343]

e=[0.351260, 0.355450, 0.359848, 0.361534, 0.357256]

plt.plot(threads, a, label='1 block')
plt.plot(threads, b, label='32 blocks')
plt.plot(threads, c, label='64 blocks')
plt.plot(threads, d, label='128 blocks')
plt.plot(threads, e, label='256 blocks')
ax = plt.gca()
print(name_dict.values())
print(name_dict.keys())
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(name_dict.keys())

plt.legend()
plt.ylabel('Execution time (hr)')
plt.xlabel('Thread count in each block')
plt.show()