## Hi there 👋

🚀 SDET Automation Framework
Welcome to the Automation Framework built by a  Software Development Engineer in Test (SDET) with more than 3.5 years of experience!
This framework is designed for end-to-end test automation using Python, Selenium, Pytest, BDD, and Robot Framework. 
It seamlessly integrates with Allure and HTML for reporting and Jenkins for continuous integration and deployment.

🛠️ Tech Stack
Programming Language: Python 🐍
Automation Tools:
Selenium WebDriver 🌐
Pytest 🧪
BDD (Behavior-Driven Development) with Pytest-BDD & Robot Framework 🤖
Reporting:
Allure Reports 📊
HTML Reports 📄
CI/CD Tools:
Jenkins 🔧

📈 Key Features
🔹 Python & Selenium Automation
Automates the functional and regression testing of web applications with Python and Selenium WebDriver, enabling efficient browser-based automation.

🔹 Pytest: Test Framework
The framework utilizes Pytest for organizing and executing test cases:

Parametrized tests for flexibility.
Reusable fixtures for test setup and teardown.
Supports parallel test execution with pytest-xdist.

🔹 BDD with Pytest & Robot Framework
BDD tests are written in a natural language format that both technical and non-technical stakeholders can understand.

Pytest-BDD: BDD integrated with Pytest for structured, behavior-driven tests.
Robot Framework: Keyword-driven test automation, commonly used for acceptance testing.


🔹 Allure & HTML Reports
Generate comprehensive, easy-to-read test reports:

Allure Reports: Interactive reports with detailed test steps, screenshots, and more.
HTML Reports: Lightweight HTML-based test summaries.

🔹 Jenkins for CI/CD Integration
Integrated with Jenkins to automate the execution of tests as part of a continuous integration pipeline, ensuring reliable code deployment.

📁 Project Structure


📦 project_root/
├── 📂 tests/                       # Test cases organized by type
│   ├── 📂 unit_tests/               # Unit tests
│   ├── 📂 integration_tests/        # Integration tests
│   ├── 📂 e2e_tests/                # End-to-end tests
│   └── 📄 test_login.py             # Example test script
├── 📂 pages/                       # Page Object Model (POM) implementations
│   └── 📄 login_page.py             # Page class for login functionality
├── 📂 resources/                   # Additional resources (data files, etc.)
│   └── 📄 test_data.json            # Example test data
├── 📂 reports/                     # Test reports directory
│   ├── 📂 allure_results/           # Allure results
│   └── 📂 html_reports/             # HTML reports
├── 📄 Jenkinsfile                   # Jenkins pipeline configuration
├── 📄 requirements.txt              # Python dependencies
├── 📄 pytest.ini                    # Pytest configuration
├── 📄 conftest.py                   # Pytest fixtures and hooks
└── 📄 README.md                     # This file



🚀 Getting Started

⚙️ Prerequisites
Ensure you have the following installed before setting up the framework:

Python 3.8+ 🐍
Selenium WebDriver 🌐
Allure Commandline 📊
Jenkins (optional for CI/CD) 🔧

🔧 Installation Steps
1. Clone the repository:
  git clone https://github.com/your-repository.git
2. Install the required dependencies:
  pip install -r requirements.txt
3. Set up Allure for reporting:
  # For macOS:
brew install allure

  # For Ubuntu:
sudo apt-add-repository ppa:qameta/allure
sudo apt-get install allure

🧪 Running Tests

✅ Running all tests:
pytest --alluredir=reports/allure_results

🎯 Running a specific test:
pytest tests/e2e_tests/test_login.py --alluredir=reports/allure_results

📊 Generate Allure Report:
allure serve reports/allure_results

🚀 Jenkins CI/CD Pipeline

Integrate your tests into a Jenkins pipeline for automated test execution and reporting.

Example Jenkinsfile:- 

pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-repository.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=reports/allure_results'
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: 'reports/allure_results']]
            }
        }
    }
}


🏆 Contributing

Contributions are welcome! Feel free to fork this repository, create a feature branch, and submit a pull request. If you find any issues or have suggestions for improvements, 
don't hesitate to open an issue.

🎉 Thanks for checking out the framework! Let's automate with Python and Selenium! 💻✨















