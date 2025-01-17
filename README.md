## Solution Overview

"In order to effectively address the problem at hand, I first identified the specific requirements and objectives. I then conducted a thorough analysis of the expected outcomes and formulated a design plan based on a modular architecture. I also incorporated three design patterns that I believed would be most suitable for the task. Through this process, I was able to develop a comprehensive and reliable solution that met all the necessary requirements using a modular architecture and the selected design patterns."

## Architecture explanation

The modular architecture was adopted for this solution due to its ability to decompose the system into smaller, independent components. These components are more amenable to testing and maintenance, and, upon identification of the requirements, can be tailored to specific functions. As a result, the modular architecture was deemed the most suitable approach for this project.

## Aproach and methodology

In my approach, I utilized design patterns to ensure that the program could accommodate additional functions or changes to inputs. Also having in mind to fullfill with SOLID principles, to do this, I followed the following steps:

    1. I compiled a list of requirements '

    2. created a UML diagram to abstractly represent the modules that would be necessary.

    3. I identified design patterns that could be applied to these modules to facilitate scalability and maintainability.

        3.1 The first pattern was Factory method to create the Employees, as a form to be able to extend the types of employees

        3.2 The second consideration was strategy, which allows for easy maintenance and flexibility in managing and storing the data collected from the input. This strategy facilitates the ability to make changes as needed. this was used for ParseSchedule module"

        3.3 The final consideration was the use of the template method design pattern, which allows for scalable modifications to be made to the algorithm, including the ability to add or alter steps as needed. This pattern was implemented in the counting module due to the potential for changes to the counting algorithm, while maintaining certain consistent steps such as the function to print the results.

    4. I implemented tests to validate the effectiveness of the chosen design patterns.

### How to Run 🔧

In case you are from the batch, go to the directory of the project then

go to src, once in this directory run the script with "python main.py"

In case you wanna try another file for input, make sure it has de the name "file.txt" and it is in the same level as main.py file

for testing, from the terminal go to src directory of the project and run the command "python -m pytest test/"

Make sure to have pytest Library globally to run the test, if not follow the next steps to create a virtual env and install pytest

    1. For create environment, from the terminal go to directory of the project, make sure to be in the same level as src folder, then run the command "python -m venv venv"

    2. Activate the environment, for windows in the terminal at the same level of venv folder run the command ".\venv\Scripts\activate"

    3.Once the environment is activated, install pytest library with the command "pip install pytest"

    4. with the virtual env activated in the terminal go to src folder with the command "cd src/" and then run the command "python -m pytest test/"
