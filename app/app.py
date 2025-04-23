import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from PIL import Image
import io

# Set page config
st.set_page_config(page_title="People Analytics Dashboard", page_icon="👥", layout="wide")

# Custom styling
st.markdown("""
<style>
    .main-header {font-size: 34px; font-weight: bold; margin-bottom: 20px;}
    .section-header {font-size: 24px; font-weight: bold; margin-top: 30px;}
    .highlight {color: #FF4B4B; font-weight: bold;}
    .card {
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 15px;
        text-align: center;
    }
    .metric-value {font-size: 24px; font-weight: bold; color: #FF4B4B;}
    .metric-label {font-size: 14px; color: #555;}
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    # Path to your CSV file
    data_path = os.path.join('notebook', 'data_cleaned.csv')
    if os.path.exists(data_path):
        data = pd.read_csv(data_path)
        return data
    else:
        st.error(f"Data file not found at {data_path}")
        return None

# Create matplotlib/seaborn chart in memory
def create_figure(plot_function, **kwargs):
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_function(ax=ax, **kwargs)
    plt.tight_layout()
    
    # Convert plot to image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas absolutas de las imágenes
principal_image_path = os.path.join(current_dir, 'banner.png')
menu_image_path = os.path.join(current_dir, 'funko.png')
dashboard_image_path = os.path.join(current_dir, 'dashboard.png')
general_analysis_image_path = os.path.join(current_dir, 'general_analysis.png')
labor_analysis_image_path = os.path.join(current_dir, 'labor_analysis.png')
summary_image_path = os.path.join(current_dir, 'summary.png')
clip_video_path = os.path.join(current_dir, 'clip.mp4')

# Título de la aplicación
st.markdown('<p class="main-header">People Analytics Project</p>', unsafe_allow_html=True)

# Mostrar imagen principal con tamaño controlado
st.image(principal_image_path, use_container_width=True)

# Menú de navegación (mejorado)
with st.sidebar:
    st.sidebar.image(menu_image_path, use_container_width=True)
    st.sidebar.markdown("## 📋 Navigation Menu")
    
    menu = st.sidebar.radio(
        "Select a section:",
        [
            "🏠 Home & Objectives", 
            "📊 Project Overview", 
            "📈 Results",
            "📊 Interactive Visualizations", 
            "📊 Power BI Dashboards", 
            "📏 Key Metrics", 
            "🎯 Conclusions"
        ]
    )
    
    # GitHub repo link
    st.sidebar.markdown("---")
    if st.sidebar.button('🔗 View GitHub Repository'):
        st.sidebar.markdown("[GitHub Repository](https://github.com/Jotis86/People-Analytics-Project)")

# Load data for visualizations
df = load_data()

# Secciones del menú
if menu == "🏠 Home & Objectives":
    st.markdown('<p class="section-header">📋 Introduction & 🎯 Objectives</p>', unsafe_allow_html=True)
    
    # Use columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Welcome to People Analytics!
        
        This project provides interactive analysis of key employee metrics to support strategic decision-making, including:
        
        - 📊 **Employee retention and turnover analysis**
        - 📈 **Performance evaluation insights**
        - 😊 **Satisfaction and engagement metrics**
        - 📚 **Training impact assessment**
        - 📉 **Absenteeism analysis**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Primary Objectives")
        st.markdown("""
        - 📊 Data-driven HR insights
        - 🔍 Identify retention factors
        - 📈 Optimize performance
        - 🌟 Enhance employee experience
        - 📊 Strategic workforce planning
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📊 Project Overview":
    st.markdown('<p class="section-header">📊 Project Overview</p>', unsafe_allow_html=True)
    
    # Display project diagram
    st.image(dashboard_image_path, use_container_width=True)
    
    # Use tabs for better organization
    tab1, tab2, tab3 = st.tabs(["Functionality", "Tools Used", "Process"])
    
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Key Functionality
        
        - 📈 **Interactive Power BI visualizations** with customizable filters
        - 📊 **Comprehensive KPI tracking** for HR metrics
        - 📅 **Time-series analysis** to identify workforce trends
        - 📊 **Three specialized dashboards** for different analysis perspectives
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Power BI
            
            - 📊 Interactive dashboards
            - 📈 Customizable visuals
            - 🔄 Real-time filtering
            - 🔗 Data relationships
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Python Analysis
            
            - 🧹 Pandas data cleaning
            - 📊 Matplotlib visualization
            - 📈 Seaborn statistical plots
            - 🔢 NumPy calculations
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Development Process
        
        1. **Data Extraction** from HR systems
        2. **Cleaning & Transformation** to prepare for analysis
        3. **Exploratory Analysis** to identify patterns
        4. **Dashboard Creation** for interactive exploration
        5. **Metric Development** to track key indicators
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📈 Results":
    st.markdown('<p class="section-header">📈 Key Results</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Power BI Analysis
        
        - 📊 **Custom KPI calculations** for retention, satisfaction and performance
        - 📏 **DAX calculated measures** for advanced metric analysis
        - ➕ **Calculated columns** for enhanced categorization
        - 🔍 **Dynamic filtering** for focused analysis
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        ### Python Insights
        
        - 🧹 **Comprehensive data cleaning** methodologies
        - 📊 **Statistical analysis** of key workforce variables
        - 📈 **Correlation analysis** between performance factors
        - 🔍 **Outlier detection** in salary and performance metrics
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Show sample visualization
    st.image(dashboard_image_path, caption="Sample dashboard visualization", use_container_width=True)

elif menu == "📊 Interactive Visualizations":
    st.markdown('<p class="section-header">📊 Interactive Visualizations</p>', unsafe_allow_html=True)
    
    # Visualization selection
    viz_options = [
        "Age Distribution",
        "Gender Distribution",
        "Department Distribution",
        "Salary Analysis",
        "Tenure Analysis",
        "Performance Metrics",
        "Rotation Analysis",
        "Training Impact"
    ]
    
    selected_viz = st.selectbox("Select visualization type:", viz_options)
    
    # Check if data is loaded
    if df is not None:
        # Filter options
        with st.expander("Visualization Filters"):
            filter_col1, filter_col2 = st.columns(2)
            
            with filter_col1:
                if 'Departamento' in df.columns:
                    dept_filter = st.multiselect(
                        "Department",
                        options=sorted(df['Departamento'].unique()),
                        default=sorted(df['Departamento'].unique())[:5] if len(df['Departamento'].unique()) > 5 else sorted(df['Departamento'].unique())
                    )
                
                if 'Edad' in df.columns:
                    age_range = st.slider(
                        "Age Range",
                        min_value=int(df['Edad'].min()),
                        max_value=int(df['Edad'].max()),
                        value=(int(df['Edad'].min()), int(df['Edad'].max()))
                    )
            
            with filter_col2:
                if 'Sexo' in df.columns:
                    gender_filter = st.multiselect(
                        "Gender",
                        options=sorted(df['Sexo'].unique()),
                        default=sorted(df['Sexo'].unique())
                    )
                
                if 'Categoría laboral' in df.columns:
                    category_filter = st.multiselect(
                        "Job Category",
                        options=sorted(df['Categoría laboral'].unique()),
                        default=sorted(df['Categoría laboral'].unique())[:3] if len(df['Categoría laboral'].unique()) > 3 else sorted(df['Categoría laboral'].unique())
                    )
        
        # Apply filters
        filtered_df = df.copy()
        
        if 'Departamento' in df.columns and locals().get('dept_filter'):
            filtered_df = filtered_df[filtered_df['Departamento'].isin(dept_filter)]
        
        if 'Edad' in df.columns and locals().get('age_range'):
            filtered_df = filtered_df[(filtered_df['Edad'] >= age_range[0]) & (filtered_df['Edad'] <= age_range[1])]
        
        if 'Sexo' in df.columns and locals().get('gender_filter'):
            filtered_df = filtered_df[filtered_df['Sexo'].isin(gender_filter)]
        
        if 'Categoría laboral' in df.columns and locals().get('category_filter'):
            filtered_df = filtered_df[filtered_df['Categoría laboral'].isin(category_filter)]
        
        # Display visualization based on selection
        st.markdown(f"### {selected_viz}")
        
        if selected_viz == "Age Distribution":
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(filtered_df['Edad'], bins=20, kde=True, ax=ax)
            ax.set_title('Age Distribution')
            ax.set_xlabel('Age')
            ax.set_ylabel('Count')
            st.pyplot(fig)
            
            # Include additional insights
            st.markdown(f"""
            **Key Insights:**
            - Average age: {filtered_df['Edad'].mean():.1f} years
            - Youngest employee: {filtered_df['Edad'].min()} years
            - Oldest employee: {filtered_df['Edad'].max()} years
            """)
        
        elif selected_viz == "Gender Distribution":
            # Create figure
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Plot
            gender_counts = filtered_df['Sexo'].value_counts()
            colors = sns.color_palette("pastel")[0:len(gender_counts)]
            gender_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=colors, ax=ax)
            ax.set_title('Gender Distribution')
            ax.set_ylabel('')
            
            # Display
            st.pyplot(fig)
            
            # Show counts in a table
            st.markdown("**Gender Breakdown:**")
            st.dataframe(gender_counts.reset_index().rename(columns={'index': 'Gender', 'Sexo': 'Count'}))
        
        elif selected_viz == "Department Distribution":
            # Create horizontal bar chart of departments
            fig, ax = plt.subplots(figsize=(10, 8))
            dept_counts = filtered_df['Departamento'].value_counts()
            dept_counts = dept_counts.sort_values(ascending=True)
            
            sns.barplot(x=dept_counts.values, y=dept_counts.index, palette='viridis', ax=ax)
            ax.set_title('Department Distribution')
            ax.set_xlabel('Number of Employees')
            ax.set_ylabel('Department')
            
            st.pyplot(fig)
            
            # Show department percentages
            st.markdown("**Department Size (% of workforce):**")
            dept_pct = (filtered_df['Departamento'].value_counts(normalize=True) * 100).reset_index()
            dept_pct.columns = ['Department', 'Percentage']
            dept_pct['Percentage'] = dept_pct['Percentage'].round(1).astype(str) + '%'
            st.dataframe(dept_pct)
        
        elif selected_viz == "Salary Analysis":
            # Create two columns for visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # Salary distribution
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                sns.histplot(filtered_df['Salario Anual Actual 2020'], bins=15, kde=True, ax=ax1)
                ax1.set_title('Salary Distribution (2020)')
                ax1.set_xlabel('Annual Salary')
                ax1.set_ylabel('Count')
                # Format x-axis to show thousands
                ax1.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
                st.pyplot(fig1)
            
            with col2:
                # Salary by department boxplot
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.boxplot(x='Departamento', y='Salario Anual Actual 2020', data=filtered_df, ax=ax2)
                ax2.set_title('Salary by Department')
                ax2.set_xlabel('Department')
                ax2.set_ylabel('Annual Salary')
                plt.xticks(rotation=45, ha='right')
                # Format y-axis to show thousands
                ax2.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
                plt.tight_layout()
                st.pyplot(fig2)
            
            # Show salary statistics
            st.markdown("**Salary Statistics:**")
            salary_stats = filtered_df['Salario Anual Actual 2020'].describe()
            st.dataframe({
                'Metric': ['Average', 'Minimum', 'Maximum', '25th Percentile', 'Median', '75th Percentile'],
                'Value': [
                    f"€{salary_stats['mean']:,.0f}",
                    f"€{salary_stats['min']:,.0f}",
                    f"€{salary_stats['max']:,.0f}",
                    f"€{salary_stats['25%']:,.0f}",
                    f"€{salary_stats['50%']:,.0f}",
                    f"€{salary_stats['75%']:,.0f}"
                ]
            })
        
        elif selected_viz == "Tenure Analysis":
            # Create two columns for visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # Tenure distribution
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                sns.histplot(filtered_df['Antigüedad Años'], bins=15, kde=True, ax=ax1)
                ax1.set_title('Tenure Distribution (Years)')
                ax1.set_xlabel('Years of Service')
                ax1.set_ylabel('Count')
                st.pyplot(fig1)
            
            with col2:
                # Age vs Tenure scatterplot
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.scatterplot(x='Edad', y='Antigüedad Años', hue='Sexo', data=filtered_df, ax=ax2)
                ax2.set_title('Age vs Tenure')
                ax2.set_xlabel('Age')
                ax2.set_ylabel('Years of Service')
                plt.tight_layout()
                st.pyplot(fig2)
            
            # Tenure by department
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            sns.boxplot(x='Departamento', y='Antigüedad Años', data=filtered_df, ax=ax3)
            ax3.set_title('Tenure by Department')
            ax3.set_xlabel('Department')
            ax3.set_ylabel('Years of Service')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig3)
        
        elif selected_viz == "Performance Metrics":
            # Create two columns for visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # Performance distribution
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                sns.histplot(filtered_df['Evaluación Desempeño'], bins=10, kde=True, ax=ax1)
                ax1.set_title('Performance Evaluation Distribution')
                ax1.set_xlabel('Performance Score')
                ax1.set_ylabel('Count')
                st.pyplot(fig1)
            
            with col2:
                # Performance by department
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.boxplot(x='Departamento', y='Evaluación Desempeño', data=filtered_df, ax=ax2)
                ax2.set_title('Performance by Department')
                ax2.set_xlabel('Department')
                ax2.set_ylabel('Performance Score')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig2)
            
            # Performance vs Training hours
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            sns.scatterplot(
                x='Horas de formación recibidas', 
                y='Evaluación Desempeño', 
                hue='Departamento',
                size='Antigüedad Años',
                sizes=(50, 200),
                alpha=0.7,
                data=filtered_df,
                ax=ax3
            )
            ax3.set_title('Training Hours vs Performance')
            ax3.set_xlabel('Training Hours')
            ax3.set_ylabel('Performance Score')
            plt.tight_layout()
            st.pyplot(fig3)
        
        elif selected_viz == "Rotation Analysis":
            # Rotation counts
            rotation_external = filtered_df['Rotación Externa'].value_counts()
            rotation_internal = filtered_df['Rotación Interna'].value_counts()
            
            # Create two columns for visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # External rotation
                fig1, ax1 = plt.subplots(figsize=(8, 8))
                ax1.pie(
                    rotation_external, 
                    labels=['No', 'Yes'] if 1 in rotation_external.index else ['No'],
                    autopct='%1.1f%%',
                    colors=sns.color_palette('pastel')[0:2],
                    startangle=90
                )
                ax1.set_title('External Rotation')
                st.pyplot(fig1)
                
                # Add metric
                external_pct = (rotation_external.get(1, 0) / rotation_external.sum() * 100) if not rotation_external.empty else 0
                st.metric("External Rotation Rate", f"{external_pct:.1f}%")
            
            with col2:
                # Internal rotation
                fig2, ax2 = plt.subplots(figsize=(8, 8))
                ax2.pie(
                    rotation_internal, 
                    labels=['No', 'Yes'] if 1 in rotation_internal.index else ['No'],
                    autopct='%1.1f%%',
                    colors=sns.color_palette('pastel')[2:4],
                    startangle=90
                )
                ax2.set_title('Internal Rotation')
                st.pyplot(fig2)
                
                # Add metric
                internal_pct = (rotation_internal.get(1, 0) / rotation_internal.sum() * 100) if not rotation_internal.empty else 0
                st.metric("Internal Rotation Rate", f"{internal_pct:.1f}%")
            
            # Department rotation analysis
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            dept_rotation = filtered_df.groupby('Departamento')['Rotación Externa'].mean() * 100
            dept_rotation = dept_rotation.sort_values(ascending=False)
            
            sns.barplot(x=dept_rotation.index, y=dept_rotation.values, palette='viridis', ax=ax3)
            ax3.set_title('External Rotation by Department (%)')
            ax3.set_xlabel('Department')
            ax3.set_ylabel('External Rotation %')
            plt.xticks(rotation=45, ha='right')
            ax3.set_ylim(0, max(dept_rotation.values) * 1.2)
            
            # Add percentage labels on bars
            for i, v in enumerate(dept_rotation.values):
                ax3.text(i, v + 0.5, f"{v:.1f}%", ha='center')
                
            plt.tight_layout()
            st.pyplot(fig3)
        
        elif selected_viz == "Training Impact":
            # Create two columns for visualizations
            col1, col2 = st.columns(2)
            
            with col1:
                # Training hours distribution
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                sns.histplot(filtered_df['Horas de formación recibidas'], bins=15, kde=True, ax=ax1)
                ax1.set_title('Training Hours Distribution')
                ax1.set_xlabel('Training Hours')
                ax1.set_ylabel('Count')
                st.pyplot(fig1)
            
            with col2:
                # Training hours by department
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                sns.boxplot(x='Departamento', y='Horas de formación recibidas', data=filtered_df, ax=ax2)
                ax2.set_title('Training Hours by Department')
                ax2.set_xlabel('Department')
                ax2.set_ylabel('Training Hours')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig2)
            
            # Correlation between training and performance
            st.subheader("Training Impact on Performance")
            
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            sns.regplot(
                x='Horas de formación recibidas', 
                y='Evaluación Desempeño', 
                data=filtered_df,
                scatter_kws={'alpha':0.5},
                line_kws={'color': 'red'},
                ax=ax3
            )
            ax3.set_title('Training Hours vs Performance Score')
            ax3.set_xlabel('Training Hours')
            ax3.set_ylabel('Performance Score')
            plt.tight_layout()
            st.pyplot(fig3)
            
            # Calculate correlation
            corr = filtered_df[['Horas de formación recibidas', 'Evaluación Desempeño']].corr().iloc[0,1]
            st.metric("Correlation Coefficient", f"{corr:.3f}")
    else:
        st.error("Dataset not loaded. Please ensure 'data_cleaned.csv' is available in the correct location.")

elif menu == "📊 Power BI Dashboards":
    st.markdown('<p class="section-header">📊 Power BI Dashboards</p>', unsafe_allow_html=True)
    
    # Use tabs for organization
    tabs = st.tabs(["General Analysis", "Labor Analysis", "Summary"])
    
    with tabs[0]:
        st.image(general_analysis_image_path, use_container_width=True)
        with st.expander("Dashboard Details"):
            st.markdown("""
            The **General Analysis** dashboard provides a comprehensive overview of key workforce metrics:
            
            - Employee demographics and distribution
            - Salary analysis across departments
            - Tenure and experience visualization
            - Performance metrics by team
            """)
    
    with tabs[1]:
        st.image(labor_analysis_image_path, use_container_width=True)
        with st.expander("Dashboard Details"):
            st.markdown("""
            The **Labor Analysis** dashboard focuses on workforce productivity and engagement:
            
            - NPS scores and satisfaction metrics
            - FTE distribution across departments
            - Absenteeism patterns and trends
            - Training effectiveness analysis
            """)
    
    with tabs[2]:
        st.image(summary_image_path, use_container_width=True)
        with st.expander("Dashboard Details"):
            st.markdown("""
            The **Summary** dashboard provides a tabular overview of all metrics:
            
            - Employee roster with key indicators
            - Hiring trends over time
            - Working hours optimization
            - Department-level performance metrics
            """)
    
    # Dashboard demo video
    st.subheader("Interactive Dashboard Demo")
    st.video(clip_video_path)

elif menu == "📏 Key Metrics":
    st.markdown('<p class="section-header">📏 Key HR Metrics</p>', unsafe_allow_html=True)
    
    # Display metrics in cards
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    
    with metric_col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🔄 Turnover Rate")
        
        if df is not None:
            turnover_rate = df['Rotación Externa'].mean() * 100
            st.markdown(f'<p class="metric-value">{turnover_rate:.1f}%</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Percentage of employees who left during a period
        
        **Formula**: (Employees who left / Total employees) × 100
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📈 NPS Score")
        
        if df is not None:
            avg_nps = df['NPS'].mean()
            st.markdown(f'<p class="metric-value">{avg_nps:.1f}</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Net Promoter Score measuring employee loyalty
        
        **Formula**: Promoters % - Detractors %
        
        **Scale**: 1-10, where 9-10: Promoters, 7-8: Passive, 1-6: Detractors
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📉 Absenteeism Rate")
        
        if df is not None:
            # Calculate average days lost per employee
            avg_days_lost = df['Días de Trabajo Perdido (Abs)'].mean()
            st.markdown(f'<p class="metric-value">{avg_days_lost:.1f} days</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Average work days lost per employee
        
        **Impact**: High absenteeism can indicate workplace issues or job dissatisfaction
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Second row of metrics
    metric_col4, metric_col5, metric_col6 = st.columns(3)
    
    with metric_col4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📊 Performance Score")
        
        if df is not None:
            avg_performance = df['Evaluación Desempeño'].mean()
            st.markdown(f'<p class="metric-value">{avg_performance:.1f}/10</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Average performance evaluation score
        
        **Scale**: 1-10, with 10 being the highest performance
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col5:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ⏱️ Training Hours")
        
        if df is not None:
            avg_training = df['Horas de formación recibidas'].mean()
            st.markdown(f'<p class="metric-value">{avg_training:.1f} hours</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Average training hours per employee
        
        **Impact**: Investment in employee development and skill enhancement
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with metric_col6:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💰 Salary Growth")
        
        if df is not None:
            avg_salary_diff = df['Diferencia Salario'].mean()
            pct_with_increase = (df['Diferencia Salario'] > 0).mean() * 100
            st.markdown(f'<p class="metric-value">€{avg_salary_diff:.0f}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="metric-label">{pct_with_increase:.1f}% received an increase</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="metric-value">--</p>', unsafe_allow_html=True)
            
        st.markdown("""
        **Definition**: Average salary increase in 2020
        
        **Impact**: Indicator of compensation strategy and employee value
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🎯 Conclusions":
    st.markdown('<p class="section-header">🎯 Project Conclusions</p>', unsafe_allow_html=True)
    
    # Use columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Key Findings")
        st.markdown("""
        The People Analytics project has revealed several important insights:
        
        - **Employee Retention Factors**: We identified key drivers of retention, including compensation, management quality, and career development opportunities.
        
        - **Performance Patterns**: Analysis revealed strong correlations between training investment and performance outcomes.
        
        - **Department-Level Insights**: Significant variations in engagement, performance, and turnover were observed across departments.
        
        - **Satisfaction Drivers**: NPS analysis highlighted crucial factors affecting employee satisfaction and engagement.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Recommendations")
        st.markdown("""
        Based on our analysis:
        
        1. **Targeted Training**: Increase training in departments with lower performance scores
        
        2. **Retention Strategy**: Focus on departments with high turnover rates
        
        3. **Engagement Initiatives**: Address low NPS scores with targeted engagement programs
        
        4. **Continuous Monitoring**: Implement ongoing analytics for proactive management
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Final thoughts
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Future Directions")
    st.markdown("""
    To further enhance people analytics capabilities:
    
    - **Predictive Models**: Develop predictive models for turnover risk and performance outcomes
    - **Real-Time Dashboards**: Implement real-time analytics for immediate insights
    - **Integration with HRIS**: Seamlessly connect with HR information systems
    - **Expanded Metrics**: Include additional metrics such as recruitment efficiency and culture indicators
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Signature
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #555;">
    <p>Project developed by Juan Duran Bon</p>
    </div>
    """, unsafe_allow_html=True)