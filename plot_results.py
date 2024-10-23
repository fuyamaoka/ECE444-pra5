import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data into a DataFrame
data = pd.read_csv('api_performance.csv')

# Create a boxplot to visualize the response times
plt.figure(figsize=(10, 6))
sns.boxplot(x='Test Case', y='Response Time (ms)', data=data)

# Add labels and title
plt.title('API Performance Boxplot')
plt.xlabel('Test Case')
plt.ylabel('Response Time (ms)')

# Save the plot as a PNG image
plt.savefig('performance_boxplot.png')

# Display the plot
plt.show()

# Calculate and print the average latency for each test case
average_latency = data.groupby('Test Case')['Response Time (ms)'].mean()
print("Average Latency (ms):\n", average_latency)
