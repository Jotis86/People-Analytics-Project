import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from PIL import Image
import io
import pickle
from datetime import datetime, date
import math

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
    

# Load model
@st.cache_resource
def load_model():
    try:
        # Import joblib
        import joblib
        
        # Try multiple possible locations for the model file
        possible_paths = [
            os.path.join(current_dir, 'modelo_rotacion_externa_random_forest.pkl'),  # Same directory as app.py
            os.path.join(current_dir, 'models', 'modelo_rotacion_externa_random_forest.pkl'),  # models subfolder
            os.path.join('models', 'modelo_rotacion_externa_random_forest.pkl'),  # models folder (relative)
            os.path.join('..', 'modelo_rotacion_externa_random_forest.pkl'),  # Parent directory
            os.path.join('..', 'models', 'modelo_rotacion_externa_random_forest.pkl'),  # models in parent dir
            os.path.join('notebook', 'modelo_rotacion_externa_random_forest.pkl')  # notebook directory
        ]
        
        # Try each path until we find the file
        for path in possible_paths:
            if os.path.exists(path):
                st.success(f"Model found at: {path}")
                
                # Use joblib to load the model
                model = joblib.load(path)
                return model
        
        # If we get here, no file was found
        st.error("Model file not found in any of the expected locations")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
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
# Enhanced application title with gradient styling
st.markdown("""
<div style="background: linear-gradient(to right, #1E3A8A, #3B82F6); 
            padding: 15px; 
            border-radius: 10px; 
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 8px solid #1E40AF;">
    <h1 style="color: white; 
              font-size: 36px; 
              margin: 0;
              text-align: center;
              font-weight: 600;
              letter-spacing: 1px;
              text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);">
        <span style="margin-right: 10px;">👥</span>
        People Analytics Project
        <span style="margin-left: 10px;">📊</span>
    </h1>
    <p style="color: #E5E7EB; 
              text-align: center; 
              margin: 8px 0 0 0;
              font-size: 16px;
              font-style: italic;">
        Data-driven insights for strategic HR decisions
    </p>
</div>
""", unsafe_allow_html=True)

# Mostrar imagen principal con tamaño controlado
#st.image(principal_image_path, use_container_width=True)

# Menú de navegación
with st.sidebar:
    # Custom CSS for sidebar with blue background
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #2E86C1;  /* Blue background */
            border-right: 1px solid #2574a9;
            padding: 1rem;
        }
        .sidebar-header {
            font-size: 24px;
            font-weight: bold;
            color: white;  /* White text on blue background */
            margin-bottom: 20px;
        }
        /* Style for radio button container */
        div.row-widget.stRadio > div {
            background-color: transparent;
            border-radius: 8px;
        }
        /* Style for radio button options */
        div.row-widget.stRadio > div[role="radiogroup"] > label {
            color: white !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px;
            transition: all 0.3s;
        }
        div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
            background-color: rgba(255, 255, 255, 0.1);
            border-left: 3px solid white;
        }
        /* White text for all elements in sidebar */
        section[data-testid="stSidebar"] .element-container {
            color: white !important;
        }
        section[data-testid="stSidebar"] p, 
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3 {
            color: white !important;
        }
        /* Style for description text */
        .nav-description {
            font-size: 14px;
            color: rgba(255, 255, 255, 0.7) !important;
            margin-bottom: 20px;
        }
        /* Buttons with white background */
        section[data-testid="stSidebar"] button {
            background-color: white !important;
            color: #2E86C1 !important;
            border: none !important;
            font-weight: bold !important;
        }
        section[data-testid="stSidebar"] button:hover {
            background-color: #f0f0f0 !important;
        }
        /* Footer */
        .sidebar-footer {
            margin-top: 30px;
            padding-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            font-size: 12px;
            color: rgba(255, 255, 255, 0.7) !important;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Logo/header image with shadow
    st.image(menu_image_path, use_container_width=True)
    
    # Navigation header
    st.markdown('<p class="sidebar-header">📋 Navigation</p>', unsafe_allow_html=True)
    
    # Custom navigation options
    nav_options = {
        "🏠 Home & Objectives": "Get started and learn about the project goals", 
        "📊 Project Overview": "Explore methodologies and frameworks",
        "📈 Interactive Visualizations": "Explore interactive HR data insights", 
        "📊 Power BI Dashboards": "View advanced analytics dashboards",
        "🔮 ML Predictions": "Predict employee turnover risk"
    }
    
    # Create radio buttons but style them better with custom HTML
    menu = st.radio("", list(nav_options.keys()), label_visibility="collapsed")
    
    # Show description of selected option
    st.markdown(f'<div class="nav-description">{nav_options[menu]}</div>', unsafe_allow_html=True)
    
    # Separator
    st.markdown('<hr style="border-top: 1px solid rgba(255, 255, 255, 0.2); margin: 15px 0;">', unsafe_allow_html=True)
    
    # Resources section
    st.markdown('<p style="font-size:18px; font-weight:500; color:white; margin-top:20px;">Resources</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📂 GitHub", use_container_width=True):
            st.markdown("[View Repository](https://github.com/Jotis86/People-Analytics-Project)")
    
    with col2:
        if st.button("📚 Docs", use_container_width=True):
            st.markdown("[Documentation](https://github.com/Jotis86/People-Analytics-Project/blob/main/README.md)")
    
    # Footer
    st.markdown("""
    <div class="sidebar-footer">
        <p>People Analytics Project</p>
        <p>Version 1.0.0</p>
        <p>© 2023</p>
    </div>
    """, unsafe_allow_html=True)


# Load data for visualizations
df = load_data()


# Secciones del menú
if menu == "🏠 Home & Objectives":
    # Introduction with visual cards - improved text contrast
    st.markdown("""
    <div style="display: flex; margin-bottom: 25px;">
        <div style="flex: 2; background: linear-gradient(135deg, #EBF5FB 0%, #D4E6F1 100%); border-radius: 10px; padding: 20px; margin-right: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #0D47A1; text-align: center; margin-bottom: 20px; border-bottom: 2px solid #0D47A1; padding-bottom: 10px;">
                📊 Interactive Analytics Platform
            </h3>
            <p style="font-size: 16px; line-height: 1.6; color: #333;">
                This comprehensive dashboard provides powerful visualization and analysis tools for workforce data, enabling HR professionals and managers to make informed decisions.
            </p>
        </div>
        <div style="flex: 1; background: linear-gradient(135deg, #E8F8F5 0%, #D1F2EB 100%); border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="color: #00695C; text-align: center; margin-bottom: 20px; border-bottom: 2px solid #00695C; padding-bottom: 10px;">
                🎯 Our Mission
            </h3>
            <p style="font-size: 16px; line-height: 1.6; text-align: center; color: #333;">
                Transform HR data into actionable insights to optimize workforce performance and employee satisfaction.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features section with icons and visual elements - fixed text overflow
    st.markdown("<h3 style='text-align: center; color: #3498DB; margin-top: 10px;'>🔎 Key Analysis Features</h3>", unsafe_allow_html=True)
    
    feature_cols = st.columns(5)
    
    features = [
        {"icon": "🔄", "title": "Retention Analysis", "color": "#3498DB"},
        {"icon": "📈", "title": "Performance Insights", "color": "#9B59B6"},
        {"icon": "😊", "title": "Satisfaction Metrics", "color": "#2ECC71"},
        {"icon": "📚", "title": "Training Impact", "color": "#F39C12"},
        {"icon": "📉", "title": "Absenteeism", "color": "#E74C3C"}
    ]
    
    for i, col in enumerate(feature_cols):
        with col:
            feature = features[i]
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 15px; height: 140px; text-align: center; 
                        border-top: 5px solid {feature['color']}; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div style="font-size: 2.5rem; margin-bottom: 15px;">{feature['icon']}</div>
                <h4 style="color: {feature['color']}; margin: 0; font-size: 16px;">{feature['title']}</h4>
            </div>
            """, unsafe_allow_html=True)
    
    # Strategic objectives with progress indicators
    st.markdown("<h3 style='text-align: center; color: #E67E22; margin-top: 30px;'>🚀 Strategic Objectives</h3>", unsafe_allow_html=True)
    
    objectives = [
        {"title": "Data-driven HR Decisions", "icon": "📊", "progress": 85, "color": "#3498DB"},
        {"title": "Identify Retention Factors", "icon": "🔍", "progress": 70, "color": "#9B59B6"},
        {"title": "Optimize Performance", "icon": "📈", "progress": 60, "color": "#2ECC71"},
        {"title": "Enhance Employee Experience", "icon": "🌟", "progress": 75, "color": "#F39C12"},
        {"title": "Strategic Workforce Planning", "icon": "🗓️", "progress": 55, "color": "#E74C3C"}
    ]
    
    obj_cols = st.columns(len(objectives))
    
    for i, col in enumerate(obj_cols):
        with col:
            obj = objectives[i]
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 15px; text-align: center; 
                       box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <div style="font-size: 1.8rem;">{obj['icon']}</div>
                <h4 style="font-size: 13px; height: 36px; display: flex; align-items: center; justify-content: center; color: #333;">
                    {obj['title']}
                </h4>
                <div style="background-color: #f0f0f0; border-radius: 10px; height: 8px; margin: 8px 0;">
                    <div style="background-color: {obj['color']}; width: {obj['progress']}%; height: 8px; border-radius: 10px;"></div>
                </div>
                <p style="font-size: 12px; color: {obj['color']}; font-weight: bold;">{obj['progress']}% Complete</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Smaller, more compact CTA
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F5EEF8 0%, #EBF5FB 100%); padding: 12px; border-radius: 8px; 
                text-align: center; margin-top: 25px; width: 60%; margin-left: auto; margin-right: auto;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); border: 1px dashed #3498DB;">
        <h4 style="color: #3498DB; margin: 0 0 5px 0;">Ready to explore the data?</h4>
        <p style="color: #555; margin: 0 0 5px 0; font-size: 14px;">Navigate using the sidebar menu</p>
        <p style="font-size: 1.5rem; margin: 0;">👈</p>
    </div>
    """, unsafe_allow_html=True)



elif menu == "📊 Project Overview":
    st.markdown('<p class="section-header">📊 Project Overview</p>', unsafe_allow_html=True)
    
    # Create a submenu within Project Overview
    overview_submenu = st.radio(
        "Select overview section:",
        ["Project Structure", "Results", "Key Metrics", "Conclusions"],
        horizontal=True
    )
    
    if overview_submenu == "Project Structure":
        # Display project diagram
        #st.image(dashboard_image_path, use_container_width=True)
        
        # Use tabs for better organization
        tab1, tab2, tab3 = st.tabs(["Functionality", "Tools Used", "Process"])
        
        with tab1:
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
                #st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("""
                ### Power BI
                
                - 📊 Interactive dashboards
                - 📈 Customizable visuals
                - 🔄 Real-time filtering
                - 🔗 Data relationships
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                #st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("""
                ### Python Analysis
                
                - 🧹 Pandas data cleaning
                - 📊 Matplotlib visualization
                - 📈 Seaborn statistical plots
                - 🔢 NumPy calculations
                """)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with tab3:
            #st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Development Process
            
            1. **Data Extraction** from HR systems
            2. **Cleaning & Transformation** to prepare for analysis
            3. **Exploratory Analysis** to identify patterns
            4. **Dashboard Creation** for interactive exploration
            5. **Metric Development** to track key indicators
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    elif overview_submenu == "Results":
        st.markdown('<p class="section-header">📈 Key Results</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            #st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Power BI Analysis
            
            - 📊 **Custom KPI calculations** for retention, satisfaction and performance
            - 📏 **DAX calculated measures** for advanced metric analysis
            - ➕ **Calculated columns** for enhanced categorization
            - 🔍 **Dynamic filtering** for focused analysis
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
    
    elif overview_submenu == "Key Metrics":
        st.markdown('<p class="section-header">📏 Key HR Metrics</p>', unsafe_allow_html=True)
        
        # Display metrics in cards
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
            #st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📉 Absenteeism")
            
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
            #st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📊 Performance")
            
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
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
            #st.markdown('<div class="card">', unsafe_allow_html=True)
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
    
    elif overview_submenu == "Conclusions":
        st.markdown('<p class="section-header">🎯 Project Conclusions</p>', unsafe_allow_html=True)
        
        # Key Findings with more visual formatting
        #st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #1E88E5;'>💡 Key Findings</h3>", unsafe_allow_html=True)
        
        # Two columns for findings to make it more compact
        f_col1, f_col2 = st.columns(2)
        
        with f_col1:
            st.markdown("""
            ✅ **Employee Retention Factors**
            - Compensation is a key driver
            - Management quality matters
            - Career development opportunities
            
            ✅ **Performance Patterns**
            - Strong correlation with training
            - Higher investments = better outcomes 
            - Performance varies by department
            """)
        
        with f_col2:
            st.markdown("""
            ✅ **Department-Level Insights**
            - Significant variations in engagement
            - Performance differs across teams
            - Turnover rates vary significantly
            
            ✅ **Satisfaction Drivers**
            - NPS analysis revealed key factors
            - Work-life balance is critical
            - Recognition affects engagement
            """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recommendations section with visual indicators
        #st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #FF5722;'>🚀 Recommendations</h3>", unsafe_allow_html=True)
        
        rec_cols = st.columns(4)
        
        with rec_cols[0]:
            st.markdown("""
            <div style='text-align: center;'>
            <span style='font-size: 2.5rem;'>📚</span>
            <h4>Targeted Training</h4>
            <p>Increase training in departments with lower performance scores</p>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_cols[1]:
            st.markdown("""
            <div style='text-align: center;'>
            <span style='font-size: 2.5rem;'>🔄</span>
            <h4>Retention Strategy</h4>
            <p>Focus efforts on departments with high turnover rates</p>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_cols[2]:
            st.markdown("""
            <div style='text-align: center;'>
            <span style='font-size: 2.5rem;'>🌟</span>
            <h4>Engagement Initiatives</h4>
            <p>Address low NPS scores with targeted programs</p>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_cols[3]:
            st.markdown("""
            <div style='text-align: center;'>
            <span style='font-size: 2.5rem;'>📊</span>
            <h4>Continuous Monitoring</h4>
            <p>Implement ongoing analytics for proactive management</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Future Directions with visual timeline
        #st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #4CAF50;'>🔮 Future Directions</h3>", unsafe_allow_html=True)
        
        # Progress bar to visualize implementation timeline
        st.markdown("<p style='text-align: center;'>Implementation Roadmap</p>", unsafe_allow_html=True)
        st.progress(25)
        
        future_cols = st.columns(4)
        
        with future_cols[0]:
            st.markdown("""
            <div style='text-align: center; border-top: 4px solid #4CAF50;'>
            <p style='color: #4CAF50; font-weight: bold;'>Phase 1</p>
            <span style='font-size: 2rem;'>🔄</span>
            <p>Data Integration & Centralization Platform</p>
            </div>
            """, unsafe_allow_html=True)
        
        with future_cols[1]:
            st.markdown("""
            <div style='text-align: center; border-top: 4px solid #2196F3;'>
            <p style='color: #2196F3; font-weight: bold;'>Phase 2</p>
            <span style='font-size: 2rem;'>⏱️</span>
            <p>Real-Time Analytics dashboards</p>
            </div>
            """, unsafe_allow_html=True)
        
        with future_cols[2]:
            st.markdown("""
            <div style='text-align: center; border-top: 4px solid #FFC107;'>
            <p style='color: #FFC107; font-weight: bold;'>Phase 3</p>
            <span style='font-size: 2rem;'>🔌</span>
            <p>Integration with HRIS systems</p>
            </div>
            """, unsafe_allow_html=True)
        
        with future_cols[3]:
            st.markdown("""
            <div style='text-align: center; border-top: 4px solid #9C27B0;'>
            <p style='color: #9C27B0; font-weight: bold;'>Phase 4</p>
            <span style='font-size: 2rem;'>📈</span>
            <p>Expanded Metrics for deeper insights</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Signature
        st.markdown("""
        <div style="text-align: center; margin-top: 30px; color: #555;">
        <p>Project developed by Jotis with love</p>
        </div>
        """, unsafe_allow_html=True)

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

# Add the new section at the end of your app, with the other menu sections
elif menu == "🔮 ML Predictions":
    #st.markdown('<p class="section-header">🔮 Machine Learning Predictions</p>', unsafe_allow_html=True)
    
    # Notify user we're using a rule-based model
    #st.info("Using a rule-based prediction model based on HR research and best practices")
    
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #2E86C1; margin-bottom: 20px;">
        <h3 style="color: #2E86C1; margin-top: 0;">Employee Turnover Prediction</h3>
        <p>This tool predicts the likelihood of an employee leaving the company based on various HR factors.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create interface for prediction inputs
    st.markdown("### Enter Employee Information")
    
    # Use tabs to organize the form
    tab1, tab2 = st.tabs(["Employee Details", "Contract & Compensation"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            negligencias = st.number_input("Negligencias/Sanciones", 0, 10, 0, help="Number of sanctions or documented policy violations")
            year_birth = st.number_input("Año de Nacimiento", 1950, 2000, 1985)
            edad = st.number_input("Edad", 20, 70, 35)
            nuevas_contrataciones = st.selectbox("¿Es nueva contratación?", ["No", "Sí"])
            nuevas_contrataciones = 1 if nuevas_contrataciones == "Sí" else 0
            
        with col2:
            exp_previa = st.number_input("Experiencia previa (meses)", 0, 240, 36, help="Previous work experience before joining the company")
            fecha_inicio = st.date_input("Fecha inicio de contrato", 
                                       date(2015, 1, 1), 
                                       min_value=date(2000, 1, 1),
                                       max_value=date.today())
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            antig_anios = st.number_input("Antigüedad en años", 0, 30, 3)
            antig_meses = st.number_input("Antigüedad en meses", 0, 11, 6)
            
        with col2:
            salario_inicial = st.number_input("Salario inicial 2020 (€)", 15000, 100000, 30000, step=1000)
            salario_actual = st.number_input("Salario anual actual 2020 (€)", 15000, 150000, 35000, step=1000)
    
    # Prediction section
    st.markdown("### Prediction")
    
    if st.button("Predict Turnover Risk", key="predict_button"):
        try:
            # Calculate derived metrics
            total_tenure = antig_anios + (antig_meses / 12)
            salary_growth = (salario_actual - salario_inicial) / max(1, salario_inicial)
            salary_growth_annual = salary_growth / max(1, total_tenure)
            today = date.today()
            days_since_hired = (today - fecha_inicio).days
            market_experience = total_tenure + (exp_previa / 12)
            
            # Initialize risk factors dictionary
            risk_factors = {}
            
            # 1. Negligencias/Sanciones - Progressive impact
            if negligencias == 0:
                negligencias_risk = 0
            elif negligencias <= 2:
                negligencias_risk = 0.15 * negligencias  # 0.15 for 1, 0.3 for 2
            elif negligencias <= 5:
                negligencias_risk = 0.3 + 0.05 * (negligencias - 2)  # 0.35 to 0.45
            else:
                negligencias_risk = 0.45 + 0.07 * (negligencias - 5)  # 0.52 to 0.8
            risk_factors["Negligencias"] = negligencias_risk
            
            # 2. Salary Growth - Inverse relationship with diminishing returns
            # If growth is negative or zero, high risk
            if salary_growth <= 0:
                salary_risk = 0.6
            else:
                # Exponential decay - less growth = higher risk
                salary_risk = 0.6 * math.exp(-5 * salary_growth)
            risk_factors["Crecimiento Salarial"] = salary_risk
            
            # 3. Tenure - Higher risk for new employees, decreases over time
            # First year is highest risk
            if total_tenure < 1:
                tenure_risk = 0.7 - (0.4 * total_tenure)  # 0.7 at 0 years to 0.3 at 1 year
            elif total_tenure < 3:
                tenure_risk = 0.3 - (0.1 * (total_tenure - 1))  # 0.3 at 1 year to 0.1 at 3 years
            else:
                tenure_risk = 0.1 * math.exp(-0.2 * (total_tenure - 3))  # Slow decrease after 3 years
            risk_factors["Antigüedad"] = tenure_risk
            
            # 4. Age - U-shaped risk (young and older have higher risk)
            if edad < 30:
                # Young employees - higher risk, decreases with age
                age_risk = 0.5 - ((edad - 20) * 0.03)  # 0.5 at 20yo to 0.2 at 30yo
            elif edad < 50:
                # Mid-career - lowest risk
                age_risk = 0.2 - ((edad - 30) * 0.005)  # 0.2 at 30yo to 0.1 at 50yo
            else:
                # Approaching retirement - increasing risk
                age_risk = 0.1 + ((edad - 50) * 0.015)  # 0.1 at 50yo to 0.4 at 70yo
            risk_factors["Edad"] = age_risk
            
            # 5. New hire status - binary factor
            new_hire_risk = 0.3 if nuevas_contrataciones == 1 else 0
            risk_factors["Nueva Contratación"] = new_hire_risk
            
            # 6. Experience vs. Compensation - Market value alignment
            # Calculate expected salary based on experience (simple model)
            expected_base = 25000
            expected_growth = 1000 * market_experience  # €1000 per year of experience
            expected_salary = expected_base + expected_growth
            
            # Risk is higher if actual salary is below expected
            salary_ratio = salario_actual / max(1, expected_salary)
            if salary_ratio >= 1.1:
                # Paid above market - low risk
                market_risk = 0.05
            elif salary_ratio >= 0.9:
                # Paid around market rate - moderate risk
                market_risk = 0.15
            elif salary_ratio >= 0.8:
                # Paid somewhat below market - higher risk
                market_risk = 0.3
            else:
                # Paid significantly below market - highest risk
                market_risk = 0.5
            risk_factors["Alineación Salarial"] = market_risk
            
            # 7. Recent hires with high previous experience - adjustment risk
            if total_tenure < 2 and exp_previa > 60:  # Less than 2 years tenure but >5 years prior experience
                adjustment_risk = 0.25
            else:
                adjustment_risk = 0
            risk_factors["Adaptación"] = adjustment_risk
            
            # Define factor weights - MUST SUM TO 1.0
            weights = {
                "Negligencias": 0.25,
                "Crecimiento Salarial": 0.15,
                "Antigüedad": 0.20,
                "Edad": 0.10,
                "Nueva Contratación": 0.10,
                "Alineación Salarial": 0.15,
                "Adaptación": 0.05
            }
            
            # Calculate weighted risk score
            weighted_risks = {}
            risk_score = 0
            
            for factor, value in risk_factors.items():
                weighted_value = value * weights[factor]
                weighted_risks[factor] = weighted_value
                risk_score += weighted_value
            
            # Apply final calibration - ensure sensible distribution of predictions
            # Cap at 90% maximum risk
            risk_score = min(0.9, risk_score)
            
            # Decision threshold
            threshold = 0.35
            prediction = 1 if risk_score > threshold else 0
            probability = [1 - risk_score, risk_score]
            
            # Display prediction
            if prediction == 1:
                risk_level = "High"
                risk_color = "#E74C3C"
                if risk_score > 0.6:
                    risk_message = "This employee is at very high risk of leaving. Immediate action recommended."
                else:
                    risk_message = "This employee is at high risk of leaving."
            else:
                if risk_score > 0.25:
                    risk_level = "Moderate"
                    risk_color = "#F39C12"
                    risk_message = "This employee has some turnover risk factors that should be monitored."
                else:
                    risk_level = "Low"
                    risk_color = "#2ECC71"
                    risk_message = "This employee is likely to stay with the company."
            
            # Display result
            st.markdown(f"""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; 
                        border-left: 5px solid {risk_color}; margin-top: 20px; width: 100%;"> <!-- Added width: 70% -->
                <h3 style="color: {risk_color}; margin-top: 0;">Turnover Risk: {risk_level}</h3>
                <p style="color: #333;">{risk_message}</p> <!-- Added color to ensure visibility -->
                <p style="color: #333;">Probability of leaving: <b>{risk_score:.2%}</b></p> <!-- Added color -->
            </div>
            """, unsafe_allow_html=True)
            
            # Create data for visualization based on weighted factors
            chart_data = pd.DataFrame({
                'Factor': list(weighted_risks.keys()),
                'Impact': list(weighted_risks.values())
            })
            
            # Sort by impact (descending to show highest impact factors first)
            chart_data = chart_data.sort_values('Impact', ascending=True)
            
            # Feature importance visualization
            st.markdown("### Key Factors")
            
            # Use a custom color palette based on risk level
            colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(chart_data)))
            
            # Create visualization
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.barh(chart_data['Factor'], chart_data['Impact'], color=colors)
            
            ax.set_title('Factors Influencing Turnover Risk', fontsize=14)
            ax.set_xlabel('Weighted Impact')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.tight_layout()
            
            st.pyplot(fig)
            
            # Show raw factor scores for transparency
            with st.expander("Show detailed factor scores"):
                raw_data = pd.DataFrame({
                    'Factor': list(risk_factors.keys()),
                    'Raw Score': list(risk_factors.values()),
                    'Weight': [weights[f] for f in risk_factors.keys()],
                    'Weighted Impact': list(weighted_risks.values())
                }).sort_values('Weighted Impact', ascending=False).reset_index(drop=True)
                
                st.table(raw_data)
            
            # Recommendations based on risk level and factors
            st.markdown("### Recommendations")
            
            # Get top 3 risk factors
            top_factors = chart_data.sort_values('Impact', ascending=False).head(3)['Factor'].tolist()
            
            if prediction == 1:  # High risk
                # Custom recommendations based on top factors
                specific_recs = []
                
                if "Negligencias" in top_factors:
                    specific_recs.append("Address the high number of sanctions or policy violations through coaching and clear expectations")
                
                if "Crecimiento Salarial" in top_factors:
                    specific_recs.append("Review compensation history and consider a market adjustment to salary")
                
                if "Antigüedad" in top_factors:
                    specific_recs.append("Implement targeted retention strategies for employees in their early tenure")
                
                if "Edad" in top_factors:
                    if edad < 30:
                        specific_recs.append("Provide clear career progression paths and development opportunities for younger employees")
                    else:
                        specific_recs.append("Consider flexible work arrangements and recognize experience contributions")
                
                if "Alineación Salarial" in top_factors:
                    specific_recs.append("Conduct a market compensation analysis and adjust if below market rate")
                
                if "Adaptación" in top_factors:
                    specific_recs.append("Check in on job satisfaction and role fit for this experienced new hire")
                
                # Generate recommendations HTML
                rec_items = "".join([f"<li>{rec}</li>" for rec in specific_recs])
                
                st.markdown(f"""
                <div style="background-color: #FDEDEC; padding: 15px; border-radius: 10px; border-left: 5px solid #E74C3C; width: 85%;">
                    <h4 style="color: #E74C3C; margin-top: 0;">Retention Strategies</h4>
                    <ul style="color: #333;"> <!-- Added color to ensure visibility -->
                        {rec_items}
                        <li>Schedule a one-on-one meeting to discuss career aspirations</li>
                        <li>Review overall compensation and benefits package</li>
                        <li>Consider role adjustments to better align with employee strengths</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            elif risk_score > 0.25:  # Moderate risk
                st.markdown("""
                <div style="background-color: #FEF9E7; padding: 15px; border-radius: 10px; border-left: 5px solid #F39C12; width: 85%;">
                    <h4 style="color: #F39C12; margin-top: 0;">Preventive Measures</h4>
                    <ul style="color: #333;"> <!-- Added color to ensure visibility -->
                        <li>Schedule regular check-ins to gauge job satisfaction</li>
                        <li>Ensure competitive compensation based on market rates</li>
                        <li>Provide learning and development opportunities</li>
                        <li>Recognize contributions and achievements</li>
                        <li>Consider potential career growth paths within the organization</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:  # Low risk
                st.markdown("""
                <div style="background-color: #EAFAF1; padding: 15px; border-radius: 10px; border-left: 5px solid #2ECC71; width: 85%;">
                    <h4 style="color: #2ECC71; margin-top: 0;">Engagement Strategies</h4>
                    <ul style="color: #333;"> <!-- Added color to ensure visibility -->
                        <li>Continue regular feedback and recognition</li>
                        <li>Identify opportunities for taking on new challenges</li>
                        <li>Consider for mentoring or knowledge-sharing roles</li>
                        <li>Involve in strategic initiatives and planning</li>
                        <li>Continue to review compensation periodically to maintain market competitiveness</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            st.markdown("Try adjusting the input values or check if all the required fields are filled correctly.")