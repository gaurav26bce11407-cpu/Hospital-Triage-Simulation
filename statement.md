Problem Statement and Solution

Project Title: VitYarthi Hospital Triage & Specialist Appointment Scheduling System


Author: GAURAV RATHI


Registration Number: 26BCE11407





1. Problem Statement

Modern healthcare facilities which range from emergency triage rooms to outpatient specialty clinics face severe operational bottlenecks that compromise patient care and clinician productivity:

Primary Challenges:

Subjective Emergency Triage & Delayed Prioritization

In high-volume clinical settings, manual assessment of arriving patients without standardized quantitative metrics frequently leads to human error. Patients with critical physiological deterioration (Example - severe hypoxemia or extreme tachycardia) may be improperly queued behind non-urgent cases, leading to preventable complications and elevated mortality risk.

Fragmented Outpatient Scheduling & Calendar Collisions

Managing consultations across multiple medical specialties (Cardiology, Orthopedics, Oncology, Pulmonology) using static or manual records often results in:

Double-booking the same physician on a single date.

Inflexible scheduling workflows that fail to cater to whether a patient prioritizes a specific physician or a specific consultation date.

Lack of real-time schedule synchronization between patient-facing booking desks and doctor-facing portals.

Data Disconnect Between Emergency Triage and Clinical Staff

Physicians often lack quick, consolidated visibility into the incoming triage queue alongside their scheduled consultations, leading to delayed situational awareness in the ward.







2. Proposed Solution


The VitYarthi Hospital Triage Simulation provides a centralized, console-based decision support and dynamic scheduling system built using Python. It resolves the core bottlenecks through automated risk scoring, real-time schedule mutation, and isolated role-based interfaces.

Core Solution Modules

A. Rule-Based Quantitative Triage Engine

To remove subjectivity and clinical delays, the system implements an algorithmic triage evaluator that captures vital indicators and computes a weighted composite risk score:

(i) Oxygen Saturation(SpO2):
<=90% = +5points (Critical Respiratory Distress)
(90-93)% = +3points (Moderate hypoxemia)

(ii) Heart Rate

>130BPM or <40BPM = +4points (Severe Cadiac Abnormality)

(111-130)BPM or (40-49)BPM = +2points (Moderate Cardiac Irregularity)


(iii) Age Factor

>60 = +1point ( Higher risk Demographic )


Automated Queue Stratification:

Score >= 6 [Critical!] (Immediate emergency attention)

Score 3-5  [Urgent!]  (Prioritized Clinical Review)

Score <3   [Normal]   (Standard Outpatient Queue)


B. Bi-Directional Dynamic Scheduling Engine

The system resolves calendar conflicts and accommodates patient preference by offering two distinct booking pathways:

Priority by Doctor: Patients select a medical department, pick their desired physician, and view only that physician's open consultation dates.

Priority by Date: Patients select an intended date from the hospital calendar and are presented with all available specialists across a department who have open capacity on that exact day.






C. Real-Time Slot Collision Prevention


Prevents double-booking through dynamic list mutation (list.pop() and list.remove()).

When a consultation is booked, that specific date is immediately withdrawn from the physician's active availability array in real time, making duplicate bookings impossible across subsequent transactions.






D. Integrated Doctor Management Portal



Provides specialists with immediate access to inspect:

The live hospital-wide emergency triage queue.

Their personal confirmed patient appointment list (filtered through case-insensitive name matching).

An audit of their remaining open dates.



4. Expected Impact

Zero Double-Bookings: Automated slot depletion guarantees schedule integrity across all departments.

Objective Patient Prioritization: Ensures high-risk patients are flagged instantly based on physiological parameters rather than arrival order alone.

Operational Transparency: Synchronizes queue data between patients, reception desks, and consulting doctors in a unified environment.



(i) Structured Problem Formulation: Explicitly details the core challenges: subjective clinical triage, scheduling collisions/double-booking, and communication gaps between reception and doctors.

(ii) Engineered Solution Breakdown: Outlines the mathematical triage scoring rules, dual booking workflows, conflict-prevention slot depletion mechanism, and doctor portal.

(iii) Visual Workflow Diagram: Demonstrates the end-to-end operational flow from triage to schedule mutation and doctor audit
