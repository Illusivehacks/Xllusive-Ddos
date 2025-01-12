# Xllusive DDoS Tool

![Banner](banner.png)

## Overview

**Xllusive DDoS Tool** is a powerful educational tool designed to simulate a stress test (DDoS simulation) on a target URL. With a simple graphical user interface (GUI), the tool provides a highly interactive and immersive experience, complete with simulated "hacking" sequences and background animations. This tool is designed for ethical use only—always get proper authorization before conducting any stress tests.

**Important Note:**  
**Unauthorized use of this tool is illegal.** Only perform DDoS simulations on systems that you own or have explicit permission to test.

---

## Features

- **🖥️ Graphical User Interface (GUI)**  
  The tool features an intuitive GUI built using **Tkinter** for easy operation.

- **🎮 Real-Time Hacking Simulation**  
  Enjoy an immersive experience with a scrolling "hacking" code and animated background GIF to simulate a cyber attack.

- **🔐 User Authentication**  
  A password prompt ensures that only authorized users can start the stress test.

- **⚡ Stress Test Configuration**  
  You can specify the target URL and the number of threads to control the intensity of the attack.

- **🛑 Stop Test Option**  
  A button to stop the test anytime.

---

## Screenshots

![GUI Screenshot](screenshot1.png)

---

## Requirements

Before running the tool, make sure you have the following:

- **Python 3.8+**  
  Download Python from [python.org](https://www.python.org/downloads/).

- **Required Python Libraries**  
  Install the following libraries using **pip**:

  ```bash
  pip install requests threading colorama pygame Pillow pystyle playsound aiohttp multiprocess
