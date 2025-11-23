#!/usr/bin/env python3
"""
Generate Executive Summary Report for Banking BI Analysis
Uses the report utilities to create comprehensive business intelligence summary
"""

import sys
import os
sys.path.append('scripts')

from report_utils import BankingReportGenerator

def main():
    """Generate the complete executive summary report"""
    print("BANKING ENTERPRISE INTELLIGENCE: EXECUTIVE REPORT GENERATOR")
    print("="*70)
    
    try:
        # Initialize report generator
        generator = BankingReportGenerator(output_dir='report')
        
        # Generate complete report
        success = generator.generate_complete_report()
        
        if success:
            print("\nEXECUTIVE REPORT GENERATED SUCCESSFULLY!")
            print("\nGenerated Files:")
            print("   - report/executive_summary_report.md")
            print("   - report/executive_dashboard.png")
            print("\nReport Contents:")
            print("   - Executive Summary with Key KPIs")
            print("   - Strategic Recommendations")
            print("   - Financial Impact Projections")
            print("   - Implementation Roadmap")
            print("   - Visual Executive Dashboard")
            print("\nNext Steps:")
            print("   1. Review executive_summary_report.md")
            print("   2. Share dashboard with stakeholders")
            print("   3. Begin implementation of Phase 1 recommendations")
            print("   4. Schedule follow-up analysis in 30 days")
        else:
            print("\nError generating report. Check data files and try again.")
            
    except Exception as e:
        print(f"\nError: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)