from flask import Blueprint, jsonify, request
from services.patient_service import PatientService

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/api/patients', methods=['GET'])
def get_patients():
    patients = PatientService.get_all_patients()
    return jsonify(patients), 200

@patient_bp.route('/api/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = PatientService.get_patient_by_id(patient_id)
    if patient:
        return jsonify(patient), 200
    return jsonify({'error': 'Patient not found'}), 404

@patient_bp.route('/api/patients', methods=['POST'])
def create_patient():
    data = request.json
    new_id = PatientService.create_patient(data)
    return jsonify({'message': 'Patient created successfully', 'id': new_id}), 201

@patient_bp.route('/api/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.json
    PatientService.update_patient(patient_id, data)
    return jsonify({'message': 'Patient updated successfully'}), 200

@patient_bp.route('/api/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    PatientService.delete_patient(patient_id)
    return jsonify({'message': 'Patient deleted successfully'}), 200

@patient_bp.route('/api/hospitals/<int:hospital_id>/doctors', methods=['GET'])
def get_hospital_doctors(hospital_id):
    data = PatientService.get_hospital_doctors(hospital_id)
    return jsonify(data), 200

@patient_bp.route('/api/admissions/<int:admission_id>/devices', methods=['GET'])
def get_patient_devices(admission_id):
    data = PatientService.get_patient_devices(admission_id)
    return jsonify(data), 200