# VistaSoft Monitor Demo

This is a demo project for VistaSoft Monitor web application. This project is mainly to showcase test automation using Python and Cucumber.

## Pre-requisites
- Chromium Browser
- Python 3.12.xx or above
- any IDE that supports Python (such as VSCode or PyCharm)
-  Git 

## Installation
1. Clone this repository into a directory of your choosing. Run this command in a terminal :
   - `git clone https://github.com/ishlahasyraf/VistaSoftMonitorDemo path/to/directory/here`
2. Create your virtual environment first by running this command (while in the directory) :
   - `python -m venv venv`
3. Activate your virtual environment :
   - `venv/Scripts/Activate`
4. run this command to install the required libraries :
   - `pip install -r requirements.txt`
5. drop the .env file into the project directory.

## Run
- to perform tests, simply run the following command while in the directory:
  - `behave`
- Running the tests will generate test results using Allure library, and it is saved inside the 'output' folder. To view the test results in a report, run the following command while in the directory :
  - `allure serve output`
