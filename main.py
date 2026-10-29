from medical_project.patient.patient import patient_details
from medical_project.patient.registration import register_patient
from medical_project.doctor.doctor import doctor_details
from medical_project.doctor.appointment import appointment
from medical_project.billing.bill import calculate_bill
from medical_project.billing.payment import payment
from medical_project.records.record import add_record
from medical_project.records.history import history

patient_id = input("enter patient id: ")
patient_name = input("enter patient name: ")
age = int(input("enter patient age: "))

register_patient(patient_id)
patient_details(patient_name, age)

doctor_name = input("enter doctor name: ")
department = input("enter department: ")

doctor_details(doctor_name, department)

date = input("enter appointment date: ")
appointment(date)

disease = input("enter disease: ")
medicine = input("enter medicine: ")
add_record(disease, medicine)

amount = float(input("enter bill amount: "))
calculate_bill(amount)
payment(amount)

history()
