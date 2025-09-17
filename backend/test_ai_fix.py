#!/usr/bin/env python3
"""
Test script to verify AI symptom analysis is working after fixes
"""

from ai_patient_database import ai_patient_db

def test_ai_analysis():
    """Test the AI analysis with sample symptoms"""
    print("Testing AI Symptom Analysis...")
    
    # Test case 1: Common cold symptoms
    print("\n=== Test 1: Common Cold Symptoms ===")
    symptoms1 = ["fever", "cough", "fatigue"]
    try:
        result1 = ai_patient_db.get_ai_recommendations(
            symptoms=symptoms1,
            patient_age=30,
            patient_gender="male"
        )
        print(f"✅ Success! Risk Level: {result1['risk_level']}")
        print(f"   Confidence: {result1['confidence']}")
        print(f"   AI Cure: {result1.get('ai_cure', 'Not available')[:100]}...")
        print(f"   Doctor Solution: {result1.get('doctor_solution', 'Not available')[:100]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test case 2: Chest pain (emergency)
    print("\n=== Test 2: Chest Pain (Emergency) ===")
    symptoms2 = ["severe chest pain", "shortness of breath", "sweating"]
    try:
        result2 = ai_patient_db.get_ai_recommendations(
            symptoms=symptoms2,
            patient_age=55,
            patient_gender="male"
        )
        print(f"✅ Success! Risk Level: {result2['risk_level']}")
        print(f"   Emergency Required: {result2['emergency_required']}")
        print(f"   Confidence: {result2['confidence']}")
        print(f"   AI Cure: {result2.get('ai_cure', 'Not available')[:100]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test case 3: Malaria symptoms
    print("\n=== Test 3: Malaria Symptoms ===")
    symptoms3 = ["fever", "chills", "muscle aches", "headache"]
    try:
        result3 = ai_patient_db.get_ai_recommendations(
            symptoms=symptoms3,
            patient_age=35,
            patient_gender="male"
        )
        print(f"✅ Success! Risk Level: {result3['risk_level']}")
        print(f"   Possible Conditions: {result3['possible_conditions']}")
        print(f"   Emergency Signs: {result3.get('emergency_signs', [])}")
        print(f"   Complications: {result3.get('complications', [])}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test database integrity
    print("\n=== Database Integrity Check ===")
    total_cases = len(ai_patient_db.patient_cases)
    valid_cases = 0
    invalid_cases = []
    
    for i, case in enumerate(ai_patient_db.patient_cases):
        if "symptoms" in case and "diagnosis" in case:
            valid_cases += 1
        else:
            invalid_cases.append(f"Case {i}: {case.get('diagnosis', 'Unknown')}")
    
    print(f"Total cases: {total_cases}")
    print(f"Valid cases: {valid_cases}")
    print(f"Invalid cases: {len(invalid_cases)}")
    
    if invalid_cases:
        print("Invalid cases found:")
        for case in invalid_cases:
            print(f"  - {case}")
    else:
        print("✅ All cases are valid!")

if __name__ == "__main__":
    test_ai_analysis()
