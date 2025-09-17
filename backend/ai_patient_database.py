"""
AI Patient Database for Symptom-Treatment Case Matching
Contains Comprehensive patient cases database with AI cures and doctor solutions
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import re

class AIPatientDatabase:
    def __init__(self):
        self.patient_cases = [
            {
                "symptoms": ["fever", "cough", "headache", "body aches"],
                "diagnosis": "Viral Fever",
                "severity": "low",
                "treatment": "Paracetamol 500mg twice daily, plenty of fluids, rest for 5-7 days",
                "ai_cure": "Rest for 5-7 days in a well-ventilated room. Drink plenty of fluids (8-10 glasses daily). Take paracetamol 500mg every 6 hours for fever and body aches. Use steam inhalation for congestion. Avoid contact with others to prevent spread.",
                "doctor_solution": "Symptomatic treatment with paracetamol 500mg twice daily for fever and pain. Adequate rest and hydration. Monitor for complications like pneumonia. Return if breathing difficulties or symptoms worsen after 7 days.",
                "doctor_name": "Dr. Sharma",
                "doctor_quote": "This is a typical viral fever case. The combination of high fever with body ache and dry cough indicates viral infection. Rest and symptomatic treatment will help recovery in 5-7 days.",
                "patient_age": 45,
                "patient_gender": "male",
                "duration": "5-7 days",
                "notes": "Common viral infection, usually self-limiting",
                "complications": ["pneumonia", "dehydration"],
                "prevention": "Hand hygiene, avoid crowded places during outbreaks",
                "emergency_signs": ["difficulty breathing", "persistent high fever", "severe headache"]
            },
            {
                "symptoms": ["abdominal pain", "nausea", "vomiting", "diarrhea"],
                "diagnosis": "Acute Gastroenteritis",
                "severity": "low",
                "treatment": "ORS solution, Metronidazole 400mg thrice daily, light diet",
                "ai_cure": "Rest, drink ORS solution frequently (1 packet in 1 liter water). Eat bland foods (BRAT diet: bananas, rice, applesauce, toast). Avoid dairy and fatty foods for 48 hours. Maintain hand hygiene to prevent spread.",
                "doctor_solution": "Oral rehydration therapy with ORS. Probiotics may help restore gut flora. Antibiotics (Metronidazole 400mg TID) only if bacterial cause confirmed by stool culture. IV fluids if severe dehydration. Monitor electrolyte balance.",
                "doctor_name": "Dr. Patel",
                "doctor_quote": "This appears to be acute gastroenteritis, likely from contaminated food or water. Hydration is key. The antibiotic will help if bacterial. Avoid solid foods for 24 hours.",
                "patient_age": 28,
                "patient_gender": "female",
                "duration": "3-5 days",
                "notes": "Common stomach infection, usually viral",
                "complications": ["severe dehydration", "electrolyte imbalance"],
                "prevention": "Hand hygiene, safe food and water practices, proper food storage",
                "emergency_signs": ["severe dehydration", "blood in stool", "high fever", "severe abdominal pain"]
            },
            {
                "symptoms": ["fever", "cough", "fatigue", "body aches", "sore throat"],
                "diagnosis": "Viral Upper Respiratory Infection",
                "severity": "low",
                "treatment": "Symptomatic treatment with paracetamol, rest, hydration, throat lozenges",
                "ai_cure": "Rest for 7-10 days in a well-ventilated room. Drink 8-10 glasses of warm water daily. Take paracetamol 500mg every 6 hours for fever and body aches. Use throat lozenges for sore throat. Gargle with warm salt water 3 times daily. Avoid contact with others to prevent spread.",
                "doctor_solution": "Symptomatic treatment with adequate rest and hydration. Paracetamol for fever and pain relief. Antiviral medications (Oseltamivir 75mg twice daily) if influenza and within 48 hours of onset. Monitor for complications like pneumonia. Return if breathing difficulties, persistent high fever, or symptoms worsen after 7 days.",
                "doctor_name": "Dr. Family Medicine",
                "doctor_quote": "This appears to be a typical viral upper respiratory infection with constitutional symptoms. We'll focus on symptomatic treatment and monitoring for complications. Most patients recover within a week with supportive care.",
                "patient_age": 35,
                "patient_gender": "male",
                "duration": "5-7 days",
                "notes": "Common viral infection, usually self-limiting",
                "complications": ["pneumonia", "dehydration", "secondary bacterial infection"],
                "prevention": "Annual flu vaccination, frequent hand washing, avoid crowded places during outbreaks",
                "emergency_signs": ["difficulty breathing", "persistent high fever", "severe headache", "chest pain"]
            },
            {
                "symptoms": ["persistent cough", "shortness of breath", "chest pain", "fatigue", "weight loss"],
                "diagnosis": "Pneumonia",
                "severity": "medium",
                "treatment": "Amoxicillin 500mg TID, rest, oxygen therapy if needed",
                "ai_cure": "Immediate medical attention required. Rest completely, increase fluid intake, use humidifier, avoid smoking. Take prescribed antibiotics as directed.",
                "doctor_solution": "Chest X-ray for confirmation. Antibiotic therapy (Amoxicillin 500mg TID or Azithromycin). Hospitalization if severe. Oxygen therapy if needed. Follow-up chest X-ray in 6 weeks.",
                "doctor_name": "Dr. Respiratory",
                "doctor_quote": "The chest X-ray shows consolidation in the right lower lobe consistent with bacterial pneumonia. We'll start empirical antibiotic therapy and monitor oxygen saturation closely.",
                "patient_age": 45,
                "patient_gender": "female",
                "duration": "1-3 weeks",
                "notes": "Bacterial or viral lung infection requiring medical treatment",
                "complications": ["respiratory failure", "sepsis"],
                "prevention": "Pneumococcal vaccination, avoid smoking"
            },
            {
                "symptoms": ["persistent cough", "coughing blood", "chest pain", "shortness of breath", "weight loss", "night sweats"],
                "diagnosis": "Tuberculosis (TB)",
                "severity": "high",
                "treatment": "DOTS regimen: Isoniazid, Rifampin, Ethambutol, Pyrazinamide for 6-9 months",
                "ai_cure": "URGENT: Seek immediate medical attention. This requires specialized treatment. Isolate from others, wear mask, ensure good ventilation in living spaces.",
                "doctor_solution": "Sputum test for AFB, chest X-ray, tuberculin skin test. Anti-TB therapy for 6-9 months (DOTS regimen). Contact tracing and screening. Isolation until non-infectious.",
                "doctor_name": "Dr. TB Specialist",
                "doctor_quote": "The sputum is positive for acid-fast bacilli and chest X-ray shows upper lobe cavitation typical of pulmonary TB. We need to start DOTS immediately and ensure strict isolation until the patient becomes non-infectious.",
                "patient_age": 40,
                "patient_gender": "male",
                "duration": "6-9 months treatment",
                "notes": "Infectious bacterial disease requiring prolonged treatment",
                "complications": ["drug resistance", "spread to other organs"],
                "prevention": "BCG vaccination, avoid crowded spaces"
            },
            # Cardiovascular Conditions
            {
                "symptoms": ["severe chest pain", "shortness of breath", "sweating", "nausea", "dizziness", "pain radiating to arm"],
                "diagnosis": "Myocardial Infarction (Heart Attack)",
                "severity": "critical",
                "treatment": "Emergency PCI, aspirin, beta-blockers, ACE inhibitors",
                "ai_cure": "EMERGENCY: Call ambulance immediately (108/102). Chew aspirin 325mg if not allergic. Sit upright, loosen tight clothing, stay calm. Do NOT drive yourself to hospital.",
                "doctor_solution": "Emergency PCI (angioplasty) or thrombolytic therapy within golden hour. ECG, cardiac enzymes, continuous monitoring. Dual antiplatelet therapy, beta-blockers, ACE inhibitors. Cardiac rehabilitation.",
                "doctor_name": "Dr. Cardio",
                "doctor_quote": "This is a classic presentation of STEMI heart attack. Time is muscle - we need immediate cardiac catheterization. The patient's survival depends on restoring blood flow within the golden hour.",
                "patient_age": 55,
                "patient_gender": "male",
                "duration": "Immediate intervention required",
                "notes": "Life-threatening emergency requiring immediate intervention",
                "complications": ["cardiac arrest", "heart failure", "arrhythmias"],
                "prevention": "Control BP, diabetes, cholesterol. Regular exercise, quit smoking"
            },
            {
                "symptoms": ["high blood pressure", "headache", "dizziness", "blurred vision", "chest pain"],
                "diagnosis": "Hypertensive Crisis",
                "severity": "high",
                "treatment": "IV labetalol, nicardipine, gradual BP reduction, ACE inhibitors",
                "ai_cure": "Seek immediate medical attention. Sit quietly, avoid sudden movements. Do not take extra blood pressure medications without doctor guidance.",
                "doctor_solution": "IV antihypertensive agents (labetalol, nicardipine). Gradual BP reduction over 24-48 hours. Monitor for organ damage. Long-term BP management with ACE inhibitors/ARBs.",
                "doctor_name": "Dr. Hypertension",
                "doctor_quote": "This patient has malignant hypertension with end-organ damage. We need controlled reduction of BP by 25% in the first hour to prevent stroke while avoiding precipitous drops that could cause ischemia.",
                "patient_age": 60,
                "patient_gender": "female",
                "duration": "Hours to days",
                "notes": "Severe hypertension requiring immediate treatment",
                "complications": ["stroke", "heart failure", "kidney damage"],
                "prevention": "Regular BP monitoring, medication compliance, low sodium diet"
            },
            {
                "symptoms": ["palpitations", "irregular heartbeat", "dizziness", "fatigue", "shortness of breath"],
                "diagnosis": "Atrial Fibrillation",
                "severity": "medium",
                "treatment": "Beta-blockers for rate control, anticoagulation with warfarin/DOACs",
                "ai_cure": "Avoid caffeine and alcohol. Practice deep breathing exercises. Seek medical evaluation for proper diagnosis and treatment.",
                "doctor_solution": "ECG for confirmation. Rate control with beta-blockers or calcium channel blockers. Anticoagulation (warfarin/DOACs) for stroke prevention. Consider cardioversion if appropriate.",
                "doctor_name": "Dr. Arrhythmia",
                "doctor_quote": "The ECG shows irregular rhythm with absent P waves characteristic of atrial fibrillation. Given the patient's age and risk factors, we need anticoagulation to prevent stroke and rate control for symptom management.",
                "patient_age": 65,
                "patient_gender": "male",
                "duration": "Chronic condition",
                "notes": "Common arrhythmia requiring anticoagulation",
                "complications": ["stroke", "heart failure"],
                "prevention": "Control underlying conditions, limit alcohol"
            },
            # Gastrointestinal Conditions
            {
                "symptoms": ["severe abdominal pain", "nausea", "vomiting", "fever", "pain in right lower abdomen"],
                "diagnosis": "Acute Appendicitis",
                "severity": "high",
                "treatment": "Emergency laparoscopic appendectomy, pre-operative antibiotics",
                "ai_cure": "URGENT: Seek immediate medical attention. Do not eat or drink anything. Do not take pain medications as they can mask symptoms. Go to emergency room immediately.",
                "doctor_solution": "Emergency appendectomy (laparoscopic preferred). Pre-operative antibiotics. Post-operative monitoring for complications. Early mobilization and gradual diet resumption.",
                "doctor_name": "Dr. Surgeon",
                "doctor_quote": "Classic McBurney's point tenderness with positive Rovsing's sign. The CT scan confirms acute appendicitis without perforation. We need emergency surgery within the next few hours to prevent complications.",
                "patient_age": 25,
                "patient_gender": "male",
                "duration": "Hours to days",
                "notes": "Surgical emergency requiring immediate intervention",
                "complications": ["perforation", "peritonitis", "abscess"],
                "prevention": "No specific prevention, early recognition important"
            },
            {
                "symptoms": ["severe abdominal pain", "vomiting", "bloating", "inability to pass gas", "constipation"],
                "diagnosis": "Intestinal Obstruction",
                "severity": "high",
                "treatment": "Nasogastric decompression, IV fluids, emergency surgery if complete obstruction",
                "ai_cure": "URGENT: Stop eating and drinking. Seek immediate medical attention. This requires emergency treatment.",
                "doctor_solution": "Nasogastric decompression, IV fluids, electrolyte correction. Surgery if complete obstruction or strangulation. Conservative management for partial obstruction.",
                "doctor_name": "Dr. Gastro",
                "doctor_quote": "The CT shows dilated bowel loops with air-fluid levels consistent with small bowel obstruction. Given the patient's surgical history, this is likely adhesional. We'll start conservative management but be ready for surgery if no improvement.",
                "patient_age": 50,
                "patient_gender": "female",
                "duration": "Hours to days",
                "notes": "Surgical emergency if complete obstruction",
                "complications": ["bowel necrosis", "perforation", "sepsis"],
                "prevention": "Avoid adhesion-causing factors, early treatment of hernias"
            },
            {
                "symptoms": ["heartburn", "acid reflux", "chest pain", "difficulty swallowing", "regurgitation"],
                "diagnosis": "Gastroesophageal Reflux Disease (GERD)",
                "severity": "low",
                "treatment": "Proton pump inhibitors (omeprazole), lifestyle modifications, antacids",
                "ai_cure": "Avoid spicy, fatty foods. Eat smaller meals. Don't lie down after eating. Elevate head while sleeping. Take antacids for symptom relief.",
                "doctor_solution": "Proton pump inhibitors (omeprazole) for 8 weeks. Lifestyle modifications. Endoscopy if alarm symptoms. H. pylori testing if indicated.",
                "doctor_name": "Dr. Gastroenterologist",
                "doctor_quote": "Classic GERD symptoms with postprandial heartburn and nocturnal regurgitation. We'll start with PPI therapy and lifestyle modifications. If symptoms persist, we may need endoscopy to rule out complications.",
                "patient_age": 40,
                "patient_gender": "male",
                "duration": "Chronic condition",
                "notes": "Common digestive disorder",
                "complications": ["Barrett's esophagus", "esophageal cancer"],
                "prevention": "Weight management, avoid trigger foods, quit smoking"
            },
            # Neurological Conditions
            {
                "symptoms": ["severe headache", "confusion", "difficulty speaking", "weakness", "numbness"],
                "diagnosis": "Stroke",
                "severity": "critical",
                "treatment": "Emergency thrombolytic therapy (tPA), aspirin, blood pressure management",
                "ai_cure": "EMERGENCY: Call ambulance immediately (108/102). Note the time of symptom onset. Do not drive yourself to hospital.",
                "doctor_solution": "Emergency CT scan or MRI. Thrombolytic therapy within 4.5 hours of symptom onset. Aspirin or other antiplatelets. Blood pressure management. Rehabilitation.",
                "doctor_name": "Dr. Neurologist",
                "doctor_quote": "The patient presents with acute onset left-sided weakness and aphasia consistent with right MCA stroke. We're within the thrombolytic window - we need to get tPA started immediately after ruling out hemorrhage on CT.",
                "patient_age": 60,
                "patient_gender": "male",
                "duration": "Immediate intervention required",
                "notes": "Life-threatening emergency requiring immediate intervention",
                "complications": ["brain damage", "disability", "death"],
                "prevention": "Control BP, diabetes, cholesterol. Regular exercise, quit smoking"
            },
            {
                "symptoms": ["memory loss", "confusion", "difficulty speaking", "mood changes"],
                "diagnosis": "Early Dementia",
                "severity": "medium",
                "treatment": "Cholinesterase inhibitors (donepezil), cognitive training, family support",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Cognitive training and support.",
                "doctor_solution": "Cognitive assessment, family counseling, safety measures, routine establishment. Medications for symptom management (cholinesterase inhibitors).",
                "doctor_name": "Dr. Geriatrician",
                "doctor_quote": "The cognitive assessment shows mild impairment in memory and executive function consistent with early-stage dementia. We'll start donepezil and establish a structured routine with family support.",
                "patient_age": 70,
                "patient_gender": "female",
                "duration": "Chronic condition",
                "notes": "Progressive cognitive decline",
                "complications": ["increased risk of falls", "malnutrition", "infections"],
                "prevention": "Regular cognitive training, social engagement, physical activity"
            },
            {
                "symptoms": ["seizures", "confusion", "difficulty speaking", "weakness", "numbness"],
                "diagnosis": "Epilepsy",
                "severity": "medium",
                "treatment": "Antiepileptic drugs (levetiracetam, phenytoin), lifestyle modifications",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Avoid triggers like stress, lack of sleep.",
                "doctor_solution": "Antiepileptic medications (AEDs). Regular monitoring of medication levels and side effects. Lifestyle modifications (avoid triggers).",
                "doctor_name": "Dr. Epileptologist",
                "doctor_quote": "The EEG shows epileptiform discharges in the temporal region. We'll start levetiracetam as first-line therapy and monitor for seizure control. Patient education about triggers is crucial.",
                "patient_age": 30,
                "patient_gender": "male",
                "duration": "Chronic condition",
                "notes": "Neurological disorder requiring long-term management",
                "complications": ["status epilepticus", "injury from falls"],
                "prevention": "Regular medication adherence, avoid triggers"
            },
            # Musculoskeletal Conditions
            {
                "symptoms": ["severe back pain", "numbness", "weakness", "loss of bladder control"],
                "diagnosis": "Herniated Disc",
                "severity": "medium",
                "treatment": "Physical therapy, NSAIDs, muscle relaxants, surgery if severe",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Avoid heavy lifting, bending.",
                "doctor_solution": "Physical therapy, pain management with NSAIDs or muscle relaxants. Surgery if severe or persistent symptoms.",
                "doctor_name": "Dr. Orthopedic",
                "doctor_quote": "The MRI shows L4-L5 disc herniation with nerve root compression. Given the neurological symptoms, we'll start conservative treatment with physical therapy and consider surgery if no improvement in 6 weeks.",
                "patient_age": 40,
                "patient_gender": "male",
                "duration": "Days to weeks",
                "notes": "Common musculoskeletal condition",
                "complications": ["chronic pain", "permanent nerve damage"],
                "prevention": "Regular exercise, proper lifting techniques"
            },
            {
                "symptoms": ["joint pain", "swelling", "redness", "warmth"],
                "diagnosis": "Rheumatoid Arthritis",
                "severity": "medium",
                "treatment": "DMARDs (methotrexate), biologics, physical therapy, NSAIDs",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Avoid strenuous activities.",
                "doctor_solution": "Disease-modifying antirheumatic drugs (DMARDs). Biologics for severe cases. Physical therapy, lifestyle modifications.",
                "doctor_name": "Dr. Rheumatologist",
                "doctor_quote": "The joint examination shows symmetric polyarthritis with positive rheumatoid factor and anti-CCP antibodies. We'll start methotrexate as first-line DMARD therapy and monitor disease activity closely.",
                "patient_age": 50,
                "patient_gender": "female",
                "duration": "Chronic condition",
                "notes": "Autoimmune disorder requiring long-term management",
                "complications": ["joint damage", "disability"],
                "prevention": "Regular exercise, maintain healthy weight"
            },
            {
                "symptoms": ["muscle weakness", "fatigue", "weight loss", "difficulty swallowing"],
                "diagnosis": "Myasthenia Gravis",
                "severity": "medium",
                "treatment": "Corticosteroids, azathioprine, plasmapheresis, IVIG",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Avoid strenuous activities.",
                "doctor_solution": "Immunosuppressive medications (corticosteroids, azathioprine). Plasmapheresis or IVIG for acute exacerbations.",
                "doctor_name": "Dr. Neurologist",
                "doctor_quote": "The patient shows fatigable weakness with positive acetylcholine receptor antibodies confirming myasthenia gravis. We'll start pyridostigmine and add corticosteroids for immunosuppression.",
                "patient_age": 60,
                "patient_gender": "female",
                "duration": "Chronic condition",
                "notes": "Autoimmune disorder requiring long-term management",
                "complications": ["respiratory failure", "myasthenic crisis"],
                "prevention": "Regular medication adherence, avoid triggers"
            },
            # Skin Conditions
            {
                "symptoms": ["skin rash", "itching", "redness", "scaling"],
                "diagnosis": "Eczema (Atopic Dermatitis)",
                "severity": "low",
                "treatment": "Topical corticosteroids, moisturizers, antihistamines",
                "ai_cure": "Avoid irritants, moisturize regularly. Topical corticosteroids for flare-ups.",
                "doctor_solution": "Topical corticosteroids, oral antihistamines for itching. Phototherapy for severe cases.",
                "doctor_name": "Dr. Dermatologist",
                "doctor_quote": "This is typical atopic dermatitis with characteristic distribution and morphology. We'll start with topical hydrocortisone and emphasize barrier repair with regular moisturizing.",
                "patient_age": 20,
                "patient_gender": "male",
                "duration": "Chronic condition",
                "notes": "Common skin condition",
                "complications": ["skin infections", "asthma"],
                "prevention": "Regular moisturizing, avoid triggers"
            },
            {
                "symptoms": ["skin lesions", "fever", "headache", "fatigue"],
                "diagnosis": "Psoriasis",
                "severity": "medium",
                "treatment": "Topical corticosteroids, vitamin D analogues, methotrexate for severe cases",
                "ai_cure": "Seek medical evaluation for proper diagnosis and treatment. Avoid triggers like stress.",
                "doctor_solution": "Topical corticosteroids, vitamin D analogues. Systemic medications (methotrexate, cyclosporine) for severe cases.",
                "doctor_name": "Dr. Dermatologist",
                "doctor_quote": "These are classic psoriatic plaques with silvery scales on extensor surfaces. We'll start with topical therapy and consider systemic treatment if there's joint involvement or extensive disease.",
                "patient_age": 40,
                "patient_gender": "male",
                "duration": "Chronic condition",
                "notes": "Autoimmune disorder requiring long-term management",
                "complications": ["psoriatic arthritis", "eye problems"],
                "prevention": "Regular exercise, stress management"
            },
            {
                "symptoms": ["skin growths", "itching", "bleeding"],
                "diagnosis": "Skin Cancer",
                "severity": "high",
                "treatment": "Surgical excision, Mohs surgery, chemotherapy for advanced cases",
                "ai_cure": "Seek immediate medical attention. Avoid further sun exposure.",
                "doctor_solution": "Surgical excision, Mohs surgery. Topical or systemic chemotherapy for advanced cases.",
                "doctor_name": "Dr. Oncologist",
                "doctor_quote": "The biopsy confirms squamous cell carcinoma with moderate differentiation. Given the size and location, we'll proceed with Mohs surgery for complete excision with tissue preservation.",
                "patient_age": 60,
                "patient_gender": "male",
                "duration": "Variable",
                "notes": "Life-threatening condition requiring prompt treatment",
                "complications": ["metastasis", "disfigurement"],
                "prevention": "Regular skin checks, sun protection"
            },
            
            # Additional Comprehensive Medical Cases
            
            # Infectious Diseases
            {
                "symptoms": ["fever", "chills", "muscle aches", "headache", "fatigue", "nausea"],
                "diagnosis": "Malaria",
                "severity": "high",
                "treatment": "Artemether-lumefantrine, supportive care, hospitalization if severe",
                "ai_cure": "URGENT: Seek immediate medical attention. Rest completely in bed. Drink plenty of fluids (3-4 liters daily). Take prescribed antimalarial medications exactly as directed without missing doses. Monitor temperature every 4 hours. Use mosquito nets to prevent further bites.",
                "doctor_solution": "Rapid diagnostic test (RDT) and thick/thin blood smears. Artemisinin-based combination therapy: Artemether-lumefantrine 20/120mg (4 tablets twice daily for 3 days). Hospitalization for severe malaria. Monitor for complications: cerebral malaria, acute kidney injury. Glucose monitoring due to hypoglycemia risk.",
                "doctor_name": "Dr. Malhotra",
                "doctor_quote": "This patient shows classic signs of P. falciparum malaria. We need to start ACT immediately and monitor closely for cerebral complications. The fever pattern and travel history are very suggestive.",
                "patient_age": 35,
                "patient_gender": "male",
                "duration": "1-2 weeks with treatment",
                "notes": "Mosquito-borne parasitic infection requiring immediate treatment",
                "complications": ["cerebral malaria", "acute kidney injury", "severe anemia", "respiratory distress"],
                "prevention": "Use insecticide-treated bed nets, indoor residual spraying, antimalarial prophylaxis in endemic areas",
                "emergency_signs": ["confusion", "seizures", "difficulty breathing", "yellow eyes"]
            },
            {
                "symptoms": ["high fever", "severe headache", "muscle pain", "joint pain", "skin rash", "nausea"],
                "diagnosis": "Dengue Fever",
                "severity": "medium",
                "treatment": "Supportive care, fluid management, paracetamol for fever, platelet monitoring",
                "ai_cure": "Rest completely in bed. Drink plenty of fluids: water, ORS, coconut water, fresh fruit juices. Take paracetamol for fever (NEVER aspirin or ibuprofen). Monitor for warning signs: severe abdominal pain, persistent vomiting, bleeding. Seek immediate medical attention if warning signs appear.",
                "doctor_solution": "Supportive care with careful fluid management. Platelet count monitoring (daily CBC). Hospitalization if platelet count <100,000 or warning signs present. IV fluid therapy for plasma leakage. No specific antiviral treatment. Avoid NSAIDs due to bleeding risk.",
                "doctor_name": "Dr. Tropical",
                "doctor_quote": "Classic dengue presentation with the triad of fever, headache, and myalgia. We need to watch the platelet count carefully and monitor for warning signs of dengue hemorrhagic fever, especially around day 4-6 of illness.",
                "patient_age": 28,
                "patient_gender": "female",
                "duration": "5-7 days acute phase",
                "notes": "Mosquito-borne viral infection",
                "complications": ["dengue hemorrhagic fever", "dengue shock syndrome", "plasma leakage"],
                "prevention": "Eliminate mosquito breeding sites, use repellents, wear long sleeves",
                "emergency_signs": ["severe abdominal pain", "persistent vomiting", "bleeding", "difficulty breathing"]
            },
            {
                "symptoms": ["diarrhea", "vomiting", "dehydration", "fever", "abdominal cramps"],
                "diagnosis": "Gastroenteritis",
                "severity": "low",
                "treatment": "ORS solution, probiotics, IV fluids if severe dehydration",
                "ai_cure": "Rest, drink ORS solution frequently (1 packet in 1 liter water). Eat bland foods (BRAT diet: bananas, rice, applesauce, toast). Avoid dairy and fatty foods for 48 hours. Maintain hand hygiene to prevent spread.",
                "doctor_solution": "Oral rehydration therapy with ORS. Probiotics may help restore gut flora. Antibiotics only if bacterial cause confirmed by stool culture. IV fluids if severe dehydration. Monitor electrolyte balance.",
                "doctor_name": "Dr. Family Medicine",
                "doctor_quote": "This appears to be viral gastroenteritis based on the acute onset and associated symptoms. The key is maintaining hydration with ORS and monitoring for signs of severe dehydration.",
                "patient_age": 30,
                "patient_gender": "male",
                "duration": "3-5 days",
                "notes": "Common stomach infection, usually viral",
                "complications": ["severe dehydration", "electrolyte imbalance"],
                "prevention": "Hand hygiene, safe food and water practices, proper food storage",
                "emergency_signs": ["severe dehydration", "blood in stool", "high fever", "severe abdominal pain"]
            },
            
            # Endocrine Conditions
            {
                "symptoms": ["excessive thirst", "frequent urination", "fatigue", "blurred vision", "weight loss"],
                "diagnosis": "Type 1 Diabetes Mellitus",
                "severity": "high",
                "treatment": "Insulin therapy (basal-bolus), blood glucose monitoring, diabetes education",
                "ai_cure": "URGENT: Seek immediate medical attention. Monitor blood sugar levels if possible. Follow prescribed insulin regimen strictly. Maintain regular meal times. Check for ketones in urine if blood sugar >250 mg/dl.",
                "doctor_solution": "Insulin therapy (basal-bolus regimen): Long-acting insulin (glargine) once daily + rapid-acting insulin (lispro) before meals. Blood glucose monitoring 4 times daily. Diabetes education program. Regular HbA1c monitoring every 3 months. Screen for complications annually.",
                "doctor_name": "Dr. Endocrinologist",
                "doctor_quote": "The patient presents with classic symptoms of diabetes with very high glucose and positive ketones, confirming new-onset Type 1 diabetes. We need immediate insulin therapy and comprehensive diabetes education.",
                "patient_age": 15,
                "patient_gender": "male",
                "duration": "Lifelong condition requiring daily management",
                "notes": "Autoimmune destruction of pancreatic beta cells",
                "complications": ["diabetic ketoacidosis", "hypoglycemia", "long-term vascular complications"],
                "prevention": "No prevention available, early recognition important for preventing DKA",
                "emergency_signs": ["vomiting", "fruity breath odor", "severe dehydration", "confusion"]
            },
            {
                "symptoms": ["fatigue", "weight gain", "cold intolerance", "dry skin", "constipation", "depression"],
                "diagnosis": "Hypothyroidism",
                "severity": "low",
                "treatment": "Levothyroxine replacement therapy, regular TSH monitoring",
                "ai_cure": "Take prescribed thyroid hormone replacement (levothyroxine) on empty stomach, 1 hour before breakfast. Maintain regular medication schedule. Eat iodine-rich foods (iodized salt, seafood). Regular follow-up for dose adjustments.",
                "doctor_solution": "Levothyroxine replacement therapy starting at 1.6 mcg/kg/day. Monitor TSH levels every 6-8 weeks initially, then every 6-12 months once stable. Adjust dose based on TSH levels (target: 0.5-2.5 mIU/L). Screen for cardiovascular disease.",
                "doctor_name": "Dr. Endocrinologist",
                "doctor_quote": "The TSH is elevated at 15 mIU/L with low T4, confirming primary hypothyroidism. We'll start levothyroxine 50 mcg daily and recheck thyroid function in 6 weeks to adjust the dose.",
                "patient_age": 45,
                "patient_gender": "female",
                "duration": "Lifelong treatment required",
                "notes": "Underactive thyroid gland, common in women",
                "complications": ["myxedema coma", "cardiovascular disease", "infertility"],
                "prevention": "Adequate iodine intake, regular screening in high-risk individuals",
                "emergency_signs": ["severe confusion", "very low body temperature", "slow heart rate"]
            },
            
            # Mental Health Conditions
            {
                "symptoms": ["persistent sadness", "loss of interest", "fatigue", "sleep problems", "appetite changes", "feelings of worthlessness"],
                "diagnosis": "Major Depressive Disorder",
                "severity": "medium",
                "treatment": "SSRIs (sertraline, escitalopram), CBT, lifestyle modifications",
                "ai_cure": "IMPORTANT: Seek professional mental health support immediately. Maintain regular sleep schedule (7-9 hours). Exercise regularly (30 minutes daily). Stay connected with family and friends. Practice stress management techniques like meditation. Avoid alcohol and recreational drugs.",
                "doctor_solution": "Antidepressant therapy: SSRIs (sertraline 50mg daily, escitalopram 10mg daily) or SNRIs (venlafaxine). Cognitive behavioral therapy (CBT) or interpersonal therapy. Regular monitoring for suicidal ideation, especially in first 4-6 weeks. Combination therapy often most effective.",
                "doctor_name": "Dr. Psychiatrist",
                "doctor_quote": "The patient meets criteria for major depressive disorder with significant functional impairment. We'll start sertraline 50mg daily and arrange CBT. Close monitoring for suicidal ideation is essential in the initial weeks.",
                "patient_age": 35,
                "patient_gender": "female",
                "duration": "6-12 months minimum treatment, may require longer",
                "notes": "Common mental health disorder affecting mood and function",
                "complications": ["suicide risk", "functional impairment", "substance abuse", "relationship problems"],
                "prevention": "Stress management, social support, early intervention, regular exercise, adequate sleep",
                "emergency_signs": ["suicidal thoughts", "self-harm", "complete social withdrawal", "psychotic symptoms"]
            },
            {
                "symptoms": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "muscle tension", "sleep problems"],
                "diagnosis": "Generalized Anxiety Disorder",
                "severity": "low",
                "treatment": "CBT, SSRIs if moderate-severe, relaxation techniques, lifestyle modifications",
                "ai_cure": "Practice deep breathing exercises (4-7-8 technique). Regular physical activity (30 minutes daily). Limit caffeine and alcohol. Maintain regular sleep schedule. Consider relaxation techniques like progressive muscle relaxation or mindfulness meditation.",
                "doctor_solution": "Cognitive behavioral therapy (CBT) as first-line treatment. SSRIs (sertraline, escitalopam) or SNRIs (venlafaxine) for moderate to severe cases. Benzodiazepines for short-term use only due to dependence risk. Stress management and lifestyle modifications.",
                "doctor_name": "Dr. Psychiatrist",
                "doctor_quote": "The patient shows persistent worry and physical symptoms consistent with generalized anxiety disorder. We'll start with CBT and relaxation techniques, considering medication if symptoms don't improve.",
                "patient_age": 30,
                "patient_gender": "male",
                "duration": "Chronic condition requiring ongoing management",
                "notes": "Persistent excessive worry about various life events",
                "complications": ["panic attacks", "depression", "substance abuse", "social isolation"],
                "prevention": "Stress management, regular exercise, adequate sleep, limit caffeine",
                "emergency_signs": ["panic attacks", "severe agitation", "inability to function", "suicidal thoughts"]
            },
            
            # Pediatric Conditions
            {
                "symptoms": ["fever", "cough", "runny nose", "ear pain", "irritability"],
                "diagnosis": "Acute Otitis Media (Ear Infection)",
                "severity": "low",
                "treatment": "Amoxicillin 40-50mg/kg/day, pain management, warm compress",
                "ai_cure": "Give paracetamol or ibuprofen for pain and fever (age-appropriate doses). Apply warm compress to affected ear. Ensure adequate rest and hydration. Complete prescribed antibiotic course if given. Follow up if symptoms worsen or persist beyond 48-72 hours.",
                "doctor_solution": "Amoxicillin 40-50mg/kg/day divided TID for 7-10 days (first-line). Amoxicillin-clavulanate if treatment failure or risk factors. Pain management with acetaminophen or ibuprofen. Tympanocentesis if severe or recurrent. Consider ear tubes for recurrent infections.",
                "doctor_name": "Dr. Pediatrician",
                "doctor_quote": "The tympanic membrane is erythematous and bulging, consistent with acute otitis media. Given the child's age and symptoms, we'll start amoxicillin and provide pain management guidance to the parents.",
                "patient_age": 3,
                "patient_gender": "male",
                "duration": "7-10 days with treatment",
                "notes": "Common childhood infection, often follows upper respiratory infection",
                "complications": ["hearing loss", "mastoiditis", "meningitis", "chronic infection"],
                "prevention": "Avoid smoke exposure, breastfeeding, pneumococcal vaccination",
                "emergency_signs": ["severe ear pain", "high fever", "discharge from ear", "hearing loss"]
            },
            
            # Geriatric Conditions
            {
                "symptoms": ["memory loss", "confusion", "difficulty with daily tasks", "mood changes", "disorientation"],
                "diagnosis": "Alzheimer's Disease",
                "severity": "medium",
                "treatment": "Cholinesterase inhibitors (donepezil), memantine, comprehensive care plan",
                "ai_cure": "Maintain structured daily routine. Ensure safe environment (remove hazards, install safety devices). Engage in cognitive activities (puzzles, reading). Regular physical exercise as tolerated. Provide emotional support and patience.",
                "doctor_solution": "Cholinesterase inhibitors (donepezil 5-10mg daily, rivastigmine, galantamine). Memantine for moderate to severe stages. Comprehensive care plan including safety assessment, caregiver support, and behavioral management. Regular monitoring for depression and agitation.",
                "doctor_name": "Dr. Geriatrician",
                "doctor_quote": "The cognitive assessment and brain imaging are consistent with Alzheimer's disease. We'll start donepezil to slow cognitive decline and arrange comprehensive support services for the patient and family.",
                "patient_age": 75,
                "patient_gender": "female",
                "duration": "Progressive condition, 7-10 years average",
                "notes": "Most common form of dementia, progressive cognitive decline",
                "complications": ["falls", "malnutrition", "infections", "behavioral problems"],
                "prevention": "Cardiovascular health, mental stimulation, social engagement, Mediterranean diet",
                "emergency_signs": ["severe agitation", "falls", "inability to eat", "signs of abuse or neglect"]
            }
        ]
        
        # Comprehensive symptom weights based on medical importance and urgency
        self.symptom_weights = {
            # Critical symptoms (0.9-1.0)
            "chest pain": 0.95,
            "difficulty breathing": 0.95,
            "shortness of breath": 0.95,
            "severe headache": 0.9,
            "unconsciousness": 1.0,
            "seizures": 0.95,
            "severe bleeding": 1.0,
            "stroke symptoms": 1.0,
            "heart attack symptoms": 1.0,
            "severe allergic reaction": 0.95,
            "difficulty swallowing": 0.9,
            "severe abdominal pain": 0.9,
            "sudden vision loss": 0.95,
            "paralysis": 0.95,
            "severe burns": 0.9,
            
            # High priority symptoms (0.7-0.89)
            "high fever": 0.85,
            "persistent fever": 0.8,
            "blood in stool": 0.85,
            "blood in urine": 0.85,
            "blood in vomit": 0.85,
            "severe vomiting": 0.8,
            "persistent vomiting": 0.8,
            "severe diarrhea": 0.8,
            "dehydration": 0.8,
            "confusion": 0.85,
            "memory loss": 0.8,
            "palpitations": 0.75,
            "irregular heartbeat": 0.8,
            "severe pain": 0.8,
            "weight loss": 0.75,
            "night sweats": 0.7,
            "persistent cough": 0.7,
            "coughing blood": 0.9,
            "severe fatigue": 0.7,
            "jaundice": 0.8,
            "severe swelling": 0.75,
            
            # Medium priority symptoms (0.5-0.69)
            "abdominal pain": 0.65,
            "nausea": 0.6,
            "vomiting": 0.65,
            "diarrhea": 0.6,
            "constipation": 0.5,
            "fatigue": 0.55,
            "dizziness": 0.65,
            "headache": 0.6,
            "joint pain": 0.6,
            "muscle aches": 0.55,
            "back pain": 0.6,
            "skin rash": 0.6,
            "itching": 0.5,
            "swelling": 0.6,
            "fever": 0.65,
            "chills": 0.6,
            "sweating": 0.5,
            "loss of appetite": 0.55,
            "sleep problems": 0.5,
            "anxiety": 0.55,
            "depression": 0.6,
            "mood changes": 0.5,
            
            # Lower priority symptoms (0.3-0.49)
            "cough": 0.45,
            "sore throat": 0.4,
            "runny nose": 0.35,
            "stuffy nose": 0.35,
            "sneezing": 0.3,
            "mild headache": 0.4,
            "mild pain": 0.4,
            "dry mouth": 0.35,
            "mild nausea": 0.4,
            "bloating": 0.4,
            "gas": 0.3,
            "heartburn": 0.45,
            "indigestion": 0.4,
            "mild fatigue": 0.4,
            "restlessness": 0.35,
            "mild dizziness": 0.4,
            "dry skin": 0.3,
            "hair loss": 0.35,
            "brittle nails": 0.3
        }

    def find_similar_cases(self, symptoms: List[str], patient_age: int = None, patient_gender: str = None) -> List[Dict]:
        """Find similar patient cases based on symptoms and demographics"""
        similar_cases = []
        
        for case in self.patient_cases:
            # Validate case has required fields
            if "symptoms" not in case:
                print(f"Warning: Case missing 'symptoms' field: {case.get('diagnosis', 'Unknown')}")
                continue
                
            try:
                similarity_score = self._calculate_similarity(symptoms, case["symptoms"], patient_age, case.get("patient_age"))
                if similarity_score > 0.1:  # Further lowered threshold to allow more potential matches
                    case_copy = case.copy()
                    case_copy["similarity_score"] = similarity_score
                    similar_cases.append(case_copy)
            except Exception as e:
                print(f"Error processing case {case.get('diagnosis', 'Unknown')}: {str(e)}")
                continue
        
        # Sort by similarity score (highest first)
        similar_cases.sort(key=lambda x: x["similarity_score"], reverse=True)
        return similar_cases[:5]  # Return top 5 matches

    def _normalize_symptoms(self, symptoms: List[str]) -> List[str]:
        """Normalize symptoms to improve matching"""
        # Common symptom aliases
        symptom_aliases = {
            "stomach pain": "abdominal pain",
            "stomach ache": "abdominal pain",
            "belly pain": "abdominal pain",
            "tummy ache": "abdominal pain",
            "body ache": "body aches",
            "muscle pain": "muscle aches",
            "joint ache": "joint pain",
            "head ache": "headache",
            "running nose": "runny nose",
            "blocked nose": "stuffy nose",
            "breathlessness": "shortness of breath",
            "breathing difficulty": "difficulty breathing",
            "loose motions": "diarrhea",
            "loose stools": "diarrhea",
            "feeling sick": "nausea",
            "throwing up": "vomiting",
            "temperature": "fever",
            "tiredness": "fatigue",
            "weakness": "fatigue"
        }
        
        normalized = []
        for symptom in symptoms:
            # Convert to lowercase and normalize
            normalized_symptom = symptom.lower().strip()
            # Check for aliases
            if normalized_symptom in symptom_aliases:
                normalized.append(symptom_aliases[normalized_symptom])
            else:
                normalized.append(normalized_symptom)
        
        return normalized

    def _calculate_similarity(self, input_symptoms: List[str], case_symptoms: List[str], input_age: int = None, case_age: int = None) -> float:
        """Calculate similarity score between input symptoms and case symptoms"""
        if not input_symptoms or not case_symptoms:
            return 0.0
        
        # Normalize symptoms for better matching
        input_symptoms = self._normalize_symptoms(input_symptoms)
        case_symptoms = self._normalize_symptoms(case_symptoms)
        
        # Symptom matching score
        common_symptoms = set(input_symptoms) & set(case_symptoms)
        
        # If no common symptoms, return 0
        if not common_symptoms:
            return 0.0

        # Jaccard index for overall symptom set similarity
        jaccard_index = len(common_symptoms) / len(set(input_symptoms) | set(case_symptoms))

        # Weight the score based on symptom importance
        weighted_score = 0
        for symptom in common_symptoms:
            weight = self.symptom_weights.get(symptom, 0.5)
            weighted_score += weight
        
        # Normalize weighted score by the number of input symptoms to penalize for few symptoms
        normalized_weighted_score = weighted_score / len(input_symptoms) if input_symptoms else 0.0
        
        # Combine Jaccard index and weighted score
        combined_score = (jaccard_index + normalized_weighted_score) / 2

        # Age similarity bonus (if provided)
        age_bonus = 0
        if input_age and case_age:
            age_diff = abs(input_age - case_age)
            if age_diff <= 5:
                age_bonus = 0.15
            elif age_diff <= 15:
                age_bonus = 0.07

        final_score = min(combined_score + age_bonus, 1.0)

        # If only one symptom is provided, reduce the score to reflect uncertainty
        if len(input_symptoms) == 1:
            final_score *= 0.6

        return final_score


    def get_ai_recommendations(self, symptoms: List[str], symptom_description: str = "", patient_age: int = None, patient_gender: str = None) -> Dict:
        """Get AI-powered recommendations based on similar cases"""
        
        if not symptoms:
            return {
                "risk_level": "unknown",
                "possible_conditions": [],
                "recommendations": ["Please provide symptoms for analysis."],
                "similar_cases": [],
                "confidence": 0.0,
                "emergency_required": False
            }

        similar_cases = self.find_similar_cases(symptoms, patient_age, patient_gender)
        
        if not similar_cases or similar_cases[0]['similarity_score'] < 0.15:
            # Provide general health advice even with low confidence
            general_advice = self._get_general_health_advice(symptoms)
            return {
                "risk_level": "low",
                "possible_conditions": ["General symptoms - specific diagnosis requires medical evaluation"],
                "ai_cure": general_advice["ai_cure"],
                "doctor_solution": general_advice["doctor_solution"],
                "recommendations": [
                    "The provided symptoms are not specific enough for a confident analysis.",
                    "Please provide more details or consult a doctor for a proper diagnosis.",
                    "Monitor symptoms and seek medical attention if they worsen or persist."
                ],
                "similar_cases": [],
                "confidence": 0.1,
                "emergency_required": False,
                "emergency_signs": general_advice["emergency_signs"],
                "complications": [],
                "prevention": "Maintain good hygiene, adequate rest, and healthy lifestyle",
                "duration": "Variable - depends on underlying condition"
            }
        
        # Analyze the top matches
        top_case = similar_cases[0]
        confidence = top_case["similarity_score"]

        # Adjust confidence based on the number of matches
        if len(similar_cases) < 3:
            confidence *= 0.8
        
        risk_levels = [case["severity"] for case in similar_cases[:3]]
        diagnoses = [case["diagnosis"] for case in similar_cases[:3]]
        
        # Determine overall risk level
        risk_level = self._determine_risk_level(risk_levels)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(similar_cases[:3], risk_level, confidence)
        
        # Get AI cure and doctor solution from the best match
        ai_cure = top_case.get("ai_cure", "Seek appropriate medical care for proper treatment.")
        doctor_solution = top_case.get("doctor_solution", "Comprehensive medical evaluation and treatment as clinically indicated.")
        
        return {
            "risk_level": risk_level,
            "possible_conditions": list(set(diagnoses)),
            "ai_cure": ai_cure,
            "doctor_solution": doctor_solution,
            "recommendations": recommendations,
            "similar_cases": similar_cases[:3],
            "confidence": round(confidence, 2),
            "emergency_required": risk_level in ["high", "critical"],
            "emergency_signs": top_case.get("emergency_signs", []),
            "complications": top_case.get("complications", []),
            "prevention": top_case.get("prevention", ""),
            "duration": top_case.get("duration", "Variable")
        }

    def _determine_risk_level(self, risk_levels: List[str]) -> str:
        """Determine overall risk level from multiple cases with improved accuracy"""
        if not risk_levels:
            return "unknown"
        
        # Count occurrences of each risk level
        risk_counts = {"critical": 0, "high": 0, "medium": 0, "moderate": 0, "low": 0}
        for level in risk_levels:
            if level in risk_counts:
                risk_counts[level] += 1
        
        # Prioritize higher risk levels
        if risk_counts["critical"] > 0:
            return "critical"
        elif risk_counts["high"] > 0:
            return "high"
        elif risk_counts["medium"] > 0 or risk_counts["moderate"] > 0:
            return "medium"
        else:
            return "low"

    def _generate_recommendations(self, cases: List[Dict], risk_level: str, confidence: float) -> List[str]:
        """Generate recommendations based on similar cases"""
        recommendations = []

        if confidence < 0.4:
            recommendations.append("DISCLAIMER: The AI has low confidence in this analysis. Please consult a doctor.")

        if risk_level in ["critical", "high"]:
            recommendations.append("⚠️ Seek immediate medical attention")
            recommendations.append("🏥 Consider emergency room visit if symptoms worsen")
        
        # Extract common treatments and advice
        treatments = []
        for case in cases:
            # Handle both old and new format
            if "ai_cure" in case:
                treatments.append(case["ai_cure"])
            elif "treatment" in case:
                treatments.append(case["treatment"])
            else:
                treatments.append("Follow medical advice")
        
        # Add general recommendations based on risk level
        if risk_level == "low":
            recommendations.extend([
                "💊 Over-the-counter medications may help with symptoms",
                "🏠 Rest and home care are usually sufficient",
                "📞 Contact doctor if symptoms persist beyond a few days"
            ])
        elif risk_level == "moderate":
            recommendations.extend([
                "👨‍⚕️ Schedule appointment with doctor within 24-48 hours",
                "📋 Monitor symptoms closely",
                "💊 Follow prescribed treatment plan"
            ])
        
        recommendations.extend([
            "💧 Stay hydrated",
            "🛌 Get adequate rest",
            "🌡️ Monitor your temperature regularly"
        ])
        
        return list(dict.fromkeys(recommendations)) # Remove duplicates

    def _get_general_health_advice(self, symptoms: List[str]) -> Dict:
        """Provide general health advice based on symptom categories"""
        
        # Categorize symptoms
        fever_symptoms = ["fever", "high fever", "chills", "sweating"]
        pain_symptoms = ["headache", "body aches", "muscle aches", "joint pain", "back pain", "abdominal pain", "chest pain"]
        respiratory_symptoms = ["cough", "shortness of breath", "difficulty breathing", "sore throat", "runny nose"]
        digestive_symptoms = ["nausea", "vomiting", "diarrhea", "constipation", "stomach pain", "loss of appetite"]
        neurological_symptoms = ["dizziness", "confusion", "memory loss", "seizures"]
        skin_symptoms = ["rash", "itching", "swelling"]
        
        has_fever = any(s in fever_symptoms for s in symptoms)
        has_pain = any(s in pain_symptoms for s in symptoms)
        has_respiratory = any(s in respiratory_symptoms for s in symptoms)
        has_digestive = any(s in digestive_symptoms for s in symptoms)
        has_neurological = any(s in neurological_symptoms for s in symptoms)
        has_skin = any(s in skin_symptoms for s in symptoms)
        
        # Generate appropriate advice
        ai_cure_parts = []
        emergency_signs = []
        
        if has_fever:
            ai_cure_parts.append("For fever: Rest in a cool environment, drink plenty of fluids, take paracetamol 500mg every 6 hours as needed.")
            emergency_signs.extend(["fever above 103°F (39.4°C)", "fever with severe headache", "fever with difficulty breathing"])
        
        if has_pain:
            ai_cure_parts.append("For pain: Apply appropriate hot/cold therapy, take over-the-counter pain relievers as directed, avoid strenuous activities.")
            emergency_signs.extend(["severe chest pain", "sudden severe headache", "severe abdominal pain"])
        
        if has_respiratory:
            ai_cure_parts.append("For respiratory symptoms: Stay hydrated, use humidifier or steam inhalation, avoid smoking and pollutants.")
            emergency_signs.extend(["severe difficulty breathing", "blue lips or fingernails", "persistent chest pain"])
        
        if has_digestive:
            ai_cure_parts.append("For digestive issues: Stay hydrated with clear fluids, eat bland foods (BRAT diet), avoid dairy and fatty foods temporarily.")
            emergency_signs.extend(["severe dehydration", "blood in vomit or stool", "severe abdominal pain"])
        
        if has_neurological:
            ai_cure_parts.append("For neurological symptoms: Ensure safety, avoid driving, seek medical evaluation promptly.")
            emergency_signs.extend(["loss of consciousness", "severe confusion", "seizures", "sudden weakness"])
        
        if has_skin:
            ai_cure_parts.append("For skin symptoms: Keep area clean and dry, avoid scratching, apply cool compresses if needed.")
            emergency_signs.extend(["severe allergic reaction", "widespread rash with fever", "difficulty swallowing"])
        
        # Default advice if no specific category matches
        if not ai_cure_parts:
            ai_cure_parts.append("General care: Get adequate rest, stay hydrated, eat nutritious foods, monitor symptoms closely.")
            emergency_signs = ["difficulty breathing", "severe pain", "high fever", "loss of consciousness"]
        
        ai_cure = " ".join(ai_cure_parts) + " Seek medical attention if symptoms worsen or persist beyond 3-5 days."
        
        doctor_solution = ("Comprehensive medical evaluation needed to determine underlying cause. " +
                         "Clinical examination, relevant investigations based on presenting symptoms. " +
                         "Symptomatic treatment and specific therapy based on diagnosis. " +
                         "Follow-up as clinically indicated.")
        
        return {
            "ai_cure": ai_cure,
            "doctor_solution": doctor_solution,
            "emergency_signs": list(set(emergency_signs))  # Remove duplicates
        }

# Initialize the database
ai_patient_db = AIPatientDatabase()
