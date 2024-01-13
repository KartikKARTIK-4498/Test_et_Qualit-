# Project: Unit Testing and Code Quality in Python

## Group Members
- [Member 1 Full Name]
- [Member 2 Full Name]
- [Member 3 Full Name]
## Project Description
This project focuses on implementing unit tests and improving code quality in a Python project. The tools used include SonarQube, pytest, coverage, and Flake8. The project includes a simple calculator that interacts with the user to perform basic mathematical operations.


## Installation and Execution Instructions
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:
  ```bash
pip install pytest coverage flake8 pytest-html
```
4. if you want to have pytest-html report
  ```bash
python -m pytest --html=report.html
 ```
5. if you want to have flake8 -html report
  ```bash
python -m flake8 --format=html --htmldir=flake8-report .
 ```
5. if you want to have coverage html report
  ```bash
coverage html
 ```

6. Run the project using the following command:
   ```bash
   python main.py

## Unit Testing and Code Quality
Exercise 1: Creating tests for basic operations

- Implemented MathOperations class with methods for addition, subtraction, multiplication, and division.

- Wrote pytest tests for each operation in the tests/test_math_operations.py file.

Exercise 2: Adding power with parameterization

- Extended MathOperations class with a power method.

- Created parameterized tests for the power method using pytest.

Exercise 3: Improvement with modulo calculation and HTML report

- Added a modulo method to the MathOperations class.

- Implemented parameterized tests for the modulo method using pytest.

Exercise 4: Interactive main function

- Created a main function for user interaction and calculation.

- Implemented parameterized tests for the main function using pytest.
## Exercise 5: Evaluating test coverage
- Used pytest to run tests and measured test coverage.
  ``` bash
   coverage run -m pytest -v
Generated coverage report-html.
```bash
python -m pytest --html=report.html
```
- Generated coverage report and integrated it with pytest-html.
```bash
coverage html
```

- Checked code style violations using Flake8 and generated an HTML report
```bash
python -m flake8 --format=html --htmldir=flake8-report .
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

