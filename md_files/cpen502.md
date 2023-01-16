---
layout: default
title: CPEN 502 Architecture for Learning Systems
# description: This is just another page
---

# CPEN 502: Architecture for Learning Systems

* * *

## Course Project

CPEN 502’s course project pertains to implementing machine learning (ML) concepts into the open-source programming game Robocode (<a href="https://robocode.sourceforge.io" target="_blank">Link available here</a>). In Robocode, tanks battle each other. In the course project, the goal is to defeat the enemy tank as much as possible using an AI-tank that I coded. The coding language used for this course project is Java as Robocode is written primarily in Java and .NET.

Project source code available via GitHub:
* Part 1 GitHub Repository: <a href="https://github.com/tkjsung/CPEN502-BackPropagation" target="_blank">Feedforward Neural Network with XOR training set</a>
* Part 2 & 3 GitHub Repository: <a href="https://github.com/tkjsung/CPEN502-QLearning_LUT_BackPropagation" target="_blank">Q-Learning with LUT and Neural Network</a>
	* Source code that I have written are located in the folder “src/cpen502_robocode” folder

### Details on each part

The course project is split into three parts.

* Part 1: Train a feedforward neural network using XOR data training set (four data points per training epoch).
	* Robocode not used at this point.
	* **Methodology:** Use PyTorch’s standard feedforward neural network coding sequence but in Java. ML functions that are commonly available in Python libraries like PyTorch is not available in Java, so essentially all neural network elements are coded from scratch. This includes connecting nodes in the feedforward network.
	* **ML Structure:** 3-layer feedforward neural network (NN) with gradient descent backpropagation.
		* One input layer with multiple input nodes (in this case, 2)
		* One hidden layer with multiple hidden nodes
		* One output layer with one output node.
* Part 2: Train a reinforcement learning algorithm using a Look-Up Table (LUT) in Robocode
	* Robocode is used in Part 2.
	* **Methodology:** Implement Q-Learning reinforcement learning algorithm using a LUT. LUT will determine what action the robot will take. Based on rewards given by the Q-learning algorithm, the LUT will update accordingly.
	* **ML Structure:** Look-Up Table that is updated via the Q-Learning reinforcement learning algorithm.
* Part 3: Train a reinforcement learning algorithm using backpropagation in Robocode
	* Part 3 is the combination of parts 1 and 2. Robocode is used in Part 3.
	* **Methodology:** Implement Q-Learning algorithm using backpropagation instead of LUT.
	* **ML Structure:** 3-layer feedforward neural network with gradient descent backpropagation. Q-learning algorithm elements Q-state and Q-value are used as input and output, respectively.
		* One input layer with multiple input nodes (Q-states)
		* One hidden layer with multiple hidden nodes
		* One output layer with one output node (Q-value). Q-value will determine the action of the robot.


<!-- ## Course Work Repositories

Written in Java.

* Backpropagation with XOR: <a href="https://github.com/tkjsung/CPEN502-BackPropagation" target="_blank">https://github.com/tkjsung/CPEN502-BackPropagation</a>
* Reinforcement Learning with Lookup Table (LUT) and Backpropagation: <a href="https://github.com/tkjsung/CPEN502-QLearning_LUT_BackPropagation" target="_blank">https://github.com/tkjsung/CPEN502-QLearning_LUT_BackPropagation</a>
 -->

## Course Info

_Text in this section is taken from the website of the Department of Electrical and Computer Engineering at the University of British Columbia (<a href="https://ece.ubc.ca" target="_blank">https://ece.ubc.ca</a>). Text was extracted in 2022._

This course is about machine learning with an emphasis on artificial neural networks and reinforcement learning. Students will have the opportunity to build a working AI that is able to adapt and learn through interactions with its environment. By the end of the course, students will understand and appreciate how reinforcement learning combined with with neural nets can be used to build powerful AI agents.

The course is very practical in nature and requires completion of 3 separate pieces of coursework written in Java.

<br><br>

[Back to Home Page](/md_files/home)
