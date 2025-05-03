# Ransomware Adversary Profiler Using LLMs

This project leverages Large Language Models (LLMs) to analyze ransomware attack patterns and automatically generate structured threat intelligence in STIX format. It processes victim reports from ransomware leak sites to profile adversary groups, their targets, and tactics.

## Key Features

- **Automated Data Collection**: Scrapes ransomware victim data from leak sites and APIs
- **LLM-Powered Analysis**: Uses Mistral-7B to extract structured threat intelligence
- **STIX 2.1 Output**: Generates standardized threat intelligence reports
- **Adversary Profiling**: Identifies group preferences for industries, company sizes, and geographies


# Installation
1. Clone the repository:
   ```bash
    git clone https://github.com/khalequzzamanlikhon/Ransomware-Adversary-Profiler-LLM.git
    cd ransomware-adversary-profiler

2. Set up Python environment:
     ```bash
            python -m venv venv
            source venv/bin/activate  # Linux/MacOS
            venv\Scripts\activate     # Windows\

3. Installation dependencies
    ```bash
     pip install -r requirements.txt
    
4. setup huggingface token
    ``` bash
      huggingface-cli login


# Key Technologies
  - Mistral-7B-Instruct: For NLP analysis of victim reports
  
  - SQLite: Lightweight database for report storage
  
  - STIX 2.1: Standardized threat intelligence format
  
  - Plotly: Interactive visualizations
  
  - Hugging Face Transformers: LLM pipeline management

# Data Sources
- Ransomware.live API


# Contributing
Contributions welcome! Please fork the repository and submit pull requests.

- Fork the project

- Create your feature branch (git checkout -b feature/AmazingFeature)

- Commit your changes (git commit -m 'Add some AmazingFeature')

- Push to the branch (git push origin feature/AmazingFeature)

- Open a Pull Request

# License
Distributed under the MIT License. See LICENSE for more information.

# Contact
Project Maintainer - Md Khalequzzaman Sarker Likhon

Project Link: [https://github.com/your-username/ransomware-adversary-profiler](https://github.com/khalequzzamanlikhon/Ransomware-Adversary-Profiler-LLM
