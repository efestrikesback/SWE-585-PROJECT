import matplotlib.pyplot as plt
import numpy as np

# Data
culling_strategies = ['Average', 'Aggressive', 'Minimal']
fps_disabled = [16, 50, 4]
fps_enabled = [25, 85, 15]

cpu_disabled = [41, 30, 32]
cpu_enabled = [37, 29.5, 36.5]

gpu_disabled = [96.5, 86.5, 45]
gpu_enabled = [96.5, 70, 41]

x = np.arange(len(culling_strategies))  # the label locations
width = 0.35  # the width of the bars

# FPS Chart
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, fps_disabled, width, label='LOD Disabled')
rects2 = ax.bar(x + width/2, fps_enabled, width, label='LOD Enabled')

ax.set_ylabel('FPS')
ax.set_title('FPS by Culling Strategy and LOD State')
ax.set_xticks(x, culling_strategies)
ax.legend()

plt.show()

# CPU Utilization Chart
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, cpu_disabled, width, label='LOD Disabled')
rects2 = ax.bar(x + width/2, cpu_enabled, width, label='LOD Enabled')

ax.set_ylabel('CPU Utilization (%)')
ax.set_title('CPU Utilization by Culling Strategy and LOD State')
ax.set_xticks(x, culling_strategies)
ax.legend()

plt.show()

# GPU Utilization Chart
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gpu_disabled, width, label='LOD Disabled')
rects2 = ax.bar(x + width/2, gpu_enabled, width, label='LOD Enabled')

ax.set_ylabel('GPU Utilization (%)')
ax.set_title('GPU Utilization by Culling Strategy and LOD State')
ax.set_xticks(x, culling_strategies)
ax.legend()

plt.show()
