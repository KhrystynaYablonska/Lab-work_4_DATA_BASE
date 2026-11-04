from dao.patient_dao import PatientDAO

class PatientService:
    @staticmethod
    def get_all_patients():
        return PatientDAO.get_all()

    @staticmethod
    def get_patient_by_id(patient_id):
        return PatientDAO.get_by_id(patient_id)

    @staticmethod
    def create_patient(data):
        return PatientDAO.create(
            data['first_name'],
            data['last_name'],
            data['date_of_birth'],
            data['gender'],
            data.get('phone')
        )

    @staticmethod
    def update_patient(patient_id, data):
        PatientDAO.update(
            patient_id,
            data['first_name'],
            data['last_name'],
            data.get('phone')
        )

    @staticmethod
    def delete_patient(patient_id):
        PatientDAO.delete(patient_id)

    @staticmethod
    def get_hospital_doctors(hospital_id):
        return PatientDAO.get_hospital_with_doctors(hospital_id)

    @staticmethod
    def get_patient_devices(admission_id):
        return PatientDAO.get_patient_devices(admission_id)