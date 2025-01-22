# Emergency Call Analysis Project

## Overview

The **Emergency Call Analysis Project** uses real-world 911 call data to analyze and visualize emergency trends. This project provides valuable insights into call volumes, types, and locations, helping authorities and organizations optimize their response strategies.

---

## Key Features

- **Data Loading and Cleaning**: Processes large datasets of 911 calls.
- **Time Series Analysis**: Examines call trends over time.
- **Categorical Analysis**: Investigates call reasons and response types.
- **Geographic Insights**: Maps emergency call locations.
- **Visual Analytics**: Generates clear and actionable visualizations.

---

## Project Files

### 1. `911_Calls.py`
This script handles data preprocessing, analysis, and visualization.

#### Key Components:

- **Data Loading**:
  - Reads the `911.csv` dataset.

- **Data Cleaning**:
  - Parses timestamps and extracts features like hour, month, and day.
  - Creates new columns for call reasons and types.

- **Data Visualization**:
  - Generates line plots for time-based trends.
  - Creates bar charts for categorical analysis.
  - Produces maps for geographic insights.

#### Example Code:
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('911.csv')
data['timeStamp'] = pd.to_datetime(data['timeStamp'])
data['Hour'] = data['timeStamp'].dt.hour

# Visualize call reasons
sns.countplot(x='Reason', data=data)
plt.title('Call Reasons Distribution')
plt.show()
```

### 2. `911.csv`
The dataset contains detailed records of 911 emergency calls, including:

- **lat/lon**: Latitude and longitude of the call.
- **timeStamp**: Date and time of the call.
- **Reason**: Type of emergency (e.g., Fire, Traffic, EMS).
- **Location**: Address of the call.
- **Category**: Coded information about the call.

---

## How to Run the Project

### Step 1: Install Dependencies
Ensure required libraries are installed:
```bash
pip install pandas seaborn matplotlib
```

### Step 2: Run the Script
Execute the main script:
```bash
python 911_Calls.py
```

### Step 3: View Results
- Plots and visualizations will be displayed in the output.
- Insights include time-based trends, reason distribution, and geographic maps.

---

## Future Enhancements

- **Interactive Dashboards**: Build real-time dashboards using Plotly or Dash.
- **Prediction Models**: Implement machine learning to forecast call volumes.
- **Deeper Geographic Insights**: Integrate external maps for richer spatial analysis.
- **Emergency Resource Optimization**: Suggest resource allocation strategies based on data trends.

---

## Conclusion

The **Emergency Call Analysis Project** highlights the power of data-driven insights in optimizing emergency responses. With its modular design and focus on visual analytics, this project is a stepping stone for further exploration and innovation in emergency management.

---

**Happy Analyzing!**

