#!/usr/bin/env python3
"""
Test the improved AI symptom analysis with various symptom combinations
"""

from ai_patient_database import ai_patient_db

def test_symptom_combinations():
    """Test various symptom combinations to see improved matching"""
    
    test_cases = [
        {
            "name": "Common symptoms with aliases",
            "symptoms": ["stomach pain", "feeling sick", "temperature"],
            "age": 25,
            "expected_improvement": "Should match gastroenteritis with normalized symptoms"
        },
        {
            "name": "Vague symptoms",
            "symptoms": ["tiredness", "weakness"],
            "age": 40,
            "expected_improvement": "Should provide general health advice"
        },
        {
            "name": "Single symptom",
            "symptoms": ["headache"],
            "age": 30,
            "expected_improvement": "Should provide pain management advice"
        },
        {
            "name": "Respiratory symptoms",
            "symptoms": ["cough", "breathing difficulty"],
            "age": 50,
            "expected_improvement": "Should match respiratory conditions"
        },
        {
            "name": "Emergency symptoms",
            "symptoms": ["severe chest pain", "breathlessness"],
            "age": 60,
            "expected_improvement": "Should detect emergency and provide immediate guidance"
        }
    ]
    
    print("=== Testing Improved AI Symptom Analysis ===\n")
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Test {i}: {test_case['name']}")
        print(f"Symptoms: {test_case['symptoms']}")
        print(f"Expected: {test_case['expected_improvement']}")
        
        try:
            result = ai_patient_db.get_ai_recommendations(
                symptoms=test_case["symptoms"],
                patient_age=test_case["age"],
                patient_gender="male"
            )
            
            print(f"✅ Risk Level: {result['risk_level']}")
            print(f"   Confidence: {result['confidence']}")
            print(f"   Conditions: {result['possible_conditions']}")
            print(f"   Emergency Required: {result['emergency_required']}")
            
            if result.get('ai_cure'):
                print(f"   AI Cure: {result['ai_cure'][:100]}...")
            
            if result.get('emergency_signs'):
                print(f"   Emergency Signs: {result['emergency_signs'][:3]}")
            
            print(f"   Similar Cases Found: {len(result['similar_cases'])}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 80)
    
    # Test symptom normalization
    print("\n=== Testing Symptom Normalization ===")
    test_symptoms = [
        ["stomach pain", "stomach ache", "belly pain"],
        ["body ache", "muscle pain", "joint ache"],
        ["running nose", "blocked nose"],
        ["breathlessness", "breathing difficulty"],
        ["loose motions", "loose stools"],
        ["feeling sick", "throwing up"],
        ["temperature", "tiredness", "weakness"]
    ]
    
    for symptoms in test_symptoms:
        normalized = ai_patient_db._normalize_symptoms(symptoms)
        print(f"Original: {symptoms}")
        print(f"Normalized: {normalized}")
        print()

if __name__ == "__main__":
    test_symptom_combinations()
