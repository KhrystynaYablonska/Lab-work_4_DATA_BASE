from flask import Flask
from controllers.patient_controller import patient_bp

app = Flask(__name__)
app.register_blueprint(patient_bp)

if __name__ == '__main__':
    print("Starting Flask server for lung_health_db...")
    app.run(debug=True, port=5000)