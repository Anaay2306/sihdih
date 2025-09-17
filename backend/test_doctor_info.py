#!/usr/bin/env python3
"""
Test script to verify doctor information is showing in patient cases
"""

from ai_patient_database import ai_patient_db

def test_doctor_information():
    """Test that patient cases include doctor names and quotes"""
    print("=== Testing Doctor Information in Patient Cases ===\n")
    
    # Test case 1: Fever symptoms
    symptoms = ["fever", "cough", "headache"]
    result = ai_patient_db.get_ai_recommendations(
        symptoms=symptoms,
        patient_age=45,
        patient_gender="male"
    )
    
    print("Test 1: Fever Symptoms")
    print(f"Symptoms: {symptoms}")
    print(f"Similar Cases Found: {len(result['similar_cases'])}")
    
    if result['similar_cases']:
        for i, case in enumerate(result['similar_cases'][:3]):
            print(f"\n--- Case {i+1}: {case['diagnosis']} ---")
            print(f"Doctor Name: {case.get('doctor_name', 'NOT FOUND')}")
            print(f"Doctor Quote: {case.get('doctor_quote', 'NOT FOUND')}")
            print(f"Treatment: {case.get('treatment', 'NOT FOUND')}")
            print(f"AI Cure: {case.get('ai_cure', 'NOT FOUND')[:100]}...")
            print(f"Similarity Score: {case.get('similarity_score', 0):.2f}")
    
    print("\n" + "="*80)
    
    # Test case 2: Chest pain (emergency)
    symptoms2 = ["severe chest pain", "shortness of breath", "sweating"]
    result2 = ai_patient_db.get_ai_recommendations(
        symptoms=symptoms2,
        patient_age=55,
        patient_gender="male"
    )
    
    print("Test 2: Chest Pain (Emergency)")
    print(f"Symptoms: {symptoms2}")
    print(f"Similar Cases Found: {len(result2['similar_cases'])}")
    
    if result2['similar_cases']:
        for i, case in enumerate(result2['similar_cases'][:3]):
            print(f"\n--- Case {i+1}: {case['diagnosis']} ---")
            print(f"Doctor Name: {case.get('doctor_name', 'NOT FOUND')}")
            print(f"Doctor Quote: {case.get('doctor_quote', 'NOT FOUND')}")
            print(f"Treatment: {case.get('treatment', 'NOT FOUND')}")
            print(f"Emergency Required: {result2.get('emergency_required', False)}")
    
    print("\n" + "="*80)
    
    # Test case 3: Malaria symptoms
    symptoms3 = ["fever", "chills", "muscle aches", "headache"]
    result3 = ai_patient_db.get_ai_recommendations(
        symptoms=symptoms3,
        patient_age=35,
        patient_gender="male"
    )
    
    print("Test 3: Malaria Symptoms")
    print(f"Symptoms: {symptoms3}")
    print(f"Similar Cases Found: {len(result3['similar_cases'])}")
    
    if result3['similar_cases']:
        for i, case in enumerate(result3['similar_cases'][:3]):
            print(f"\n--- Case {i+1}: {case['diagnosis']} ---")
            print(f"Doctor Name: {case.get('doctor_name', 'NOT FOUND')}")
            print(f"Doctor Quote: {case.get('doctor_quote', 'NOT FOUND')}")
            print(f"Treatment: {case.get('treatment', 'NOT FOUND')}")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY:")
    
    total_cases = len(ai_patient_db.patient_cases)
    cases_with_doctor_name = sum(1 for case in ai_patient_db.patient_cases if case.get('doctor_name'))
    cases_with_doctor_quote = sum(1 for case in ai_patient_db.patient_cases if case.get('doctor_quote'))
    cases_with_treatment = sum(1 for case in ai_patient_db.patient_cases if case.get('treatment'))
    
    print(f"Total Cases in Database: {total_cases}")
    print(f"Cases with Doctor Name: {cases_with_doctor_name}")
    print(f"Cases with Doctor Quote: {cases_with_doctor_quote}")
    print(f"Cases with Treatment: {cases_with_treatment}")
    
    if cases_with_doctor_name > 0 and cases_with_doctor_quote > 0:
        print("✅ SUCCESS: Doctor information is now available!")
    else:
        print("❌ ISSUE: Doctor information is still missing from some cases.")

if __name__ == "__main__":
    test_doctor_information()
