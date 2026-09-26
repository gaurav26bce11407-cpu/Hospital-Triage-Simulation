# Hospital-Triage-Simulation using Python
The Hospital Triage Simulation is a Python-based console application designed to simulate a basic hospital patient-management, appointment-booking and doctor's interface system.

The program allows users to:

(i) Add and register patients
(ii) Calculate a patient's triage priority
(iii) View registered patient information
(iv) Access a doctor's interface
(v) View booked appointments
(vi) Check doctors' available dates
(vii) Book appointments based on doctor preference or date preference

#Features
1.) Patient Registration
The triage system collects basic patient's information such as :
(i) Patient's name
(ii) Age 
(iii) (O2) Oxygen Levels
(iv) Heart Rate
Then the patient's condition assigned a 'score' which is based on the entered medical values

2.) The Priority System

The program calculates a score using:

Oxygen(O2)levels
Heart rate 
Age

The patient is then assigned one of three priority levels:

Score	Priority
if score is - 6 or above then ->	CRITICAL
if score is 3–5	then -> URGENT
if it is below 3 then ->	NORMAL

This allows patients to be categorized according to the simulated urgency of their condition

3. Patient Records
All registered patients are stored during the program's execution.
The user can select "Show the patients" to display the registered patient information.

4. Doctor's Interface
The doctor interface provides three main functions:

View all registered patient data
View booked appointments for a doctor
View remaining available dates for a doctor

The program contains doctors from four different specialties:

Cardiologist

Orthopedic

Oncologist

Pulmonologist

5. Appointment Booking

Patients can book appointments using two different methods:

Priority by Doctor

The user can:

Select a medical specialty
Select a doctor
Select an available date
Confirm the appointment
Priority by Date

The user can:

Select a medical specialty
Select a hospital date
View doctors available on that date
Select a doctor
Confirm the appointment

Once a date is booked, it is removed from that doctor's available dates.

Python 3
Lists
Dictionaries
Conditional statements
while loops
for loops
Functions of built-in Python data structures
User input/output
String manipulation
Basic data management

The Main Menu will appear as:
Which task do you want to proceed with?

1. Add patients
2. Show the patients
3. Doctor's interface
4. Book Appointment
5. Exit

The user can select an option by entering its corresponding number.

The Triage Logic

The triage score is calculated using the patient's oxygen level, heart rate, and age.

Oxygen Level
O₂ < 90     → +5 points
O₂ < 94     → +3 points

Heart Rate
Heart rate > 130 or < 40 → +4 points
Heart rate > 110 or < 50 → +2 points

Age
Age > 60 → +1 point

The final score determines the patient's simulated priority level.

 Hospital Doctors

The simulation currently contains four departments:

Cardiologist

Dr. Sharma

Dr. Mehta

Dr. Rao

Orthopedic

Dr. Kapoor

Dr. Iyer

Dr. Verma

Oncologist

Dr. Sen

Dr. Bannerjee

Dr. Joshi

Pulmonologist

Dr. Das

Dr. Kulkarni

Dr. Nair

Each doctor initially has availability on the hospital's configured dates.

 Data Storage

This project currently stores data in memory using Python lists and dictionaries.

For example:

patient = []
appointments = []

Patient information and appointment information are stored while the program is running.

Note: The data is not permanently saved. Closing the program will remove the data.

 Purpose of the Project

This project was developed to practice fundamental Python programming concepts through a practical real-world simulation.

It demonstrates how basic programming concepts can be combined to create a larger console-based application.

 Future Improvements

Possible improvements for future versions include:

Adding a graphical user interface (GUI)
Adding permanent data storage using files or a database
Adding patient IDs
Adding login systems for doctors and administrators
Adding appointment cancellation
Adding more medical specialties
Adding more detailed patient records
Adding date and time slots for appointments
Improving input validation
Generating patient/appointment reports

 Author:[Gaurav Rathi]
Registration Number: [26BCE11407]

 Disclaimer

This project is an educational simulation created for learning Python programming.

It is not a real medical triage or hospital management system and should not be used for actual medical decision-making.
