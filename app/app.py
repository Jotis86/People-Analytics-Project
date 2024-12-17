import streamlit as st

# Mostrar imagen principal
st.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/principal.png", use_column_width=True)

# Título de la aplicación
st.title("People Analytics Dashboard")

# Menú de navegación
st.sidebar.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/menu.png", use_column_width=True)
st.sidebar.title("📋 Navigation Menu")
menu = st.sidebar.radio("Go to", ["Introduction & Objectives", "Project Overview", "Results", "Visualizations", "Power BI", "Metrics", "Project Conclusions"])

# Botón para ir al repositorio de GitHub
st.sidebar.markdown("[Go to GitHub Repository](https://github.com/Jotis86/People-Analytics-Project)")

# Secciones del menú
if menu == "Introduction & Objectives":
    st.header("📋 Introduction & 🎯 Objectives")
    st.write("""
    Welcome to the **People Analytics** repository created with Power BI! This project aims to provide, analyze, and visualize employee-related data such as retention, performance, satisfaction, and more.
    
    The objective of this project is to provide an interactive and detailed analysis of key employee metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.
    """)
elif menu == "Project Overview":
    st.header("📊 Project Overview")
    st.write("""
    This project includes various functionalities, tools, and development processes to ensure comprehensive analysis and visualization of employee data.

    ### 🚀 Functionality
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

    ### 🛠️ Tools Used
    - 🖥️ **Power BI**: For creating the interactive dashboard.
    - 🐍 **Python**: For data analysis.
      - 🐼 **pandas**: Data cleaning and preprocessing.
      - 📊 **matplotlib and seaborn**: Data visualization.

    ### 🔄 Development Process
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
    st.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/dashboard.png", use_column_width=True)
    st.write("The attached dashboard includes some of the visualizations created during the analysis, providing a comprehensive overview of the key metrics and insights.")
elif menu == "Power BI":
    st.header("📊 Power BI")
    st.write("""
    In Power BI, we created an interactive dashboard to visualize and analyze employee-related data. The dashboard includes various tabs and visualizations to provide insights into key metrics such as retention, performance, satisfaction, and more.
    """)
    st.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/general_analysis.png", caption="General Analysis", use_column_width=True)
    st.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/labor_analysis.png", caption="Labor Analysis", use_column_width=True)
    st.image("c:/Users/juane/OneDrive/Escritorio/Dashboard-People-Analytics-en-PowerBi/app/summary.png", caption="Summary", use_column_width=True)
elif menu == "Metrics":
    st.header("📊 Metrics")
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
             
    ### 📊 Key Metrics

    #### 🔄 Turnover Rate
    - **📋 Definition**: The turnover rate measures the percentage of employees who leave the company during a specific period. It is a critical metric for understanding employee retention and the overall stability of the workforce.
    - **📈 Importance**: High turnover rates can indicate issues with employee satisfaction, management practices, or workplace culture. Conversely, low turnover rates suggest a stable and satisfied workforce.
    - **🧮 Calculation**: Turnover Rate = (Number of terminations during a period / Total number of employees during that period) * 100
    - **📊 Example**: If a company has 10 terminations in a month and 200 employees, the turnover rate would be (10 / 200) * 100 = 5%.

    #### 📈 Net Promoter Score (NPS)
    - **📋 Definition**: The Net Promoter Score (NPS) measures employee loyalty and their likelihood to recommend the company as a great place to work. Originally used for customer satisfaction, NPS has been adapted to gauge employee engagement.
    - **📈 Importance**: NPS provides insights into employee satisfaction and loyalty. A high NPS indicates that employees are likely to recommend the company to others, reflecting a positive work environment.
    - **🧮 Calculation**: NPS = % Promoters - % Detractors
    - **👥 Groups**:
    - **👍 Promoters**: Score 9-10. These employees are highly satisfied and likely to recommend the company.
    - **😐 Passives**: Score 7-8. These employees are satisfied but not enthusiastic enough to be promoters.
    - **👎 Detractors**: Score 1-6. These employees are dissatisfied and may negatively impact the company's reputation.
    - **📊 Example**: If 60% of employees are promoters, 30% are passives, and 10% are detractors, the NPS would be 60% - 10% = 50.

    #### 📉 Absenteeism Rate
    - **📋 Definition**: The absenteeism rate measures the percentage of work hours lost due to employee absences. It includes absences due to illness, personal reasons, and other causes.
    - **📈 Importance**: High absenteeism rates can indicate issues with employee health, workplace conditions, or job satisfaction. Monitoring absenteeism helps identify and address underlying problems.
    - **🧮 Calculation**: Absenteeism Rate = (Hours not worked due to occasional causes, IT, or other reasons / Effective agreed hours) * 100
    - **⏱️ Effective Agreed Hours**: Agreed hours + Overtime hours - Hours not worked due to vacations and holidays
    - **📊 Example**: If employees collectively miss 500 hours in a month and the effective agreed hours are 10,000, the absenteeism rate would be (500 / 10,000) * 100 = 5%.

    These metrics help in understanding the overall health of the organization, identifying areas for improvement, and making data-driven decisions.
    """)
elif menu == "Project Conclusions":
    st.header("📋 Project Conclusions")
    st.write("""
    The People Analytics project has provided valuable insights into various aspects of employee data, including retention, performance, satisfaction, and more. By leveraging Power BI and Python, we have created interactive dashboards and detailed visualizations that support strategic decision-making.

    ### Key Takeaways:
    - **Employee Retention**: Understanding the factors that contribute to employee retention and identifying areas for improvement.
    - **Performance Analysis**: Assessing employee performance and identifying high-performing individuals and teams.
    - **Satisfaction and Engagement**: Gauging employee satisfaction and engagement levels to improve workplace culture.
    - **Diversity and Inclusion**: Evaluating the diversity of the workforce and promoting inclusive practices.
    - **Productivity Metrics**: Measuring productivity and identifying opportunities for optimization.

    ### Future Recommendations:
    - **Continuous Monitoring**: Regularly update and monitor key metrics to stay informed about workforce trends.
    - **Employee Feedback**: Incorporate employee feedback into the analysis to gain deeper insights into satisfaction and engagement.
    - **Advanced Analytics**: Explore advanced analytics techniques, such as machine learning, to predict employee behavior and outcomes.
    - **Integration with HR Systems**: Integrate the analytics platform with HR systems for real-time data updates and seamless analysis.

    By implementing these recommendations, organizations can enhance their people analytics capabilities and make more informed decisions to drive employee satisfaction and organizational success.
    """)