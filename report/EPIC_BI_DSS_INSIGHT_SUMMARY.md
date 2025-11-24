Business Intelligence & DSS – EPIC Insight Summary

Course: BIT 2119
Dataset: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
Objective: Extract insights to support enterprise decision-making through Python analysis using the EPIC storytelling framework.


1. ENGAGE – Business Problem Context

Banks face ongoing challenges balancing customer acquisition and credit risk management. High default rates reduce profitability, while inefficient targeting wastes marketing resources. Data-driven insights can improve portfolio quality, refine customer segmentation, and support more effective decision-making.

This analysis uses the “Credit Card Clients” dataset to explore customer behavior, risk patterns, and drivers of payment performance.

2. PRESENT – Data Overview & Analytical Approach

The dataset includes demographic, financial, and behavioral attributes:

Age, education, marital status

Credit limit, bill amounts, payment history

Previous months’ payment behavior

Python tools applied:

Descriptive statistics

Correlation checks

Trend and distribution analysis

Visual patterns exploration (matplotlib, seaborn)

The goal was to identify variables influencing likelihood of default and extract insights that support enterprise decision making.

3. INTERPRET – Key Insights from Analysis
a. Age and Default Patterns

Younger clients (below 30) show noticeably higher default rates. This demographic appears more vulnerable to financial instability and less consistent in repayment behavior.

b. Credit Utilization Signals Risk

Clients who used more than 80% of their credit limit consistently showed higher default likelihood. This pattern suggests that utilization is a strong behavioral risk indicator.

c. Payment History as a Predictor

Delayed payments across multiple months form a clear early-warning signal. Customers with repeated late payments in the last six months show significantly elevated risk.

d. Bill Amount vs Payment Capability

High bill-to-payment ratios strongly correlate with repayment difficulties. Customers whose monthly bills exceed their stable repayment patterns form a higher-risk segment.

4. CONCLUDE – Decision-Oriented Recommendations
1. Strengthen Risk Screening

Introduce enhanced screening for younger applicants and those with consistently high utilization. Include additional verification or reduced initial credit limits for high-risk groups.

2. Implement Utilization Monitoring

Set automated alerts for customers exceeding 80% utilization and offer financial coaching or payment reminders before risk escalates.

3. Integrate Payment Trend Analysis

Incorporate six-month payment behavior into credit scoring. This allows earlier intervention and more accurate risk assessment.

4. Customize Credit Limits

Segment customers based on historical repayment consistency and adjust credit limits to reduce exposure while maintaining customer satisfaction.

Summary

The analysis demonstrates that age, credit utilization, and payment history are key drivers of default behavior. These insights help the bank optimize risk assessment, improve customer segmentation, and support more informed decision-making. The EPIC framework provides a structured, data-driven foundation for enterprise-level decision support.