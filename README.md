# Selenium Automation Pipeline with Jenkins and AWS

This project demonstrates a robust CI/CD pipeline for automation testing, leveraging AWS EC2, Jenkins, and Python Selenium. It is designed to handle environment-specific challenges and provide real-time feedback through automated reporting.

---

## Live Test Dashboard (Guest Access)
To verify the live pipeline and build history, I have provided Read-Only access to the Jenkins dashboard.

<details>
  <summary>Click to show Jenkins Credentials</summary>

  * **Dashboard URL**: http://16.58.119.172:8080
  * **Guest ID**: guest
  * **Guest PW**: guest8989

</details>

---

## Automated Test Scenarios
To ensure application stability, the following automated test cases were implemented:

### 1. End-to-End (E2E) Purchase Flow
* **Objective**: Verifies the complete customer journey, including product selection, cart management, and the final checkout process.
* **Scope**: Automated execution of the full transaction cycle: accessing the landing page, adding items to the shopping cart, navigating to the checkout page, selecting the shipping region, and submitting the final order.
* **Key Validation**: Ensures cross-page data persistence and successful transaction completion in a production-like environment.

### 2. Form Submission and Data Integrity
* **Objective**: Validates the input handling mechanism and successful data submission.
* **Scope**: Automated entry of diverse data types, boundary value testing, and verification of success/error messaging.
* **Key Validation**: Confirms that backend-bound data is correctly processed and that the UI provides appropriate feedback to the user.

---

## Technical Stack
* **Language**: Python 3.14
* **Framework**: Pytest, Selenium WebDriver
* **Infrastructure**: AWS EC2 (Windows Server - Ohio Region)
* **CI/CD**: Jenkins
* **Reporting**: JUnit XML, Gmail SMTP (Real-time Email Notifications)

---

## System Architecture
(Insert Architecture Diagram Here)
* **Local Development**: Code authored in PyCharm and pushed to GitHub (dev to main branches).
* **Jenkins Automation**: Jenkins detects changes and triggers automated test execution on an AWS EC2 instance.
* **Headless Optimization**: Tests run in Chrome Headless mode with optimized viewport settings (1920x1080) for resource efficiency and stability.
* **Result Notification**: Automated reports are dispatched via Gmail SMTP upon build completion (Success/Failure).
