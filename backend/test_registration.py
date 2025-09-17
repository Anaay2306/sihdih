#!/usr/bin/env python3
"""
Test script to verify registration endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_patient_registration():
    """Test patient registration endpoint"""
    print("Testing Patient Registration...")
    
    patient_data = {
        "user": {
            "name": "Test Patient",
            "email": "test.patient@example.com",
            "password": "testpass123",
            "role": "patient",
            "phone": "+91-9876543210"
        },
        "age": 30,
        "gender": "male",
        "village": "Test Village",
        "blood_group": "O+",
        "medical_history": "No major issues",
        "emergency_contact": "+91-9876543211",
        "allergies": "None"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register/patient", json=patient_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_doctor_registration():
    """Test doctor registration endpoint"""
    print("\nTesting Doctor Registration...")
    
    doctor_data = {
        "user": {
            "name": "Test Doctor",
            "email": "test.doctor@example.com",
            "password": "testpass123",
            "role": "doctor",
            "phone": "+91-9876543212"
        },
        "specialization": "General Medicine",
        "license_number": "TEST001",
        "location": "Test Hospital",
        "experience_years": 5
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register/doctor", json=doctor_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_basic_registration():
    """Test basic user registration endpoint"""
    print("\nTesting Basic Registration...")
    
    user_data = {
        "name": "Test User",
        "email": "test.user@example.com",
        "password": "testpass123",
        "role": "patient",
        "phone": "+91-9876543213"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_server_health():
    """Test if server is responding"""
    print("Testing Server Health...")
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"Server Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Server Error: {e}")
        return False

if __name__ == "__main__":
    print("=== Registration Endpoint Tests ===")
    
    if not test_server_health():
        print("❌ Server is not responding!")
        exit(1)
    
    print("✅ Server is running")
    
    # Test all registration endpoints
    patient_success = test_patient_registration()
    doctor_success = test_doctor_registration()
    basic_success = test_basic_registration()
    
    print("\n=== Test Results ===")
    print(f"Patient Registration: {'✅ PASS' if patient_success else '❌ FAIL'}")
    print(f"Doctor Registration: {'✅ PASS' if doctor_success else '❌ FAIL'}")
    print(f"Basic Registration: {'✅ PASS' if basic_success else '❌ FAIL'}")
    
    if all([patient_success, doctor_success, basic_success]):
        print("\n🎉 All registration endpoints are working!")
    else:
        print("\n⚠️  Some registration endpoints have issues.")
