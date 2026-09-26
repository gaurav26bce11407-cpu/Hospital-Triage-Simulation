print("Name - GAURAV RATHI")
print("Registration Number - 26BCE11407")

patient = []
appointments = []

all_hospital_dates = ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04"]

doctors_directory = {
    "1": {
        "specialty": "Cardiologist",
        "doctors": {
            "Dr. Sharma": list(all_hospital_dates),
            "Dr. Mehta": list(all_hospital_dates),
            "Dr. Rao": list(all_hospital_dates)
        }
    },
    "2": {
        "specialty": "Orthopedic",
        "doctors": {
            "Dr. Kapoor": list(all_hospital_dates),
            "Dr. Iyer": list(all_hospital_dates),
            "Dr. Verma": list(all_hospital_dates)
        }
    },
    "3": {
        "specialty": "Oncologist",
        "doctors": {
            "Dr. Sen": list(all_hospital_dates),
            "Dr. Bannerjee": list(all_hospital_dates),
            "Dr. Joshi": list(all_hospital_dates)
        }
    },
    "4": {
        "specialty": "Pulmonologist",
        "doctors": {
            "Dr. Das": list(all_hospital_dates),
            "Dr. Kulkarni": list(all_hospital_dates),
            "Dr. Nair": list(all_hospital_dates)
        }
    }
}

print("===========VitYarthi PROJECT===============")
print("========Welcome to Hospital triage Simulation!========")

while True:
    print("\nWhich task do you want to proceed with?")
    print("1. Add patients")
    print("2. Show the patients")
    print("3. Doctor's interface")
    print("4. Book Appointment")
    print("5. Exit")

    task = input("Enter your preferred task : ")

    if task == "1":
        print("\nAdding patient details...")
        name1 = input("Enter patient's name : ")

        age = int(input("Enter patient's age : "))
        if age < 0:
            print("Enter valid age!")

        oxy = int(input("Enter patient's O2(oxygen) levels : "))
        if oxy < 0:
            print("Please enter valid oxygen levels!")

        heartbeat_rate = int(input("Enter heart beat value : "))
        if heartbeat_rate < 0:
            print("Please enter valid heartbeat readings!")

        score = 0
        if oxy < 90:
            score = score + 5
        elif oxy < 94:
            score = score + 3

        if heartbeat_rate > 130 or heartbeat_rate < 40:
            score = score + 4
        elif heartbeat_rate > 110 or heartbeat_rate < 50:
            score = score + 2

        if age > 60:
            score = score + 1

        if score >= 6:
            priority = "CRITICAL!"
        elif score >= 3:
            priority = "URGENT!"
        else:
            priority = "NORMAL"

        record = [
            ("Name : ", name1),
            ("Patient's age", age),
            ("Oxygen levels : ", oxy),
            ("Heart rate : ", heartbeat_rate),
            ("Score : ", score),
            ("Priority : ", priority)
        ]

        patient.append(record)
        print("Patient added in system successfully!")
        print("Priority - ", priority)

    elif task == "2":
        print("\nLoading patient's details...")
        if len(patient) == 0:
            print("No patients registered.")
        else:
            print("\n=== Registered Triage Patients ===")
            for p in patient:
                print(p)

    elif task == "3":
        while True:
            print("\n--- Doctor's Interface ---")
            print("1.) View all triage patients data")
            print("2.) View my booked appointments")
            print("3.) View my remaining available dates")
            print("4.) Exit Interface")

            tusk = input("Enter your preferred task : ")

            if tusk == "1":
                print("\nLoading patient's details...")
                if len(patient) == 0:
                    print("No patients registered.")
                else:
                    print("\n=== Patient Data ===")
                    for p in patient:
                        print(p)

            elif tusk == "2":
                doc_name_query = input("Enter Doctor's Name (e.g., Dr. Sharma): ").strip().lower()
                matching_appointments = [
                    appt for appt in appointments 
                    if appt["doctor"].lower() == doc_name_query
                ]

                if not matching_appointments:
                    print(f"No appointments found for '{doc_name_query}'.")
                else:
                    print(f"\n=== Booked Slots for {matching_appointments[0]['doctor']} ===")
                    for idx, appt in enumerate(matching_appointments, 1):
                        print(f"{idx}. Date: {appt['date']} | Patient: {appt['patient_name']} | Specialty: {appt['specialty']}")

            elif tusk == "3":
                doc_name_query = input("Enter Doctor's Name (e.g., Dr. Sharma): ").strip().lower()
                found = False
                for cat in doctors_directory.values():
                    for doc, dates in cat["doctors"].items():
                        if doc.lower() == doc_name_query:
                            found = True
                            print(f"\nRemaining available dates for {doc}:")
                            if dates:
                                for d in dates:
                                    print(f"- {d}")
                            else:
                                print("No remaining dates available (fully booked).")
                            break
                    if found:
                        break
                if not found:
                    print("Doctor name not found in the directory.")

            elif tusk == "4":
                print("Closing Doctor's Interface.")
                break
            else:
                print("Invalid choice! Try again!")

    elif task == "4":
        print("\n--- Book an Appointment ---")
        p_name = input("Enter patient's name: ")

        print("\nHow would you like to book?")
        print("1. Priority by Doctor")
        print("2. Priority by Date")
        pref_choice = input("Enter your choice (1 or 2): ").strip()

        if pref_choice == "1":
            print("\nSelect Specialty:")
            print("1. Cardiologist")
            print("2. Orthopedic doctor")
            print("3. Oncologist")
            print("4. Pulmonologist")
            spec_choice = input("Enter specialty choice (1-4): ").strip()

            if spec_choice not in doctors_directory:
                print("Invalid specialty selected!")
                continue

            selected_dept = doctors_directory[spec_choice]
            doctor_list = list(selected_dept["doctors"].keys())

            print(f"\nAvailable {selected_dept['specialty']} Doctors:")
            for idx, doc in enumerate(doctor_list, 1):
                print(f"{idx}. {doc}")

            doc_input = input(f"Select a doctor (1-{len(doctor_list)}): ").strip()
            if not doc_input.isdigit() or int(doc_input) < 1 or int(doc_input) > len(doctor_list):
                print("Invalid doctor selection!")
                continue

            selected_doctor = doctor_list[int(doc_input) - 1]
            available_dates = selected_dept["doctors"][selected_doctor]

            if not available_dates:
                print(f"Sorry, {selected_doctor} has no available dates left!")
                continue

            print(f"\nAvailable dates for {selected_doctor}:")
            for idx, d in enumerate(available_dates, 1):
                print(f"{idx}. {d}")

            date_input = input(f"Choose a date (1-{len(available_dates)}): ").strip()
            if not date_input.isdigit() or int(date_input) < 1 or int(date_input) > len(available_dates):
                print("Invalid date selection!")
                continue

            booked_date = available_dates.pop(int(date_input) - 1)

            appointments.append({
                "patient_name": p_name,
                "specialty": selected_dept["specialty"],
                "doctor": selected_doctor,
                "date": booked_date
            })

            print("\nAppointment booked successfully!")
            print(f"Details -> Patient: {p_name} | Doctor: {selected_doctor} ({selected_dept['specialty']}) | Date: {booked_date}")

        elif pref_choice == "2":
            # 1. Ask for doctor category first
            print("\nSelect Specialty:")
            print("1. Cardiologist")
            print("2. Orthopedic doctor")
            print("3. Oncologist")
            print("4. Pulmonologist")
            spec_choice = input("Enter specialty choice (1-4): ").strip()

            if spec_choice not in doctors_directory:
                print("Invalid specialty selected!")
                continue

            selected_dept = doctors_directory[spec_choice]

            # 2. Ask for the desired date
            print("\nHospital Available Dates:")
            for idx, d in enumerate(all_hospital_dates, 1):
                print(f"{idx}. {d}")

            date_input = input(f"Select a date (1-{len(all_hospital_dates)}): ").strip()
            if not date_input.isdigit() or int(date_input) < 1 or int(date_input) > len(all_hospital_dates):
                print("Invalid date selection!")
                continue

            selected_date = all_hospital_dates[int(date_input) - 1]

            # 3. Show doctors in that category available on that date
            available_doctors = []
            for doc_name, dates in selected_dept["doctors"].items():
                if selected_date in dates:
                    available_doctors.append({
                        "doctor": doc_name,
                        "specialty": selected_dept["specialty"],
                        "date_list": dates
                    })

            if not available_doctors:
                print(f"No {selected_dept['specialty']} doctors are available on {selected_date}.")
                continue

            print(f"\n{selected_dept['specialty']} doctors available on {selected_date}:")
            for idx, entry in enumerate(available_doctors, 1):
                print(f"{idx}. {entry['doctor']}")

            doc_pick = input(f"Select a doctor (1-{len(available_doctors)}): ").strip()
            if not doc_pick.isdigit() or int(doc_pick) < 1 or int(doc_pick) > len(available_doctors):
                print("Invalid choice!")
                continue

            chosen_entry = available_doctors[int(doc_pick) - 1]
            chosen_entry["date_list"].remove(selected_date)

            appointments.append({
                "patient_name": p_name,
                "specialty": chosen_entry["specialty"],
                "doctor": chosen_entry["doctor"],
                "date": selected_date
            })

            print("\nAppointment booked successfully!")
            print(f"Details -> Patient: {p_name} | Doctor: {chosen_entry['doctor']} ({chosen_entry['specialty']}) | Date: {selected_date}")

        else:
            print("Invalid choice! Returning to main menu.")

    elif task == "5":
        print("Closing Hospital triage , Goodbye!")
        break

    else:
        print("Invalid choice , try again!")