import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('911.csv')

# Display basic information about the dataset
df.info()
print(df.head())

# Top 5 zip codes for 911 calls
print("Top 5 Zipcodes:")
print(df['zip'].value_counts().head(5))

# Top 5 townships (twp) for 911 calls
print("Top 5 Townships:")
print(df['twp'].value_counts().head(5))

# Number of unique title codes
print("Number of Unique Titles:")
print(df['title'].nunique())

# Create a new column 'Reason' by extracting the string before ':' in the 'title' column
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# Most common Reason for a 911 call
print("Most Common Reason:")
print(df['Reason'].value_counts())

# Countplot of 911 calls by Reason
sns.countplot(x='Reason', data=df, palette='viridis')
plt.title('Count of 911 Calls by Reason')
plt.show()

# Convert the 'timeStamp' column to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# Extract hour, month, and day of the week from the DateTime objects
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day Of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

# Map numerical day of the week to string names
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day Of Week'] = df['Day Of Week'].map(dmap)

# Countplot of Day Of Week with hue based on Reason
sns.countplot(x='Day Of Week', data=df, hue='Reason', palette='viridis')
plt.title('911 Calls by Day of Week and Reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
plt.show()

# Countplot of Month with hue based on Reason
sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.title('911 Calls by Month and Reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
plt.show()

# Group data by month and count occurrences
byMonth = df.groupby('Month').count()
print(byMonth.head())

# Plot the count of calls per month
byMonth['lat'].plot()
plt.title('911 Calls per Month')
plt.xlabel('Month')
plt.ylabel('Number of Calls')
plt.show()

# Linear fit on the number of calls per month
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.title('Linear Fit of Calls per Month')
plt.show()

# Create a new column 'Date' containing the date from the timeStamp column
df['Date'] = df['timeStamp'].apply(lambda t: t.date())

# Plot counts of 911 calls grouped by Date
df.groupby('Date').count()['lat'].plot()
plt.title('911 Calls per Day')
plt.tight_layout()
plt.show()

# Separate plots for each Reason
for reason in df['Reason'].unique():
    df[df['Reason'] == reason].groupby('Date').count()['lat'].plot()
    plt.title(f'{reason} Calls')
    plt.tight_layout()
    plt.show()

# Heatmap data for Day of Week and Hour
dayHour = df.groupby(by=['Day Of Week', 'Hour']).count()['Reason'].unstack()

plt.figure(figsize=(12, 6))
sns.heatmap(dayHour, cmap='viridis')
plt.title('Heatmap of Calls by Day and Hour')
plt.show()

# Clustermap for Day of Week and Hour
sns.clustermap(dayHour, cmap='coolwarm')
plt.title('Clustermap of Calls by Day and Hour')
plt.show()

# Heatmap data for Day of Week and Month
dayMonth = df.groupby(by=['Day Of Week', 'Month']).count()['Reason'].unstack()

plt.figure(figsize=(12, 6))
sns.heatmap(dayMonth, cmap='viridis')
plt.title('Heatmap of Calls by Day and Month')
plt.show()

# Clustermap for Day of Week and Month
sns.clustermap(dayMonth, cmap='coolwarm')
plt.title('Clustermap of Calls by Day and Month')
plt.show()
