import pandas as pd
import numpy as np

# Load both datasets
print("=== BANK MARKETING DATASET ===")
try:
    # Use the actual data file
    bank_data = pd.read_csv('data/Bank_dataset.csv')
    print(f"Shape: {bank_data.shape}")
    print(f"Columns: {list(bank_data.columns)}")
    print(f"Data types:\n{bank_data.dtypes}")
    print(f"Missing values: {bank_data.isnull().sum().sum()}")
    print(f"Duplicated rows: {bank_data.duplicated().sum()}")
    print("\nFirst few rows:")
    print(bank_data.head())
    
    # Show unique values for categorical columns
    print("\n=== BANK DATASET CATEGORICAL VARIABLES ===")
    categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'y']
    for col in categorical_cols:
        if col in bank_data.columns:
            print(f"{col}: {bank_data[col].unique()}")
    
except Exception as e:
    print(f"Error loading Bank_dataset.csv: {e}")

print("\n" + "="*50)
print("=== CREDIT DEFAULT DATASET ===")
try:
    credit_data = pd.read_csv('data/credit_default_clean.csv')
    print(f"Shape: {credit_data.shape}")
    print(f"Columns: {list(credit_data.columns)}")
    print(f"Data types:\n{credit_data.dtypes}")
    print(f"Missing values: {credit_data.isnull().sum().sum()}")
    print(f"Duplicated rows: {credit_data.duplicated().sum()}")
    print("\nFirst few rows:")
    print(credit_data.head())
    
    # Show target variable distribution
    print(f"\nTarget variable distribution:")
    print(credit_data['default payment next month'].value_counts())
    
except Exception as e:
    print(f"Error loading credit_default_clean.csv: {e}")

print("\n" + "="*50)
print("=== COMPREHENSIVE DUAL-DATASET ANALYSIS STRATEGY ===")
print("\n1. BANK MARKETING DATASET - Campaign Effectiveness Analysis:")
print("   - Customer demographics and campaign response")
print("   - Marketing channel effectiveness")
print("   - Term deposit subscription patterns")
print("   - Campaign cost-effectiveness metrics")

print("\n2. CREDIT DEFAULT DATASET - Risk Assessment Analysis:")
print("   - Credit risk profiling and default prediction")
print("   - Customer financial behavior patterns")
print("   - Payment history and credit utilization")
print("   - Risk-based customer segmentation")

print("\n3. INTEGRATED BUSINESS INTELLIGENCE INSIGHTS:")
print("   - Cross-reference marketing effectiveness with credit risk")
print("   - Identify high-value, low-risk customer segments")
print("   - Optimize marketing campaigns based on risk profiles")
print("   - Develop customer lifetime value models")
print("   - Create comprehensive customer 360-degree view")

print("\n4. EPIC STORYTELLING FRAMEWORK APPLICATION:")
print("   - Explain: Banking enterprise challenges in customer acquisition and risk management")
print("   - Problem: Balancing marketing effectiveness with credit risk assessment")
print("   - Insight: Data-driven customer segmentation and campaign optimization")
print("   - Conclusion: Strategic recommendations for integrated marketing and risk management")