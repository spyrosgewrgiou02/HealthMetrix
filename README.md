# Healthmetrix: PC Diagnostic Tool

## Overview

Healthmetrix is a comprehensive PC diagnostic tool designed to provide detailed insights into your computer's health, including system information, disk health, read/write speeds, and network activity. This tool aims to help users monitor and maintain their PC's performance effectively.

## Features

- **System Information:**
  - CPU details
  - RAM size
  - Disk space
  - GPU information
  - CPU temperature (if available)

- **Disk Health:**
  - Total, used, and free disk space
  - Disk usage percentage

- **Diagnostics:**
  - Disk read/write speeds
  - Network activity (bytes sent and received)

## Installation

### Prerequisites

- Python 3.x
- Required libraries:
  - `psutil`
  - `cpuinfo`
  - `GPUtil`
  - `tqdm`
  - `wmi` (for Windows)
  - `os` (for Linux)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Healthmetrix.git
Navigate to the project directory:

sh
cd Healthmetrix
Install the required libraries:

sh
pip install psutil py-cpuinfo gputil tqdm wmi
Usage
Run the main script to start the diagnostic tool:

sh
python main.py
The tool will display system information, disk health, and diagnostics information directly in the console.

Logging
All errors and important events are logged to diagnostics.log for easy troubleshooting and reference.

License
This project is licensed under the MIT License. See the LICENSE file for details.

© Spyros Gewrgiou 2025. All rights reserved.
