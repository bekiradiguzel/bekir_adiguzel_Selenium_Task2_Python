# **Insider Job Application E2E Test**

This project contains an End-to-End (E2E) test suite developed using Python and Selenium WebDriver to automate a specific flow on the Insider careers website.

## **Project Goal**

The primary objective of the test is to:

1. Navigate to the Insider homepage and accept cookies.  
2. Navigate to the "Company" section and then the "Careers" page.  
3. Scroll down to the job listings section.  
4. Filter the job listings by **Location** (e.g., Istanbul, Turkiye).  
5. Filter the job listings by **Department** (e.g., Quality Assurance).  
6. Click the first resulting job listing.  
7. Verify successful navigation to the external job application platform (Lever).

## **Prerequisites**

To run these tests, you must have the following installed:

* **Python 3.x**  
* **Selenium WebDriver**  
* A suitable browser driver (e.g., **ChromeDriver**). Ensure the driver version matches your Chrome browser version and is accessible in your system's PATH.

## **Setup Instructions**

1. **Clone the Repository:**  
   git clone \[your-repo-link\]  
   cd \[your-repo-name\]

2. **Create and Activate a Virtual Environment (Recommended):**  
   python \-m venv venv  
   \# On Windows:  
   .\\venv\\Scripts\\activate  
   \# On macOS/Linux:  
   source venv/bin/activate

3. **Install Dependencies:**  
   pip install selenium

   *(Note: Assuming pages/home\_page.py and Locators.py are present)*

## **Running the Tests**

The main test file is located at tests/test\_job\_application.py.

Execute the test using your chosen test runner (e.g., pytest):

pytest tests/test\_job\_application.py  
