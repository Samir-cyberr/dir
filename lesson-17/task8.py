import matplotlib.pyplot as plt
import numpy as np

time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [20, 35, 30, 35]
category_B = [25, 32, 34, 20]
category_C = [15, 18, 20, 25]

x = np.arange(len(time_periods))

plt.figure(figsize=(8, 6))
plt.bar(x, category_A, label='Category A', color='skyblue')
plt.bar(x, category_B, bottom=category_A, label='Category B', color='lightgreen')
bottom_C = np.array(category_A) + np.array(category_B)
plt.bar(x, category_C, bottom=bottom_C, label='Category C', color='salmon')

plt.title('Stacked Bar Chart of Categories Over Time')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.xticks(x, time_periods)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
