import streamlit as st
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas absolutas de las imágenes
principal_image_path = os.path.join(current_dir, 'principal.png')
menu_image_path = os.path.join(current_dir, 'menu.png')
dashboard_image_path = os.path.join(current_dir, 'dashboard.png')
general_analysis_image_path = os.path.join(current_dir, 'general_analysis.png')
labor_analysis_image_path = os.path.join(current_dir, 'labor_analysis.png')
summary_image_path = os.path.join(current_dir, 'summary.png')

# Mostrar imagen principal
st.image(principal_image_path, use_container_width=True)

# Título de la aplicación
st.title("People Analytics Project")

# Menú de navegación
st.sidebar.image(menu_image_path, use_container_width=True)
st.sidebar.title("📋 Navigation Menu")
menu = st.sidebar.radio("Go to", ["Introduction & Objectives", "Project Overview", "Results", "Visualizations", "Power BI", "Metrics", "Project Conclusions"])

# Botón para ir al repositorio de GitHub
if st.sidebar.button('🔗 Go to GitHub Repository'):
    st.sidebar.markdown("[Click here to visit the GitHub Repository](https://github.com/Jotis86/People-Analytics-Project)")

# Secciones del menú
if menu == "Introduction & Objectives":
    st.header("📋 Introduction & 🎯 Objectives")
    st.write("""
    Welcome to the **People Analytics** repository created with Power BI! This project aims to provide, analyze, and visualize employee-related data such as retention, performance, satisfaction, and more.

    The objective of this project is to provide an interactive and detailed analysis of key employee metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.

    ### Introduction
    In today's competitive business environment, understanding and managing employee data is crucial for organizational success. People Analytics involves the use of data and analytical techniques to gain insights into various aspects of the workforce, such as employee retention, performance, satisfaction, and diversity. By analyzing this data, organizations can make informed decisions that enhance employee engagement, productivity, and overall business performance.

    ### Objectives
    The primary objectives of this People Analytics project are:
    - **📊 Data Collection and Integration**: Gather employee-related data from various sources and integrate it into a unified dataset for comprehensive analysis.
    - **🧹 Data Cleaning and Preprocessing**: Ensure the accuracy and consistency of the data by removing duplicates, handling missing values, and normalizing data formats.
    - **📈 Interactive Dashboards**: Create interactive dashboards using Power BI to visualize key employee metrics and trends. These dashboards provide an intuitive and user-friendly interface for exploring the data.
    - **📊 Advanced Analytics**: Utilize Python for advanced data analysis, including statistical analysis, data visualization, and predictive modeling. This helps uncover hidden patterns and insights within the data.
    - **📋 Strategic Decision-Making**: Provide actionable insights to support strategic decision-making in areas such as talent management, employee engagement, and organizational development.
    - **🔄 Continuous Improvement**: Establish a framework for continuous monitoring and improvement of employee metrics to ensure ongoing organizational success.

    ### Key Areas of Focus
    - **🔄 Employee Retention**: Analyze factors that influence employee retention and identify strategies to reduce turnover rates. This includes examining employee demographics, job satisfaction, and career development opportunities.
    - **📈 Performance Management**: Assess employee performance through key performance indicators (KPIs) and performance evaluations. Identify high-performing individuals and teams, as well as areas for improvement.
    - **😊 Employee Satisfaction and Engagement**: Measure employee satisfaction and engagement levels through surveys and feedback mechanisms. Understand the drivers of employee satisfaction and develop initiatives to enhance engagement.
    - **🌐 Diversity and Inclusion**: Evaluate the diversity of the workforce in terms of gender, age, ethnicity, and other demographics. Promote inclusive practices and ensure equal opportunities for all employees.
    - **📚 Training and Development**: Track employee training hours and participation in development programs. Assess the impact of training on employee performance and career progression.
    - **📉 Absenteeism and Attendance**: Monitor absenteeism rates and identify patterns or trends related to employee attendance. Address underlying issues that contribute to high absenteeism rates.

    ### Benefits of People Analytics
    - **📊 Data-Driven Insights**: Gain a deeper understanding of the workforce through data-driven insights, enabling more informed decision-making.
    - **😊 Improved Employee Engagement**: Identify factors that influence employee engagement and implement strategies to enhance job satisfaction and motivation.
    - **📈 Enhanced Performance Management**: Use data to assess and improve employee performance, leading to higher productivity and organizational effectiveness.
    - **📋 Strategic Workforce Planning**: Develop strategic workforce plans based on data insights, ensuring the right talent is in place to achieve business goals.
    - **🔄 Increased Retention Rates**: Implement targeted initiatives to reduce employee turnover and retain top talent within the organization.
    - **🌐 Promoting Diversity and Inclusion**: Foster a diverse and inclusive workplace by understanding and addressing diversity-related challenges.

    By leveraging People Analytics, organizations can create a more engaged, productive, and satisfied workforce, ultimately driving business success and achieving long-term goals.
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

    - 📊 **KPIs Calculation**: Key Performance Indicators (KPIs) have been calculated to measure critical aspects of employee performance and organizational health. These KPIs include metrics such as employee retention rate, turnover rate, and absenteeism rate.
    - 📏 **Calculated Measures**: Specific measures have been calculated to provide deeper insights into various aspects of the data. These measures help in understanding trends, patterns, and correlations within the dataset.
    - ➕ **Calculated Columns**: Additional columns have been created to enrich the dataset and facilitate more detailed analysis. These columns include derived metrics and categorizations that enhance the analytical capabilities of the dataset.
    - 🔍 **Filtering and Dynamic Segmentation**: Advanced filtering and segmentation techniques have been applied to the data to enable dynamic analysis. This allows users to explore the data from different perspectives and gain insights into specific segments of the workforce.

    In Python, the analysis includes:

    - 🧹 **Detailed Data Cleaning Processes**: Comprehensive data cleaning processes have been implemented using pandas to ensure the accuracy and consistency of the data. This includes removing duplicates, handling missing values, and normalizing data formats.
    - 📊 **Creation of Visualizations**: Various visualizations have been created using matplotlib and seaborn to explore and present data insights. These visualizations include histograms, bar charts, line charts, scatter plots, heatmaps, and box plots.

    ### Key Visualizations

    - **📊 Histograms and Bar Charts**: These visualizations help in understanding the distribution of data and comparing different categories. They provide a clear view of the frequency and proportion of various data points.
    - **📈 Line Charts**: Line charts are used to analyze trends over time, helping to identify patterns and opportunities for improvement. They are particularly useful for tracking changes in key metrics over specific periods.
    - **🔍 Scatter Plots**: Scatter plots are used to explore relationships between different variables, uncovering correlations and potential causations. They provide a visual representation of how two variables interact with each other.
    - **🔥 Heatmaps**: Heatmaps provide a visual representation of data density and relationships between variables. They are useful for identifying areas of high and low concentration within the dataset.
    - **📦 Box Plots**: Box plots summarize the distribution of data and help in identifying outliers. They provide a clear view of the central tendency, variability, and skewness of the data.

    These visualizations and analyses provide a comprehensive overview of the dataset, highlighting key aspects such as demographics, salary, tenure, training, absenteeism, rotation, performance, and NPS. By analyzing these metrics, organizations can gain valuable insights into their workforce, identify areas for improvement, and make data-driven decisions to enhance employee satisfaction and productivity.
    """)
elif menu == "Visualizations":
    st.header("📊 Visualizations")
    st.write("""
    In addition to the Power BI dashboard, a complete analysis has been performed using Python, including:

    - **📊 Histograms and Bar Charts**: Visualizing the distribution of data and comparing different categories. These visualizations help in understanding the frequency and proportion of various data points, making it easier to identify trends and patterns.
    - **📈 Line Charts**: Analyzing trends over time to identify patterns and opportunities. Line charts are particularly useful for tracking changes in key metrics over specific periods, helping to forecast future trends and make informed decisions.
    - **🔍 Scatter Plots**: Exploring relationships between different variables to uncover correlations. Scatter plots provide a visual representation of how two variables interact with each other, revealing potential causations and correlations.
    - **🔥 Heatmaps**: Providing a visual representation of data density and relationships between variables. Heatmaps are useful for identifying areas of high and low concentration within the dataset, highlighting significant patterns and anomalies.
    - **📦 Box Plots**: Summarizing the distribution of data and identifying outliers. Box plots offer a clear view of the central tendency, variability, and skewness of the data, making it easier to spot outliers and understand the overall distribution.

    ### Detailed Analysis of Visualizations

    - **📊 Age Distribution**: This histogram shows the distribution of ages within the company, helping to understand the age demographics of the workforce.
    - **👥 Gender Distribution**: This bar chart displays the count of employees by gender, providing insights into gender diversity within the organization.
    - **💍 Marital Status Distribution**: This bar chart illustrates the distribution of employees' marital status, offering a view of the workforce's personal demographics.
    - **🎓 Education Level Distribution**: This bar chart shows the distribution of employees' education levels, highlighting the educational background of the workforce.
    - **🏢 Department Distribution**: This horizontal bar chart displays the count of employees in each department, helping to understand the distribution of the workforce across different departments.
    - **💰 Salary Range Distribution (2020)**: This bar chart shows the distribution of annual salaries for 2020, providing insights into the salary structure within the organization.
    - **💵 Salary Distribution by Department**: This box plot compares annual salaries for 2020 across different departments, highlighting salary variations and outliers within departments.
    - **📅 Tenure Distribution (Months)**: This histogram shows the distribution of employees' tenure in months, helping to understand the length of service of the workforce.
    - **📈 Age vs. Tenure**: This scatter plot explores the relationship between age and tenure, revealing potential correlations between these two variables.
    - **📈 Age vs. NPS**: This line chart analyzes the relationship between age and Net Promoter Score (NPS), providing insights into how employee satisfaction varies with age.
    - **🔄 External Rotation Distribution**: This pie chart displays the count of employees who have experienced external rotation, offering a view of workforce mobility.
    - **🔄 Internal Rotation Distribution**: This pie chart shows the count of employees who have experienced internal rotation, highlighting internal mobility within the organization.

    These visualizations are crucial for gaining a comprehensive understanding of the dataset, allowing organizations to identify key insights and make data-driven decisions.
    """)
    st.image(dashboard_image_path, use_container_width=True)
    st.write("The attached dashboard includes some of the visualizations created during the analysis, providing a comprehensive overview of the key metrics and insights.")


elif menu == "Power BI":
    st.header("📊 Power BI")
    st.write("""
    In Power BI, we created an interactive dashboard to visualize and analyze employee-related data. The dashboard includes various tabs and visualizations to provide insights into key metrics such as retention, performance, satisfaction, and more.

    ### Key Features of the Power BI Dashboard:
    - **🌍 General Analysis**: This tab provides an overview of all key metrics, offering a high-level view of the organization's performance. It includes visualizations such as bar charts, line charts, and pie charts to represent various metrics.
    - **📦 Labor Analysis**: This tab offers a detailed analysis of specific metrics such as Net Promoter Score (NPS), Full-Time Equivalent (FTE), absenteeism, training hours, and sanctions. It helps in understanding the workforce's engagement and productivity levels.
    - **📊 Summary**: The summary tab includes a dynamic table of employees, hiring trends, working hours, and other analyzed measures. It provides a comprehensive view of the workforce, helping to identify trends and patterns in employee data.

    ### Benefits of Using Power BI:
    - **📈 Interactive Visualizations**: Power BI allows users to interact with the data through various visualizations, making it easier to explore and understand complex datasets.
    - **🔍 Advanced Filtering**: Users can apply advanced filtering techniques to the data, enabling dynamic analysis and the ability to view data from different perspectives.
    - **📊 Real-Time Data Updates**: Power BI supports real-time data updates, ensuring that the dashboard always reflects the most current information.
    - **📋 Customizable Dashboards**: Users can customize the dashboard to meet their specific needs, adding or removing visualizations and adjusting the layout as required.
    - **📊 Data Integration**: Power BI can integrate data from multiple sources, providing a unified view of the organization's performance.

    By leveraging the capabilities of Power BI, organizations can gain valuable insights into their workforce, identify areas for improvement, and make data-driven decisions to enhance employee satisfaction and productivity.
    """)
    st.image(general_analysis_image_path, caption="General Analysis", use_container_width=True)
    st.image(labor_analysis_image_path, caption="Labor Analysis", use_container_width=True)
    st.image(summary_image_path, caption="Summary", use_container_width=True)


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

    Throughout this project, we have focused on understanding the key drivers of employee behavior and performance. By analyzing various metrics, we have been able to identify patterns and trends that can help organizations make more informed decisions. The insights gained from this analysis can be used to develop targeted strategies that enhance employee engagement, improve performance, and foster a positive workplace culture.

    ### Key Takeaways:
    - **🔄 Employee Retention**: Understanding the factors that contribute to employee retention and identifying areas for improvement. This helps in developing strategies to reduce turnover and retain top talent.
    - **📈 Performance Analysis**: Assessing employee performance and identifying high-performing individuals and teams. This enables targeted development and recognition programs to enhance productivity.
    - **😊 Satisfaction and Engagement**: Gauging employee satisfaction and engagement levels to improve workplace culture. By understanding what drives satisfaction, organizations can implement initiatives to boost morale and engagement.
    - **🌐 Diversity and Inclusion**: Evaluating the diversity of the workforce and promoting inclusive practices. This ensures a diverse and equitable work environment, fostering innovation and collaboration.
    - **📊 Productivity Metrics**: Measuring productivity and identifying opportunities for optimization. This helps in streamlining processes and improving overall efficiency.

    ### Future Recommendations:
    - **🔄 Continuous Monitoring**: Regularly update and monitor key metrics to stay informed about workforce trends. This allows for timely interventions and adjustments to strategies.
    - **🗣️ Employee Feedback**: Incorporate employee feedback into the analysis to gain deeper insights into satisfaction and engagement. This ensures that employee voices are heard and considered in decision-making.
    - **🤖 Advanced Analytics**: Explore advanced analytics techniques, such as machine learning, to predict employee behavior and outcomes. This can provide predictive insights and help in proactive management.
    - **🔗 Integration with HR Systems**: Integrate the analytics platform with HR systems for real-time data updates and seamless analysis. This ensures that the data is always current and relevant, enhancing the accuracy of insights.

    By implementing these recommendations, organizations can enhance their people analytics capabilities and make more informed decisions to drive employee satisfaction and organizational success.

    ### Final Thoughts
    The journey through the People Analytics Dashboard has been enlightening, revealing the power of data in transforming workforce management. We believe that the insights and recommendations provided will serve as a valuable resource for your organization, guiding you towards a more engaged, productive, and satisfied workforce.

    Remember, the key to success lies in continuous improvement and adaptation. Keep monitoring, analyzing, and acting on the data to stay ahead in the ever-evolving business landscape.

    Thank you for being a part of this journey. If you have any questions or need further assistance, don't hesitate to reach out. Together, let's build a brighter future for your organization!

    Best wishes,
    Juan Duran Bon
    """)