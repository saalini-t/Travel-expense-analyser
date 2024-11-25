import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/shalu/Downloads/travel_expense_dataset.csv") 

# Visualization 1: Cost Breakdown (Pie Chart)
cost_columns = ['Accommodation Cost', 'Transport Cost', 'Food Cost', 'Activity Cost', 'Misc Cost']
cost_breakdown = df[cost_columns].mean()

plt.figure(figsize=(8, 6))
plt.pie(cost_breakdown, labels=cost_columns, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title('Average Cost Breakdown')
plt.show()

# Visualization 2: Destination-Based Expense Trends (Bar Chart)
dest_expenses = df.groupby('Destination')['Total Expense (INR)'].mean()

plt.figure(figsize=(10, 6))
plt.bar(dest_expenses.index, dest_expenses, color='skyblue')
plt.title('Average Total Expense by Destination')
plt.xlabel('Destination')
plt.ylabel('Average Total Expense (INR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 3: Seasonal Variation in Costs (Boxplot Simulation with Error Bars)
season_expenses = df.groupby('Season')['Total Expense (INR)']
season_mean = season_expenses.mean()
season_std = season_expenses.std()

plt.figure(figsize=(10, 6))
plt.bar(season_mean.index, season_mean, yerr=season_std, color='lightgreen', capsize=5)
plt.title('Travel Expenses Across Seasons')
plt.xlabel('Season')
plt.ylabel('Total Expense (INR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 4: Transport Mode Analysis (Bar Chart)
transport_expenses = df.groupby('Transport Mode')['Transport Cost'].mean()

plt.figure(figsize=(10, 6))
plt.bar(transport_expenses.index, transport_expenses, color='orange')
plt.title('Average Transport Cost by Mode')
plt.xlabel('Transport Mode')
plt.ylabel('Average Transport Cost (INR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 5: Accommodation Type Comparison (Bar Chart)
accommodation_expenses = df.groupby('Accommodation Type')['Accommodation Cost'].mean()

plt.figure(figsize=(10, 6))
plt.bar(accommodation_expenses.index, accommodation_expenses, color='purple')
plt.title('Accommodation Costs by Type')
plt.xlabel('Accommodation Type')
plt.ylabel('Average Accommodation Cost (INR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 6: Duration vs. Total Expense (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(df['Duration (Days)'], df['Total Expense (INR)'], color='red', alpha=0.6, edgecolor='black')
for i, destination in enumerate(df['Destination']):
    plt.text(df['Duration (Days)'][i], df['Total Expense (INR)'][i], destination, fontsize=9, ha='right')
plt.title('Duration vs Total Expense')
plt.xlabel('Duration (Days)')
plt.ylabel('Total Expense (INR)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Visualization 7: Number of Travelers and Cost Sharing (Bar Chart)
df['Cost per Traveler'] = df['Total Expense (INR)'] / df['No. of Travelers']
group_cost_per_traveler = df.groupby('No. of Travelers')['Cost per Traveler'].mean()

plt.figure(figsize=(10, 6))
plt.bar(group_cost_per_traveler.index.astype(str), group_cost_per_traveler, color='teal')
plt.title('Cost per Traveler by Group Size')
plt.xlabel('Number of Travelers')
plt.ylabel('Cost per Traveler (INR)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
