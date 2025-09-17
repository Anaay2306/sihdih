import React, { useState, useContext } from 'react';
import { AuthContext } from '../App';

const RegisterPage = () => {
  const { register } = useContext(AuthContext);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    role: 'patient',
    phone: '',
    // Patient fields
    age: '',
    gender: '',
    village: '',
    blood_group: '',
    medical_history: '',
    allergies: '',
    emergency_contact: '',
    // Doctor fields
    specialization: '',
    license_number: '',
    location: '',
    experience_years: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    const userData = {
      name: formData.name,
      email: formData.email,
      password: formData.password,
      role: formData.role,
      phone: formData.phone,
      // Patient fields
      age: parseInt(formData.age) || null,
      gender: formData.gender,
      village: formData.village,
      blood_group: formData.blood_group,
      medical_history: formData.medical_history,
      allergies: formData.allergies,
      emergency_contact: formData.emergency_contact || formData.phone,
      // Doctor fields
      specialization: formData.specialization,
      license_number: formData.license_number,
      location: formData.location,
      experience_years: parseInt(formData.experience_years) || 0
    };

    const result = await register(userData);
    if (!result.success) {
      setError(result.error);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div style={{ maxWidth: '500px', margin: '2rem auto' }}>
        <div className="card">
          <div className="card-header">
            <h2 className="card-title">Register for Rural Telemedicine</h2>
            <p className="card-subtitle">Create your account to access healthcare services</p>
          </div>
          
          {error && <div className="alert alert-danger">{error}</div>}
          
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="form-label">Full Name *</label>
              <input
                type="text"
                className="form-control"
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Email *</label>
              <input
                type="email"
                className="form-control"
                value={formData.email}
                onChange={(e) => setFormData({...formData, email: e.target.value})}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Phone Number</label>
              <input
                type="tel"
                className="form-control"
                value={formData.phone}
                onChange={(e) => setFormData({...formData, phone: e.target.value})}
                placeholder="+91 XXXXX XXXXX"
              />
            </div>
            
            <div className="form-group">
              <label className="form-label">Password *</label>
              <input
                type="password"
                className="form-control"
                value={formData.password}
                onChange={(e) => setFormData({...formData, password: e.target.value})}
                required
              />
            </div>
            
            <div className="form-group">
              <label className="form-label">Confirm Password *</label>
              <input
                type="password"
                className="form-control"
                value={formData.confirmPassword}
                onChange={(e) => setFormData({...formData, confirmPassword: e.target.value})}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Role</label>
              <select
                className="form-control"
                value={formData.role}
                onChange={(e) => setFormData({...formData, role: e.target.value})}
              >
                <option value="patient">Patient</option>
                <option value="doctor">Doctor</option>
              </select>
            </div>

            <div className="form-group">
              <label className="form-label">Age</label>
              <input
                type="number"
                className="form-control"
                value={formData.age}
                onChange={(e) => setFormData({...formData, age: e.target.value})}
                min="1"
                max="120"
              />
            </div>

            <div className="form-group">
              <label className="form-label">Gender</label>
              <select
                className="form-control"
                value={formData.gender}
                onChange={(e) => setFormData({...formData, gender: e.target.value})}
              >
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>
            </div>

            <div className="form-group">
              <label className="form-label">Village/Location</label>
              <input
                type="text"
                className="form-control"
                value={formData.village}
                onChange={(e) => setFormData({...formData, village: e.target.value})}
                placeholder="Your village or location"
              />
            </div>

            {/* Patient-specific fields */}
            {formData.role === 'patient' && (
              <>
                <div className="form-group">
                  <label className="form-label">Blood Group</label>
                  <select
                    className="form-control"
                    value={formData.blood_group}
                    onChange={(e) => setFormData({...formData, blood_group: e.target.value})}
                  >
                    <option value="">Select Blood Group</option>
                    <option value="A+">A+</option>
                    <option value="A-">A-</option>
                    <option value="B+">B+</option>
                    <option value="B-">B-</option>
                    <option value="AB+">AB+</option>
                    <option value="AB-">AB-</option>
                    <option value="O+">O+</option>
                    <option value="O-">O-</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Emergency Contact</label>
                  <input
                    type="tel"
                    className="form-control"
                    value={formData.emergency_contact}
                    onChange={(e) => setFormData({...formData, emergency_contact: e.target.value})}
                    placeholder="+91 XXXXX XXXXX"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Medical History</label>
                  <textarea
                    className="form-control"
                    value={formData.medical_history}
                    onChange={(e) => setFormData({...formData, medical_history: e.target.value})}
                    placeholder="Any previous medical conditions or treatments"
                    rows="3"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Allergies</label>
                  <textarea
                    className="form-control"
                    value={formData.allergies}
                    onChange={(e) => setFormData({...formData, allergies: e.target.value})}
                    placeholder="Any known allergies"
                    rows="2"
                  />
                </div>
              </>
            )}

            {/* Doctor-specific fields */}
            {formData.role === 'doctor' && (
              <>
                <div className="form-group">
                  <label className="form-label">Specialization *</label>
                  <select
                    className="form-control"
                    value={formData.specialization}
                    onChange={(e) => setFormData({...formData, specialization: e.target.value})}
                    required
                  >
                    <option value="">Select Specialization</option>
                    <option value="General Medicine">General Medicine</option>
                    <option value="Pediatrics">Pediatrics</option>
                    <option value="Gynecology">Gynecology</option>
                    <option value="Cardiology">Cardiology</option>
                    <option value="Dermatology">Dermatology</option>
                    <option value="Orthopedics">Orthopedics</option>
                    <option value="Psychiatry">Psychiatry</option>
                    <option value="Emergency Medicine">Emergency Medicine</option>
                    <option value="Other">Other</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">License Number *</label>
                  <input
                    type="text"
                    className="form-control"
                    value={formData.license_number}
                    onChange={(e) => setFormData({...formData, license_number: e.target.value})}
                    placeholder="Medical license number"
                    required
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Hospital/Clinic Location</label>
                  <input
                    type="text"
                    className="form-control"
                    value={formData.location}
                    onChange={(e) => setFormData({...formData, location: e.target.value})}
                    placeholder="Your practice location"
                  />
                </div>

                <div className="form-group">
                  <label className="form-label">Years of Experience</label>
                  <input
                    type="number"
                    className="form-control"
                    value={formData.experience_years}
                    onChange={(e) => setFormData({...formData, experience_years: e.target.value})}
                    min="0"
                    max="50"
                    placeholder="Years of medical practice"
                  />
                </div>
              </>
            )}
            
            <button type="submit" className="btn btn-primary" style={{width: '100%'}} disabled={loading}>
              {loading ? 'Creating Account...' : 'Register'}
            </button>
          </form>
          
          <div style={{ textAlign: 'center', marginTop: '1rem' }}>
            <p>Already have an account? <a href="/">Sign in here</a></p>
            <p><a href="/admin-login">Admin/Government Login</a></p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
