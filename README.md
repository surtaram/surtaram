# Simple Book API Testing

### Author: Vinutha

Welcome to the **Simple Book API Testing** repository! This project provides a robust framework for testing a simple book API, utilizing modern tools and best practices in software development.

---

## 📚 Tech Stack

- **Python**: The programming language used for writing tests and implementing logic.
- **Requests**: A powerful library for making HTTP requests with ease.
- **PyTest**: A flexible testing framework that allows for writing simple as well as complex test cases.
- **Allure Report**: A beautiful reporting framework that provides a detailed overview of test results.

---

## 🚀 How to Install Packages

To get started, you'll need to install the required packages. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
---

## 🏃 How to Run Test Cases

To execute the test cases, use the following command:

```bash
pytest -n 2 -v --host=staging
```
Command Breakdown:
-n 2: This runs the tests in parallel, utilizing 2 CPU cores for faster execution.
-v: Enables verbose output, providing more details during the test run.
--host=staging: Specifies the environment for the tests.
---

## 📊 Viewing Reports
After running your tests, you can generate and view the Allure reports to get insights into your test results. Follow these steps:

Make sure you have Allure installed on your system.
Run the following command to generate the report:

```bash
allure serve
```
---
## Test Report

<img width="1546" alt="Screenshot 2024-09-21 at 11 04 29 AM" src="https://github.com/user-attachments/assets/e23f60c3-9bfa-4ffb-8f25-56ba138b167c">

## 🌟 Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please feel free to submit a pull request or open an issue.

Thank you for checking out this repository! Happy testing! 🎉