# Cyber-trener
EN: An intelligent stationary system for monitoring the execution of complex physical exercises using computer vision (MediaPipe/YOLO) and a voice interface.

PL: Stacjonarny system nadzorujący poprawność wykonywania ćwiczeń fizycznych z wykorzystaniem wizji komputerowej i interfejsu głosowego.

## Project Overview
[cite_start]Cyber Trainer is a stationary intelligent system designed to monitor physical exercises with higher precision than wearable devices[cite: 2, 5]. [cite_start]While smartwatches can count repetitions, they cannot verify if a movement is performed correctly[cite: 5]. [cite_start]This system uses computer vision to detect improper positioning and imprecise movements that could lead to injury or spinal curvature[cite: 4].

## ✨ Key Features
* [cite_start]**Dual-Camera Analysis:** Utilizes a front and a side camera to achieve high-precision skeletal tracking[cite: 6, 7, 8].
* [cite_start]**Voice Interface:** Interaction is driven by voice commands, allowing the trainee to stay focused on the exercise without looking at a screen[cite: 22, 23].
* [cite_start]**Real-time Correction:** Provides immediate feedback on form and tempo[cite: 3].
* [cite_start]**Post-Session Review:** Users can review their performance on a screen after completing a set to see their movements visualized with skeletal overlays[cite: 23].

## 🛠 Tech Stack
* [cite_start]**Language:** Python [cite: 31]
* [cite_start]**Computer Vision:** OpenCV, MediaPipe [cite: 31]
* [cite_start]**Audio & Voice:** Speech_recognition [cite: 31]

## 🏗 System Setup
[cite_start]The system is designed for a stationary laboratory or gym environment[cite: 21]:
1. [cite_start]**Cameras:** Two smartphones mounted on tripods, configured for network video transmission.
2. [cite_start]**Audio:** A portable microphone worn by the trainee[cite: 28].
3. [cite_start]**Processing:** A laptop (optionally connected to a projector) running the core algorithms[cite: 29].

## Installation & Usage
*(This section will be updated as the project progresses)*
1. Clone the repository: `git clone https://github.com/user/cyber-trainer-ai.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure camera IP addresses in the configuration file.
