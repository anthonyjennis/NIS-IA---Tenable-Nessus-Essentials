# Vulnerability Scanning and Automation with Nessus Essentials

## Project Overview
This repository contains the automation script and documentation for our group project on vulnerability scanning using Tenable Nessus Essentials. 

As part of our project, we successfully demonstrated:
* Host discovery and network scanning
* The difference between Authenticated and Unauthenticated vulnerability scanning
* Advanced scan template configuration
* Detailed vulnerability analysis and remediation recommendations
* Security tool automation using the Nessus API

### Final Video - [Youtube](https://youtu.be/eZ4VtrQYhxc)

### Installations
* Virtual Box - [Link](https://www.virtualbox.org/)
* Metasploitable - [Link](https://sourceforge.net/projects/metasploitable/)
* Tenable Nessus Essentials - [Link](https://www.tenable.com/downloads/nessus)

### Prerequisites
* Python 3.x installed on your machine
* A running instance of Tenable Nessus Essentials
* API Keys (Access and Secret) generated from your Nessus user account
* A pre-configured scan in Nessus to target

### Installation & Setup
1. Clone this repository to your local machine.
2. Install the required Python dependencies using the terminal:
   ```bash
   pip install -r requirements.txt

3. Open nessus_trigger.py in a text editor and update the configuration variables at the top of the file with your specific details:
   ```bash
   ACCESS_KEY = Your Nessus API Access Key
   SECRET_KEY = Your Nessus API Secret Key

### Demo Videos
* Host Discovery - [Youtube](https://youtu.be/vu5VF0lB-kE)
* Unauthenticated Scan - [Youtube](https://youtu.be/KDlqICQPQM8)
* Authenticated Scan - [Youtube](https://youtu.be/lejSyNUCvfM)
* Advanced Scan - [Youtube](https://youtu.be/-TGVpU6YDCk)

### Usage
Because the free Student tier restricts launching scans via the API, this script is designed to authenticate securely and automatically retrieve/audit the status of all configured scans on the server.
