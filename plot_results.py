import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data into a DataFrame
data = pd.read_csv('api_performance.csv')

# Create a boxplot to visualize response times
plt.figure(figsize=(10, 6))
sns.boxplot(x='Test Case', y='Response Time (ms)', data=data)

# Add labels and title
plt.title('API Performance Boxplot')
plt.xlabel('Test Case')
plt.ylabel('Response Time (ms)')

# Save the plot as a PNG image
plt.savefig('performance_boxplot.png')

# Calculate the average (mean) latency for each test case
average_latency = data.groupby('Test Case')['Response Time (ms)'].mean()

# Save the average latencies to a new CSV file
average_latency.to_csv('average_latency.csv', sep=' ',  header=['Average Latency (ms)'])

print("Average latencies saved to 'average_latency.csv'.")
