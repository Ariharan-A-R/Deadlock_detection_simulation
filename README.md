# Deadlock_detection_simulation
🌀 Chandy-Misra-Haas Deadlock Detection Simulator
This is a visual simulator for the Chandy-Misra-Haas algorithm, implemented using Python's Tkinter GUI and NetworkX. The project simulates deadlock detection in a distributed system using a probe-based approach and provides a visual and interactive interface for students and developers to understand how the algorithm works.

🚀 Features

✅ Interactive process creation (click to add processes)

✅ Edge creation between nodes with visual arrows

✅ Animated probe messages showing the deadlock detection process

✅ Deadlock detection using Chandy-Misra-Haas algorithm

✅ Reset and retry support

✅ Visual status updates for user guidance

✅ Easy-to-understand interface for learning distributed deadlock detection

![image](https://github.com/user-attachments/assets/7c7f3819-1042-4ef9-80aa-747e1283aac1)
<!-- Optional: Replace with actual image link -->

🛠️ Tech Stack

Python 3.x

Tkinter (for GUI)

NetworkX (for graph representation and cycle detection)

📦 Installation
Clone the repository

bash
Copy
Edit

cd deadlock-simulator
Install dependencies
(Only networkx is required if you're using standard Python)

bash
Copy
Edit
pip install networkx
Run the application

bash
Copy
Edit
python simulator.py

📋 How to Use

Click on the canvas to create processes (P0, P1, etc.).

Click two existing processes to draw a directed edge between them.

The direction represents a wait-for relationship.

Click "Detect Deadlock" to simulate the Chandy-Misra-Haas algorithm.

Animated probes will simulate the message-passing.

You’ll get a notification if a deadlock is detected.

Click "Reset" to start a new simulation.

📚 Algorithm Overview

The Chandy-Misra-Haas algorithm detects deadlock using probe messages in the format (initiator, sender, receiver):

If a probe ever returns to the initiator, a cycle (i.e., deadlock) exists.

Otherwise, the system is deadlock-free.

👨‍💻 Developer Info

Author: Your Name

Email: rajusanthoshari@gmail.com



📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

