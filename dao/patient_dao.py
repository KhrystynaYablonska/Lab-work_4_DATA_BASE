from config import get_db_connection

class PatientDAO:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patients;")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_id(patient_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM patients WHERE patient_id = %s;", (patient_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def create(first_name, last_name, date_of_birth, gender, phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (first_name, last_name, date_of_birth, gender, phone))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    @staticmethod
    def update(patient_id, first_name, last_name, phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE patients SET first_name = %s, last_name = %s, phone = %s WHERE patient_id = %s;"
        cursor.execute(query, (first_name, last_name, phone, patient_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patients WHERE patient_id = %s;", (patient_id,))
        conn.commit()
        cursor.close()
        conn.close()

    # Зв'язок 1:M (Лікарня -> Лікарі через Відділення)
    @staticmethod
    def get_hospital_with_doctors(hospital_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT h.name AS hospital_name, dep.name AS department_name, d.first_name, d.last_name, d.specialization
            FROM hospitals h
            JOIN departments dep ON h.hospital_id = dep.hospital_id
            JOIN doctors d ON dep.department_id = d.department_id
            WHERE h.hospital_id = %s;
        """
        cursor.execute(query, (hospital_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    # Зв'язок M:M (Пристрої пацієнта)
    @staticmethod
    def get_patient_devices(admission_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT p.first_name, p.last_name, dev.serial_number, dev.model, pd.assigned_at
            FROM admissions a
            JOIN patients p ON a.patient_id = p.patient_id
            JOIN patient_devices pd ON a.admission_id = pd.admission_id
            JOIN devices dev ON pd.device_id = dev.device_id
            WHERE a.admission_id = %s;
        """
        cursor.execute(query, (admission_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result