---
layout: default
title: ELEC 49X Electrical and Computer Engineering Capstone Project
---

# ELEC 49X: Electrical and Computer Engineering Capstone Project

* * *

## About My Capstone Project

**Project Title: Wearable Capacitive Strain Sensor System**

The purpose of this project was to determine the feasibility of a wearable electronic sensor system and mobile application to assist post-stroke patients with limited arm mobility as they undergo rehabilitative physiotherapy. Specifically, it was designed to help users quantify their movements and track progress to help them stay motivated and convey their at-home progress to their physiotherapists. A minimum viable product that achieved this goal, which includes an armband with a capacitive sensor, custom printed circuit board (PCB), and an Android application, was created.

The flexible sensor, made from household materials, measures the change in capacitance as a user wearing it bends their elbow. The PCB is a rigid, 2-layer, 4.1-by-2.5 cm board that utilizes a small surface-mount microcontroller, the BGM121, to provide a compact but effective solution. The change in capacitance of the sensor is read and interpreted by the PCB and transmitted using Bluetooth Low Energy (BLE) to the application.

The Android application was built in Java using Android Studio. It implemented BLE to communicate with the sensor system. The app scans for nearby devices and, upon connection, reads live sensor data to show to the user. This data is also stored to track a users’ motion throughout each at-home physiotherapy session. The tracked data is displayed to the user in a graph which can be viewed again at any time.


## Capstone Project Work GitHub Repositories

For testing purposes, sensor data is transmitted to the Android app using an Arduino Nano 33 BLE Board.

* <a href="https://github.com/tkjsung/ELEC49X-DemoCode" target="_blank">Strain Sensor Data Transmission Code using Arduino</a>
* <a href="https://github.com/erinjhacker/ELEC490" target="_blank">Android App receives sensor data using BLE</a>


## Course Info

_Text in this section is taken from the website of the Department of Electrical and Computer Engineering at Queen's University (<a href="https://ece.queensu.ca" target="_blank">https://ece.queensu.ca</a>). Text was extracted in 2022._

The main objectives of the ELEC 49X project courses are either: (a) to propose, design, build, test, and present a project that deals with hardware and/or software and that produces a tangible result; or (b) to propose and study a thesis topic and then prepare a detailed thesis on the application or suitability of a particular device, technique, software artefact, or system to solve a significant, well-defined industrial or research problem.

The course features group projects in which both independent work and co-operative effort are required. A supervised working environment is established for the course where progress and long term goals (i.e., project milestones) are evaluated on a continuing basis by the student groups themselves and also by the faculty supervisors associated with the project groups and the ELEC 490 course instructors.

For the implementation-oriented projects, the emphasis is placed on systems and design methodology, which includes proposal and specification writing, subsystem design, testing, evaluation, and documentation. For a thesis-oriented effort, the emphasis is placed on research methodologies, ability to analyze and compare research results, degree of understanding of underlying theories and experimental methodologies, reporting, and documentation.

Throughout the course, students gain an appreciation of (a) the industrial or research context for the discipline and (b) the demands that might be placed on a junior engineer in the workplace or in postgraduate studies. This course relies on the technical and non-technical skills acquired in any of the courses taken before and concurrently with the project activity. The course is also intended to further develop relevant skills such as project management, documentation, and presentation.


[Back to Home Page](/md_files/home)
