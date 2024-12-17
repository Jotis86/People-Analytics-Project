import streamlit as st
from PIL import Image


# Cargar imágenes
menu_image = Image.open("menu.png")
main_image = Image.open("principal.png")

# Mostrar imagen principal
st.image(main_image, use_container_width=True)

# Título de la aplicación
st.title("People Analytics Dashboard")

# Menú de navegación
st.sidebar.image(menu_image, use_container_width=True)
st.sidebar.title("📋 Navigation Menu")
menu = st.sidebar.radio("Go to", ["Introduction & Objectives", "Functionality", "Tools Used", "Development Process", "Results", "Visualizations", "Power BI", "Metrics & Summary Report"])

# Botón para ir al repositorio de GitHub
st.sidebar.markdown("[Go to GitHub Repository](https://github.com/Jotis86/People-Analytics-Project)")

# Secciones del menú
if menu == "Introduction & Objectives":
    st.header("📋 Introduction & 🎯 Objectives")
    st.write("Welcome to the **People Analytics** repository created with Power BI! This project aims to provide, analyze, and visualize employee-related data such as retention, performance, satisfaction, and more.")
    st.write("The objective of this project is to provide an interactive and detailed analysis of key employee metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.")
elif menu == "Functionality":
    st.header("🚀 Functionality")
    st.write("""
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
    """)
elif menu == "Tools Used":
    st.header("🛠️ Tools Used")
    st.write("""
    - 🖥️ **Power BI**: For creating the interactive dashboard.
    - 🐍 **Python**: For data analysis.
      - 🐼 **pandas**: Data cleaning and preprocessing.
      - 📊 **matplotlib and seaborn**: Data visualization.
    """)
elif menu == "Development Process":
    st.header("🔄 Development Process")
    st.write("""
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
    """)
elif menu == "Results":
    st.header("📈 Results")
    st.write("""
    Various metrics have been created using DAX (Data Analysis Expressions) in Power BI to provide detailed and customized analysis:
    - 📊 KPIs calculation.
    - 📏 Calculated measures for specific analyses.
    - ➕ Calculated columns to enrich the data.
    - 🔍 Filtering and dynamic segmentation of data.
    In Python, the analysis includes:
    - 🧹 Detailed data cleaning processes.
    - 📊 Creation of visualizations to explore and present data insights.
    """)
elif menu == "Visualizations":
    st.header("📊 Visualizations")
    st.write("""
    In addition to the Power BI dashboard, a complete analysis has been performed using Python, including:
    - **Histograms and Bar Charts**: Visualizing the distribution of data and comparing different categories.
    - **Line Charts**: Analyzing trends over time to identify patterns and opportunities.
    - **Scatter Plots**: Exploring relationships between different variables to uncover correlations.
    - **Heatmaps**: Providing a visual representation of data density and relationships between variables.
    - **Box Plots**: Summarizing the distribution of data and identifying outliers.
    """)
    st.image("dashboard.png", use_container_width=True)
    st.write("The attached dashboard includes some of the visualizations created during the analysis, providing a comprehensive overview of the key metrics and insights.")
elif menu == "Power BI":
    st.header("📊 Power BI")
    st.write("""
    In Power BI, we created an interactive dashboard to visualize and analyze employee-related data. The dashboard includes various tabs and visualizations to provide insights into key metrics such as retention, performance, satisfaction, and more.
    """)
    st.image("general_analysis.png", caption="General Analysis", uuse_container_width=True)
    st.image("labor_analysis.png", caption="Labor Analysis", use_container_width=True)
    st.image("summary.png", caption="Summary", use_container_width=True)
elif menu == "Metrics & Summary Report":
    st.header("📊 Metrics & Summary Report")
    st.write("""
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
    """)
    st.write("""
    This directory contains images of the various charts and graphs generated during the analysis, along with brief descriptions of each.
    - **📈 Age Distribution**: Shows the distribution of employee ages within the company.
    - **👥 Gender Distribution**: Displays the count of employees by gender.
    - **💍 Marital Status Distribution**: Illustrates the distribution of employees' marital status.
    - **🎓 Education Level Distribution**: Shows the distribution of employees' education levels.
    - **🏢 Department Distribution**: Displays the count of employees in each department.
    - **💰 Salary Distribution**: Shows the distribution of annual salaries for 2020.
    - **💵 Salary by Gender**: Compares annual salaries for 2020 between genders.
    - **🏢 Salary by Department**: Compares annual salaries for 2020 across different departments.
    - **🎓 Salary by Education Level**: Compares annual salaries for 2020 based on education levels.
    - **📅 Tenure Distribution**: Shows the distribution of employees' tenure in months.
    - **🏢 Tenure by Department**: Compares tenure in months across different departments.
    - **⏱️ Training Hours Distribution**: Shows the distribution of training hours received by employees.
    - **🏢 Training Hours by Department**: Compares training hours received across different departments.
    - **📉 Absenteeism Distribution**: Shows the distribution of days of work lost due to absenteeism.
    - **🏢 Absenteeism by Department**: Compares days of work lost across different departments.
    - **🔄 External Rotation Distribution**: Displays the count of employees who have experienced external rotation.
    - **🔄 Internal Rotation Distribution**: Displays the count of employees who have experienced internal rotation.
    - **📊 Performance Evaluation Distribution**: Shows the distribution of performance evaluations.
    - **🏢 Performance Evaluation by Department**: Compares performance evaluations across different departments.
    - **📈 NPS Distribution**: Shows the distribution of Net Promoter Scores (NPS).
    These visualizations provide a comprehensive overview of the dataset, highlighting key aspects such as demographics, salary, tenure, training, absenteeism, rotation, performance, and NPS.
    """)