### Table of Contents
- [Installation](#installation)
- [Usage](#usage)


# Installation
>[!NOTE]
>do ensure the following pre-requisites are installed first :
>- Python
>- Allure
>- Visual Studio Code (or PyCharm)
>- pip

1. Clone the repository by running the following script in a terminal
    : `git clone https://github.com/ishlahasyraf/VistaSoftMonitorDemo.git "your directory"
`
2. drop the .env file into the directory
3. open code editor of choice and open the folder
4. create a virtual environment by running the following script in a terminal : `python -m venv "your virtual env name"`
5. run the following script to install the required libraries : `pip install -r requirements.txt`

# Usage
- to perform tests, simply run the following script in a terminal(while in the directory) : `behave`
- Running the tests will automatically generate Allure test results in the `output` folder, which will be automatically generated once a test has been completed.
- to generate an Allure Report, run the following script in a terminal(while in the directory) : `allure serve output`
