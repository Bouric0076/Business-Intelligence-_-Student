# Banking Business Intelligence & Analytics Dashboard

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://banking-enterprise-analysis.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/bouric0076/Business-Intelligence-_-Student.svg)](https://github.com/bouric0076/Business-Intelligence-_-Student/commits/main)

**Live Dashboard**: [https://banking-enterprise-analysis.streamlit.app/](https://banking-enterprise-analysis.streamlit.app/)

*Data-driven banking insights for strategic decision-making*

</div>

---

## Project Overview

This Business Intelligence project applies advanced analytics to optimize banking operations through customer behavior analysis, marketing performance evaluation, and credit risk assessment. Built with Streamlit, it provides interactive dashboards for data-driven decision making.

### Key Objectives
- Identify high-value customer segments for targeted marketing
- Detect key drivers of credit default risk  
- Quantify financial impact of BI-driven strategies
- Provide actionable recommendations for sustainable growth

### Financial Impact Summary
| Metric | Value |
|--------|-------|
| **Projected Annual Benefit** | ~$5,000,000 |
| **ROI Payback Period** | ~3.5 months |
| **3-Year NPV** | ~$12.4 million |

---

## Quick Start

### Live Demo
Access the fully interactive dashboard: **[Banking BI Dashboard](https://banking-enterprise-analysis.streamlit.app/)**

### Local Development
```bash
# Clone repository
git clone https://github.com/bouric0076/Business-Intelligence-_-Student.git
cd Business-Intelligence-_-Student

# Install dependencies
pip install -r requirements.txt

# Launch dashboard
streamlit run interactive_dashboard.py
```

---

## Dashboard Features

### Customer Analytics
- **Segmentation Analysis**: Demographic and behavioral customer clustering
- **Campaign Performance**: Marketing ROI and conversion tracking
- **Risk Assessment**: Credit default prediction and scoring

### Interactive Visualizations
- **Real-time Filtering**: Dynamic data exploration
- **Multi-dimensional Analysis**: Cross-segment performance comparison
- **Financial Modeling**: ROI and NPV calculations

---

## Technical Architecture

### Technology Stack
- **Frontend**: Streamlit 1.51.0
- **Data Processing**: Pandas 2.3.3, NumPy 2.3.5
- **Visualization**: Plotly 6.5.0, Matplotlib 3.10.7, Seaborn 0.13.2
- **Machine Learning**: Scikit-learn 1.7.2, SciPy 1.16.3
- **Deployment**: Streamlit Cloud (Linux-compatible)

### Data Sources
- **Primary Dataset**: 45,211 customer records with 21 features
- **Data Types**: Demographics, campaign responses, credit utilization, financial metrics
- **Data Quality**: Cleaned and validated for analysis

---

## Repository Structure

```
Business-Intelligence-_-Student/
│
├── interactive_dashboard.py          # Main Streamlit application
├── PRESENTATION_CONTENT.md          # Project presentation materials
├── requirements.txt                   # Python dependencies
├── requirements-deploy.txt           # Linux-compatible deployment deps
│
├── data/                            # Dataset storage
│   └── bank_data.csv                # Primary customer dataset
│
├── notebooks/                       # Jupyter analysis notebooks
├── scripts/                         # Python utility scripts
│
├── visuals/                         # Generated visualizations
├── reports/                         # Project documentation
│
└── README.md                        # This file
```

---

## Key Insights Discovered

### High-Value Customer Segments
- **Retired customers**: Higher campaign conversion rates
- **Mobile-contacted clients**: Improved engagement metrics
- **October campaigns**: Seasonal performance peaks

### Risk Indicators
- **Credit utilization >80%**: Strongly correlated with default risk
- **Customers under 30**: Higher default probability
- **Data-driven targeting**: 3x more effective than intuition-based approaches

---

## Deployment & Development

### Deployment Status
- **Live Production**: Streamlit Cloud deployment active
- **Cross-platform**: Linux-compatible requirements configured
- **Auto-deployment**: GitHub integration enabled

### Development Setup
```bash
# Development dependencies
pip install -r requirements.txt

# Production deployment (Linux)
pip install -r requirements-deploy.txt

# Run locally
streamlit run interactive_dashboard.py --server.port 8501
```

---

## GitHub Activity & Contributions

### Repository Statistics
<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=bouri&theme=default&hide_border=false&include_all_commits=true&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=bouri&theme=default&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

</div>

### Commit Activity & Streaks
<div align="center">

![GitHub Streak](https://streak-stats.demolab.com/?user=bouri&theme=default&hide_border=false)

</div>

### Project Contributors
<div align="center">

![Contributors](https://contrib.rocks/image?repo=bouri/Business-Intelligence-_-Student&max=100&columns=12)

</div>

### Recent Development Activity
<!--START_SECTION:activity-->
1. **Deployment Fix**: Resolved Streamlit deployment issues with Linux-compatible requirements
2. **Dashboard Enhancement**: Updated interactive visualizations and filtering capabilities  
3. **Dependency Management**: Separated Windows/Linux requirements for cross-platform compatibility
4. **Data Processing**: Optimized customer segmentation and risk assessment algorithms
<!--END_SECTION:activity-->



---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


- **Live Dashboard**: [https://banking-enterprise-analysis.streamlit.app/](https://banking-enterprise-analysis.streamlit.app/)
- **Issues**: [GitHub Issues](https://github.com/bouri/Business-Intelligence-_-Student/issues)
- **Discussions**: [GitHub Discussions](https://github.com/bouri/Business-Intelligence-_-Student/discussions)

---

<div align="center">

**[Back to Top](#banking-business-intelligence--analytics-dashboard)**

*Made with Streamlit and Python*

</div>
