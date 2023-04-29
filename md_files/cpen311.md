---
layout: default
title: CPEN 311 Digital Systems Design
---

# CPEN 311: Digital Systems Design

* * *
## Table of Contents
* [Course Laboratory Work](#course-laboratory-work)
* [Course Info](#course-info)
* [List of Covered Topics](#list-of-covered-topics)

* * * 

## Course Laboratory Work

Available at: <a href="https://github.com/tkjsung/CPEN311" target="_blank">https://github.com/tkjsung/CPEN311</a>

In CPEN 311, laboratory sessions required the use of Altera’s DE1-SoC FPGA board. In the laboratory sessions, hardware description language SystemVerilog was used to enable certain features on or using the DE1-SoC FPGA board.

There were a total of five laboratory assessment items. Each subsequent lab uses concepts from earlier labs (e.g., If Finite State Machine (FSM) is first used in lab 2, lab 3 onwards would also use the concept).
* <b>Lab 1: Tone Organ</b>
	* Focus: Basic Verilog/SystemVerilog
	* Goal: Write HDL code that...
		* Plays a specified frequency tone through the audio output of the FPGA (HDL code for processing and playing audio provided as black box.)
		* Implements clock dividers using counters
* <b>Lab 2: Simple iPod.</b>
	* Focus: Finite State Machines (FSM), Flash Memory, PS2 Keyboard
	* Goal: Write FSMs that...
		* Reads keyboard input to control when music plays / stops / pauses / rewinds / forwards / resets.
		* Reads flash memory by controlling memory address
* <b>Lab 3: Simple iPod with Strength Meter</b>
	* Focus: Assembly Language
	* Goal: An extension of Lab 2, write assmebly language to show the current volume level of the music by finding highest bit containing a 1. Result should be shown using LEDs on the FPGA.
* <b>Lab 4: RC4 Decryption</b>
	* Focus: Memory, Scheduling, and Decryption
	* Goal: Write FSMs that...
		* Reads RC4-encrypted data from RAM (Generated via Altera's IP).
		* Write RC4-decrypted data to RAM going through the RC4 algorithm
		* Detect if data is decrypted
		* Finds the decryption key by cycling through 0x0 to 0x3FFFFF.
* <b>Lab 5: VGA Oscilloscope</b>
	* Focus: Hardware/Software Interface, Direct Digital Synthesis (DDS), Linear Feedback Shift Register (LFSR), Modulations, Clock Domains, Audio, and VGA.
	* Goal: Provided with a 2-channel VGA oscilloscope, ...
		* Use Avalon IP via System Integration Tool to specify required components, such as procesor, memory, I/O, timer, and parallel I/O.
			* Processor: NIOS-II
			* Tool: Quartus II's Qsys GUI
		* Instantiate DDS and LFSR and show on the oscilloscope via the newly created PIO from System Integration Tool
		* Generate the following modulations based on LFSR pattern and show on oscilloscope: Amplitude Shift Keying (ASM), Binary Phase Shift Keying (BPSK), and Frequency Shift Keying (FSK).
		* Write modules to cross clock domains safely
		* Modify or Create C programs to implement more audio files and change icons displayed on VGA oscilloscope


<!-- Hardware Description Language used is SystemVerilog.

Please note that the repository may be privated during certain times of the year (usually September to December) so current students cannot use this to fulfill laboratory assessments.

Link: <a href="https://github.com/tkjsung/CPEN311" target="_blank">https://github.com/tkjsung/CPEN311</a> -->

## Course Info

CPEN 311 is a course on advanced combination and sequential electronic system design, which involves the use of computer hardware. Hardware specifications, modeling, and simulation are done using hardware description languages (HDL) and CAD tools. Hardware designs written using HDL or designed using CAD tools are implemented with programmable logic on FPGAs. Applications include complex state machines, microcontrollers, arithmetic circuits, and interface units.

### List of Covered Topics

* SystemVerilog Basics
* Timing
	* Clock Skew
	* Phase Locked Loops
	* Glitches
	* Pipelining
	* Gate Delays
	* FPGA Delays
	* Metastability
	* Clock Domain Crossings
* Reliable Finite State Machine Design
* Arithmetic Circuits
* Linear Feedback Shift Register (LFSR)
* Clock Skew and Domains
* Power Consumption
* Digital Signal Processing
* Direct Digital Synthesis
* Digital to Analog / Analog to Digital Circuits
* Transceivers and 8b/10b
	* Multigigabit Transceivers (MGT)
	* Serializer / Deserializer (SERDES)
	* Line / Block Coding
	* Eye Diagram
	* Differential Signaling
* High Level Synthesis


<br><br>

<!---
Advanced combinational and sequential electronic system design. Hardware specification, modeling, and simulation using hardware description languages (HDLs) and CAD tools. Design with programmable logic including FPGA’s. Applications include complex state machines, microcontrollers, arithmetic circuits, and interface units.
-->

[Back to Home Page](/md_files/home)
