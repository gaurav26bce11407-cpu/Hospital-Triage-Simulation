Problem Statement & System Requirements Specification

Project Title: VitYarthi Hospital Triage & Specialist Appointment Scheduling System

Author: GAURAV RATHI

Registration Number: 26BCE11407

Platform : Python 3.14

1. Problem Statement

In both outpatient departments and emergency healthcare intake units, two critical administrative and clinical bottlenecks consistently emerge:

Subjective Emergency Triage & Delayed Risk Identification:

Manual, unstructured patient intake relies heavily on subjective visual judgment or simple first-come-first-served queues. In high-pressure environments, this results in human error where patients suffering from silent, acute physiological distress (such as severe hypoxemia or abnormal tachycardia) wait behind stable patients, substantially elevating the risk of preventable morbidity and mortality.


2.) Scheduling Conflicts and Inflexible Consultation Booking:

Coordinating outpatient consultations across multiple clinical specialties (Cardiology, Orthopedics, Oncology, and Pulmonology) using decentralized or manual registries frequently causes:

Double-booking: Multiple patients receiving the same specialist slot.

Rigid Scheduling Pathways: Systems typically force users into a single booking flow, failing to support patients who prioritize a specific physician versus those who need a consultation on a specific date.

Provider-Patient Desynchronization: Physicians lack real-time visibility into their booked consultations, remaining availability, and the incoming emergency triage queue.

The objective of this project is to implement a unified, algorithmic decision-support and scheduling simulation in Python that automates patient urgency triage using physiological markers and provides dynamic, conflict-free appointment management.


2. Scope of the Project
In-Scope:

Algorithmic Triage Prioritization: Quantitative risk scoring based on physiological vital inputs: Oxygen Saturation (SpO2), Heart Rate (BPM), and Age.

Urgency Stratification: Automated classification of patient intake into three distinct priority levels: NORMAL, URGENT!, and CRITICAL!.

Specialty & Physician Roster Management: In-memory modeling of multiple medical disciplines (Cardiologist, Orthopedic, Oncologist, Pulmonologist) with distinct medical staff and date rosters.

Bi-Directional Booking Engine: Dual booking pipelines allowing users to book either by specialist preference (Doctor-First) or by calendar schedule availability (Date-First).

Dynamic Slot Depletion (Collision Prevention): Real-time removal (pop/remove) of consultation dates from a doctor's schedule upon successful booking to guarantee zero duplicate reservations.

Provider Dashboard: A dedicated physician portal enabling doctors to review hospital triage patients, inspect patient appointments booked under their name, and audit remaining available dates.

Input Validation: Numeric constraints and type-checking on vitals, menu options, and roster indices to prevent runtime exceptions.

Out-of-Scope:

Persistent disk or external relational database integration (all state management is handled in-memory during runtime).

Graphical User Interface (GUI) or web application frontend (interaction is strictly terminal/CLI-based).

External SMS, email, or webhook notification systems for appointment confirmation.

Integration with clinical hardware/IoT sensors for direct vitals capture.

Patient billing, health insurance processing, and electronic health record (EHR) export.



3. Target Users

The system is designed to simulate workflows utilized by three primary user groups:

Triage Nurses & Emergency Reception Staff:

Front-desk healthcare personnel who record arriving patient vitals, verify physiological parameters, and require instantaneous, algorithmic priority classification to direct critical patients to immediate emergency care.

Outpatient Coordinators & Helpdesk Staff / Patients:

Users booking specialist consultations who require flexible filtering—either matching a patient with a specific expert doctor or finding any available specialist on an urgent, specific calendar date without scheduling collisions.

Consulting Physicians & Medical Specialists:

Hospital doctors who need direct visibility into their scheduled consultations, accurate audits of their open calendar dates, and cross-departmental awareness of pending emergency triage cases.

4. High-Level FeaturesA

Quantitative Vital-Signs Triage Engine

Captures physiological vitals: SpO2, Heart Rate, and Age.

Evaluates clinical risk using a multi-factor tiered weighting formula:

Oxygen Saturation:

(SpO2): <90% then (+5 points), 

90% - 93% then (+3 points).

Heart Rate (BPM):

>130 or <40(BPM) then (+4 points),

111 - 130 or 40 - 49 (BPM) then (+2 points).

Age Demographics: >60(years) then (+1 point).

Maps scores to immediate action classifications:

(Score)>=6 then CRITICAL!

Score(3 - 5) then URGENT!

(Score) < 3 then NORMAL

Appends comprehensive intake records into a centralized patient registry.



B. Bi-Directional Specialist Booking System:

Pathway 1 (Priority by Doctor): 

Specialty = Doctor the Available Date is Confirmation.

Pathway 2 (Priority by Date):

Specialty = Target Hospital Date then 'List of Available Specialists' on that Day then 'Confirmation'.

Autonomous Calendar Depletion: 

Immediately isolates and removes confirmed calendar dates from the target doctor's list, ensuring complete concurrency safety within the session.

C. Physician Management Interface

Triage Queue Inspection: 

Comprehensive audit of all triage-screened patients and their priority ratings.

Doctor-Specific Appointment Search: 

Case-insensitive query system allowing doctors to review their upcoming consultations along with patient names and booked dates.

Remaining Slot Auditing:

Real-time visibility into still-available open consultation dates for any physician in the directory.


D. System Diagnostics & Error Handling

Safe input sanitization utilizing .strip(), .lower(), and .isdigit() checks.

Guard rails preventing invalid menu entries, out-of-range date selections, and negative vital-sign inputs.


This file covers:

Problem Statement: Detailed breakdown of manual triage subjectivity and scheduling collision bottlenecks.

Scope of the Project: Clear distinction of both in-scope features and out-of-scope boundaries.

Target Users: Personas for triage staff, booking coordinators/patients, and medical specialists.

High-Level Features: Clinical triage scoring logic, bi-directional booking mechanics, dynamic calendar depletion, and the doctor interface.


(iii) Visual Workflow Diagram: Demonstrates the end-to-end operational flow from triage to schedule mutation and doctor audit
