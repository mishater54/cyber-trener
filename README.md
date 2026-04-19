# Cyber-trener
EN: An intelligent stationary system for monitoring the execution of complex physical exercises using computer vision (MediaPipe/YOLO) and a voice interface.

PL: Stacjonarny system nadzorujący poprawność wykonywania ćwiczeń fizycznych z wykorzystaniem wizji komputerowej i interfejsu głosowego.

## Project Overview
Cyber Trainer is a stationary intelligent system designed to monitor physical exercises with higher precision than wearable devices. While smartwatches can count repetitions, they cannot verify if a movement is performed correctly. This system uses computer vision to detect improper positioning and imprecise movements that could lead to injury or spinal curvature.

## ✨ Key Features
**Dual-Camera Analysis:** Utilizes a front and a side camera to achieve high-precision skeletal tracking.

**Voice Interface:** Interaction is driven by voice commands, allowing the trainee to stay focused on the exercise without looking at a screen.

**Real-time Correction:** Provides immediate feedback on form and tempo.

**Post-Session Review:** Users can review their performance on a screen after completing a set to see their movements visualized with skeletal overlays.

## 🛠 Tech Stack
**Language:** Python.

**Computer Vision:** OpenCV, MediaPipe.

**Audio & Voice:** Speech_recognition.

## 🏗 System Setup
The system is designed for a stationary laboratory or gym environment:
1. **Cameras:** Two smartphones mounted on tripods, configured for network video transmission.
2. **Audio:** A portable microphone worn by the trainee#.
3. #**Processing:** A laptop (optionally connected to a projector) running the core algorithms.

## Installation & Usage
*(This section will be updated as the project progresses)*
1. Clone the repository: `git clone https://github.com/user/cyber-trainer-ai.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure camera IP addresses in the configuration file.
