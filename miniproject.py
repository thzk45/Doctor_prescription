import datetime

# Medicine database with prices (₹)
medicine_prices = {
    "Paracetamol": 2,
    "Amoxicillin": 5,
    "Cetirizine": 3,
    "Dolo650": 4,
    "Azithromycin": 7
}

# Consultation fee
consultation_fee = 100

# Patient details
patient_name = input("Enter Patient Name: ")
patient_age = input("Enter Patient Age: ")

# Current date and time
now = datetime.datetime.now()
date_time = now.strftime("%d-%m-%Y %H:%M:%S")

prescription = []
total_medicine_cost = 0

while True:
    med_name = input("\nEnter Medicine Name (or type 'done' to finish): ")

    if med_name.lower() == "done":
        break

    if med_name not in medicine_prices:
        print(" Medicine not found in database. Please try again.")
        continue

    dosage = input("Enter Dosage (format Morning-Afternoon-Night, e.g., 1-0-1): ")
    days = int(input("Enter Number of Days: "))

    # Calculate daily consumption
    try:
        morning, afternoon, night = map(int, dosage.split("-"))
    except:
        print("Invalid format! Please use like 1-0-1")
        continue

    total_pills = (morning + afternoon + night) * days
    cost = total_pills * medicine_prices[med_name]
    total_medicine_cost += cost

    prescription.append(f"{med_name} ({dosage}) for {days} days = {total_pills} tablets = Rs.{cost}")

# Final bill
total_amount = total_medicine_cost + consultation_fee

# Preparing prescription text
prescription_text = f"""
=============================
       Doctor Prescription
=============================
Patient Name : {patient_name}
Age          : {patient_age}
Date & Time  : {date_time}

Medicines Prescribed:
-----------------------------
"""

for item in prescription:
    prescription_text += item + "\n"

prescription_text += f"""
Consultation Fee : Rs.{consultation_fee}
-----------------------------
Total Amount     : Rs.{total_amount}
=============================
"""

# Save to txt file with UTF-8 encoding
file_name = f"{patient_name}_prescription.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(prescription_text)

print("\n Prescription saved successfully as", file_name)

