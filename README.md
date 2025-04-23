# 📊 People Analytics Project

![Cover Image](images/banner.png)

![Commits](https://img.shields.io/github/commit-activity/t/Jotis86/People-Analytics-Project?color=ff80ab&label=commits)
![Stars](https://img.shields.io/github/stars/Jotis86/People-Analytics-Project?color=ff80ab)
![Issues Abiertas](https://img.shields.io/github/issues/Jotis86/People-Analytics-Project?color=ff80ab)
![Pull Requests](https://img.shields.io/github/issues-pr/Jotis86/People-Analytics-Project?color=ff80ab)
![Forks](https://img.shields.io/github/forks/Jotis86/People-Analytics-Project?color=ff80ab)
![Tamaño del Repositorio](https://img.shields.io/github/repo-size/Jotis86/People-Analytics-Project?color=ff80ab)
![Último Commit](https://img.shields.io/github/last-commit/Jotis86/People-Analytics-Project?color=ff80ab)
![Autor](https://img.shields.io/badge/autor-Juan%20Duran%20Bon-ff80ab)
![Licencia](https://img.shields.io/github/license/Jotis86/People-Analytics-Project?color=ff80ab)


## 📋 Introduction

Welcome to the **People Analytics** repository created with Power BI! 
This project aims to provide, analyze, and visualize employee-related data such as retention, performance, satisfaction, and more.

## 🎯 Objectives

The primary objective of this project is to **transform raw HR data into actionable business intelligence** that supports strategic decision-making across all levels of the organization.  
By combining **Power BI's visualization capabilities** with **Python's analytical power**, we aim to:

- 🔍 **Identify Key Retention Drivers**: Analyze factors correlated with employee turnover to develop targeted retention strategies  
- 😊 **Measure Employee Engagement**: Track satisfaction metrics to understand workforce sentiment and improvement opportunities  
- 📈 **Optimize Performance Management**: Provide insights into performance patterns across departments, roles, and time periods  
- 💸 **Guide Compensation Strategy**: Analyze salary data relative to market rates and performance  
- 🧠 **Enable Data-Driven HR Decisions**: Replace intuition with evidence-based approaches to workforce management  
- 🌐 **Democratize HR Analytics**: Make complex workforce data accessible to stakeholders with varying technical expertise  
- 🔮 **Predict Future Workforce Trends**: Utilize historical patterns to forecast key metrics and proactively address challenges  
  

## 🚀 Functionality

This project delivers a comprehensive suite of analytical capabilities:

### 📈 Interactive Visualizations

- 🎛️ Dynamic filtering from company-wide to department-specific metrics  
- 🔁 Cross-filtering between visualizations for multidimensional analysis  
- 🧩 Customizable dashboards with slicers (time, department, roles)  
- 💡 Tooltip-enhanced visuals with contextual information  
- 📱 Mobile-responsive design for on-the-go insights  


### 📊 Key Metrics Analysis

- 🔄 **Turnover Analysis**: Voluntary vs. involuntary, regrettable vs. non-regrettable  
- 🧾 **Performance Metrics**: Ratings distribution, trends, high-potential tracking  
- ❤️ **Satisfaction & Engagement**: NPS scores, survey results, correlation with retention  
- 💰 **Compensation Analysis**: Salary benchmarking, pay equity, compensation-to-performance ratios  
- 🎓 **Training Effectiveness**: Learning hours vs. performance improvement, skill gaps  
- 🌍 **Diversity Metrics**: Representation and inclusion indicators  

### 📅 Temporal Analysis

- 📊 Year-over-year comparison of all KPIs  
- 📆 Seasonal patterns in hiring, turnover, and performance  
- 🔎 Trend detection with statistical significance  
- 🤖 Predictive modeling for workforce planning  
- 🚨 Anomaly detection in key metrics  


## 🛠️ Tools Used

### 🖥️ Power BI

- 💻 **Power BI Desktop**: Dashboard development  
- ☁️ **Power BI Service**: Cloud-based sharing and collaboration  
- 🔣 **DAX**: Custom calculations and KPIs  
- 🔄 **Power Query**: ETL for data transformation  
- 🧮 **M Language**: Advanced prep and transformation  
- 📊 **Custom Visuals**: Decomposition tree, key influencers, AI visuals  
- 🔐 **Row-Level Security**: Controlled access based on roles  

---

### 🐍 Python Ecosystem

#### 📦 pandas

- 🧹 Data cleaning and preprocessing  
- 📅 Time series and datetime handling  
- 🔄 Aggregation and pivot operations  

#### ➗ NumPy

- 🔢 Numerical calculations and performance boosts  

#### 📉 matplotlib & seaborn

- 🎨 Advanced visualizations beyond Power BI  
- 📊 Box plots, violin plots, correlation heatmaps  
- 🎨 Branded color palettes  

#### 🤖 scikit-learn

- 📈 Predictive modeling (e.g., turnover)   
- 🔍 Feature importance analysis  

## 🚀 Streamlit

- 🧱 Interactive web app with component-based UI  
- 🔁 Real-time Python integration  

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


### 🔑 Key Features

- 📊 **Interactive visualizations**  
  Dynamic and responsive charts that update in real-time as filters are applied, making it easy to explore trends and compare different segments.

- 🔍 **Multi-dimensional filtering**  
  Easily segment data by department, role, tenure, performance ratings, and more. This allows for deep dives into specific employee groups or organizational units.

- 📈 **Key HR metrics**  
  Track and monitor essential HR indicators such as turnover rates, employee performance, engagement levels, and compensation structures. All metrics are updated automatically with the latest data.

- 🧠 **Predictive insights**  
  Leverage built-in analytics to identify trends, forecast risks, and uncover hidden patterns in employee behavior and workforce dynamics.

- 🖥️ **User-friendly interface**  
  Built with accessibility in mind, the dashboard is easy to use for both technical and non-technical users, ensuring that everyone can gain value from the data.

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
