# 📊 People Analytics Project

![Cover Image](images/banner.png)

![Commits](https://img.shields.io/github/commit-activity/m/Jotis86/People-Analytics-Project)
![Issues Abiertas](https://img.shields.io/github/issues/Jotis86/People-Analytics-Project)
![Pull Requests](https://img.shields.io/github/issues-pr/Jotis86/People-Analytics-Project)
![Forks](https://img.shields.io/github/forks/Jotis86/People-Analytics-Project)
![Tamaño del Repositorio](https://img.shields.io/github/repo-size/Jotis86/People-Analytics-Project)
![Autor](https://img.shields.io/badge/autor-Juan%20Duran%20Bon-blue)
![Licencia](https://img.shields.io/github/license/Jotis86/People-Analytics-Project)


## 📋 Introduction

Welcome to the **People Analytics** repository created with Power BI! 
This project aims to provide, analyze, and visualize employee-related data such as retention, performance, satisfaction, and more.

## 🎯 Objectives

The objective of this project is to provide an interactive and detailed analysis of key employee metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.

## 🚀 Functionality

This project includes:

- 📈 **Interactive visualizations**: Pivot charts and tables in Power BI to explore data.
- 📊 **Key metrics**: Analysis of important KPIs such as retention, performance, satisfaction, and more.
- 📅 **Temporal analysis**: Trends over time to identify patterns and opportunities.
- 🗂️ **Three tabs in Power BI**:
  - 🌍 **General Analysis**: Overview of all metrics.
  - 📦 **Labor Analysis**: Detailed analysis of NPS, FTE, absenteeism, training hours, sanctions, and other metrics.
  - 📊 **Summary**: Dynamic table of employees, hiring trends, working hours, among other analyzed measures.
- 🐍 **Python Analysis**:
  - 🧹 **Data Cleaning**: Using pandas for data cleaning and preprocessing.
  - 📊 **Visualization**: Using matplotlib and seaborn for data visualization.

## 🛠️ Tools Used

- 🖥️ **Power BI**: For creating the interactive dashboard.
- 🐍 **Python**: For data analysis.
  - 🐼 **pandas**: Data cleaning and preprocessing.
  - 📊 **matplotlib and seaborn**: Data visualization.

## 🔄 Development Process

- 📥 **Extraction**: Data obtained from CSV files.
- 🔄 **Transformation**:
  - 🖥️ **Power BI**:
    - 🔗 Combining tables using Power Query.
    - 🧹 Data cleaning: Removing duplicates, handling null values, and normalizing data.
    - 📈 Data enrichment: Adding calculated columns and transforming data to improve analysis.
  - 🐍 **Python**:
    - 🧹 Data cleaning with pandas: Removing duplicates, handling null values, and normalizing data.
    - 📈 Data enrichment: Adding calculated columns and transforming data to improve analysis.
- 📤 **Load**:
  - 🖥️ **Power BI**: Integrating transformed data into Power BI for analysis and visualization.
  - 🐍 **Python**: Preparing data for visualization and analysis in Jupyter notebooks.

## 📈 Results

Various metrics have been created using DAX (Data Analysis Expressions) in Power BI to provide detailed and customized analysis:

- 📊 KPIs calculation.
- 📏 Calculated measures for specific analyses.
- ➕ Calculated columns to enrich the data.
- 🔍 Filtering and dynamic segmentation of data.

In Python, the analysis includes:

- 🧹 Detailed data cleaning processes.
- 📊 Creation of visualizations to explore and present data insights.

## 📊 Power BI Dashboard

Here are some screenshots of the Power BI dashboard:

![General Analysis](images/general_analysis.png)
![Labor Analysis](images/labor_analysis.png)
![Summary](images/summary.png)

## 📊 Metrics Used

In this project, we use various metrics to analyze employee data effectively. Some of the key metrics include:

- **📈 Retention Rate**: Measures the percentage of employees who remain in the company over a specific period.
- **🔄 Turnover Rate**: Calculates the percentage of employees who leave the company during a specific period.
- **📉 Absenteeism Rate**: Tracks the number of days employees are absent from work.
- **😊 Employee Satisfaction**: Gauges employee satisfaction levels through surveys and feedback.
- **📈 Net Promoter Score (NPS)**: Measures employee loyalty and likelihood to recommend the company.
- **⏱️ Training Hours**: Tracks the number of hours employees spend in training programs.
- **📊 Performance Evaluation Scores**: Assesses employee performance based on evaluations.
- **💰 Salary Analysis**: Analyzes salary distribution and trends across different departments and roles.
- **🌐 Diversity Metrics**: Evaluates the diversity of the workforce in terms of gender, age, and other demographics.
- **📈 Productivity Metrics**: Measures employee productivity through various performance indicators.

These metrics help in understanding the overall health of the organization, identifying areas for improvement, and making data-driven decisions.

## 📂 Summary Report

For a detailed summary of the visualizations and key metrics, please refer to the [Summary Report](summary_report/README.md).

## 📊 Visualizations

In addition to the Power BI dashboard, a complete analysis has been performed using Python, including:

### 🧹 Data Cleaning with Pandas:

- **Removing Duplicates**: Ensuring that the dataset is free from duplicate entries to maintain data integrity.
- **Handling Missing Values**: Addressing missing data points through imputation or removal to ensure a complete dataset.

### 📊 Data Visualization with Matplotlib and Seaborn:

- **Histograms and Bar Charts**: Visualizing the distribution of data and comparing different categories.
- **Line Charts**: Analyzing trends over time to identify patterns and opportunities.
- **Scatter Plots**: Exploring relationships between different variables to uncover correlations.
- **Heatmaps**: Providing a visual representation of data density and relationships between variables.
- **Box Plots**: Summarizing the distribution of data and identifying outliers.

![Dashboard Example](images/plot.png)

The attached dashboard includes some of the visualizations created during the analysis, providing a comprehensive overview of the key metrics and insights.

## 📂 Project Structure

- `app/`: Streamlit app to present the results.
  - `main.py`: Main script for the Streamlit app.
- `assets/`: Directory for app assets like images and logos.
  - 🖼️ `menu.png`: Menu image.
  - 🖼️ `portada.png`: Cover image.
- `data/`: Directory for raw and processed data.
  - 📄 `marketing_campaign.csv`: Raw marketing campaign data.
  - 📄 `marketing_campaign_cleaned.csv`: Cleaned marketing campaign data.
- `images/`: Directory for Power BI screenshots.
  - 🖼️ `general_analysis.png`: Power BI screenshot 1.
  - 🖼️ `labor_analysis.png`: Power BI screenshot 2.
  - 🖼️ `summary.png`: Power BI screenshot 3.
- `notebooks/`: Jupyter notebooks with the Python analysis.
  - 📓 `data_cleaning.ipynb`: Notebook for data cleaning.
  - 📓 `data_visualization.ipynb`: Notebook for data visualization.
- `powerbi/`: Directory for Power BI files.
  - 📊 `dashboard.pbix`: Main file of the Power BI dashboard.
- `summary_report/`: Directory for summary report images and README.
  - `images/`: Directory for summary report images.
  - `README.md`: Explanation of the summary report.
- 🚫 `.gitignore`: Git ignore file.
- 📜 `LICENSE`: [License file](LICENSE).
- 📄 `README.md`: Readme file.
- 📋 `requirements.txt`: Python dependencies file.

## 🌐 Web App

The interactive app created with Streamlit allows exploring the analysis results dynamically and accessibly. It includes features such as:
- 📊 **Interactive charts and graphs**: Visualize data through various types of charts and graphs that update in real-time based on user interactions.
- 🔍 **Filters to dynamically segment data**: Apply filters to the data to focus on specific segments, such as time periods, product categories, or customer demographics.
- 📈 **Detailed views of key metrics and trends**: Drill down into specific metrics to see detailed trends and insights, helping to identify patterns and opportunities.
- 🖥️ **User-friendly interface**: The app is designed to be intuitive and easy to use, making it accessible to users with varying levels of technical expertise.
- 🛠️ **Customizable dashboards**: Users can customize the dashboards to suit their needs, adding or removing widgets and adjusting the layout as required.

You can access the web app [HERE](https://people-analytics-project-cxrukqhwgdwnagx8cabr97.streamlit.app/).

## 🛠️ Requirements

- Power BI Desktop
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## 📧 Contact

For any inquiries, you can contact me at:

- 📧 Email: jotaduranbon@gmail.com
- 💼 LinkedIn: [Juan Duran Bon](https://www.linkedin.com/in/juan-duran-bon)

## 💡 Suggestions and Contributions

Suggestions and contributions are welcome. Please open an issue or submit a pull request to discuss any changes you would like to make. Here are some ways you can contribute:

- 🐛 **Report Bugs**: If you find any bugs, please report them by opening an issue.
- 🌟 **Feature Requests**: If you have ideas for new features, feel free to suggest them.
- 💻 **Code Contributions**: You can contribute by fixing bugs, adding new features, or improving the documentation.
- 📝 **Feedback**: Any feedback to improve the project is highly appreciated.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for visiting the **People Analytics** project! We hope you find the insights and visualizations helpful for your strategic decision-making. Happy analyzing! 🚀
