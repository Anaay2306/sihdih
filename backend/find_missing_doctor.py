#!/usr/bin/env python3
"""
Find the case missing doctor information
"""

from ai_patient_database import ai_patient_db

def find_missing_doctor_info():
    """Find cases missing doctor information"""
    print("=== Finding Cases Missing Doctor Information ===\n")
    
    missing_cases = []
    
    for i, case in enumerate(ai_patient_db.patient_cases):
        if not case.get('doctor_name') or not case.get('doctor_quote') or not case.get('treatment'):
            missing_cases.append({
                'index': i,
                'diagnosis': case.get('diagnosis', 'Unknown'),
                'missing_doctor_name': not case.get('doctor_name'),
                'missing_doctor_quote': not case.get('doctor_quote'),
                'missing_treatment': not case.get('treatment')
            })
    
    if missing_cases:
        print(f"Found {len(missing_cases)} cases missing doctor information:")
        for case in missing_cases:
            print(f"\nCase {case['index']}: {case['diagnosis']}")
            if case['missing_doctor_name']:
                print("  - Missing doctor_name")
            if case['missing_doctor_quote']:
                print("  - Missing doctor_quote")
            if case['missing_treatment']:
                print("  - Missing treatment")
    else:
        print("✅ All cases have complete doctor information!")
    
    return missing_cases

if __name__ == "__main__":
    find_missing_doctor_info()
