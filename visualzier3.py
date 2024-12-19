import matplotlib.pyplot as plt
import numpy as np

# Categories (Culling Strategies)
culling_strategies = ['Average', 'Aggressive', 'Minimal']

# FPS Data
fps_test = [28, 88, 17]
fps_default = [25, 85, 15]

# CPU Data (approx midpoints)
cpu_test = [36.5, 28, 36]
cpu_default = [37, 29.5, 36.5]

# GPU Data (approx midpoints)
gpu_test = [94, 68.5, 40]
gpu_default = [96.5, 70, 41]

x = np.arange(len(culling_strategies))  # the label locations
width = 0.35  # the width of the bars

def create_grouped_bar_chart(title, ylabel, test_data, default_data, y_unit=''):
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, test_data, width, label='Test Case', color='blue')
    rects2 = ax.bar(x + width/2, default_data, width, label='Default Case', color='orange')

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(culling_strategies)
    ax.legend()

    # Add value labels on top of each bar
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}{y_unit}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

    for rect in rects2:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}{y_unit}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Create FPS Chart
create_grouped_bar_chart('FPS by Culling Strategy (Test vs. Default)', 'FPS', fps_test, fps_default, 'FPS')

# Create CPU Utilization Chart (Percentage)
create_grouped_bar_chart('CPU Utilization by Culling Strategy (Test vs. Default)', 'CPU (%)', cpu_test, cpu_default, '%')

# Create GPU Utilization Chart (Percentage)
create_grouped_bar_chart('GPU Utilization by Culling Strategy (Test vs. Default)', 'GPU (%)', gpu_test, gpu_default, '%')
