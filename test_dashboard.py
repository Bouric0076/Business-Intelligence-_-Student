#!/usr/bin/env python3
"""
Test script for the interactive dashboard
Verifies that all components load correctly
"""

import sys
import os
sys.path.append('scripts')

def test_dashboard():
    """Test dashboard functionality"""
    print("🧪 Testing Interactive Dashboard Components...")
    
    try:
        # Test data loading
        from report_utils import BankingReportGenerator
        print("✅ Report utilities imported successfully")
        
        # Test data loading
        generator = BankingReportGenerator()
        data = generator.load_analysis_data()
        
        if data:
            print("✅ Data loading successful")
            print(f"   - Marketing records: {len(data['bank_marketing']):,}")
            print(f"   - Credit records: {len(data['credit_default']):,}")
            print(f"   - Conversion rate: {data['marketing_conversion']:.1%}")
            print(f"   - Default rate: {data['credit_default_rate']:.1%}")
        else:
            print("❌ Data loading failed")
            return False
            
        # Test dashboard import
        try:
            import interactive_dashboard
            print("✅ Interactive dashboard imported successfully")
        except Exception as e:
            print(f"❌ Dashboard import failed: {e}")
            return False
            
        print("\n🎉 All tests passed! Dashboard is ready for use.")
        print("\n📋 To start the dashboard:")
        print("   streamlit run interactive_dashboard.py")
        print("\n📊 Dashboard features:")
        print("   - EPIC storytelling framework (4 sections)")
        print("   - Interactive visualizations")
        print("   - Real-time data filtering")
        print("   - Professional presentation layout")
        print("   - 10-minute presentation optimized")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_dashboard()
    sys.exit(0 if success else 1)