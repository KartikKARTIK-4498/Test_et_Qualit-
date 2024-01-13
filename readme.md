# Project: Tests Unitaires et la Qualité du Code en Python

## Group Members
- Kartik Kartik
- Chetana OLI
- Krishnaraj KONGANAPURAM CHIDAMBARAM
- Alioune badara FALL

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
####Exo 1 : Création de tests pour les opérations de base :
1. Créez une classe MathOperations dans un fichier main.py contenant des méthodes pour 
l'addition, la soustraction, la multiplication et la division.
2. Utilisez pytest pour écrire une suite de tests pour chaque opération, couvrant différents cas 
(entiers, décimaux, négatifs, etc.).
3. Assurez-vous de tester les cas limites et les cas d'erreur.
Exo 2 : Ajout de la puissance avec paramétrisation :
1. Ajoutez une méthode power à la classe MathOperations pour le calcul de la puissance.
2. Utilisez pytest avec la paramétrisation pour créer des tests avec différents jeux de données 
afin de vous assurer que la méthode fonctionne correctement.
Exo 3 : Amélioration avec le calcul du modulo et rapport HTML :
1. Ajoutez une méthode modulo à la classe MathOperations pour le calcul du modulo.
2. Utilisez pytest avec la paramétrisation pour tester différentes combinaisons de nombres 
pour cette nouvelle méthode.
Exo 4 : Fonction main interactive :
1. À la suite de vos fonctions, créez une fonction main qui ne prend aucun argument.
2. Cette méthode demande à l'utilisateur de saisir des éléments à calculer et effectue 
l’opération demandée en utilisant les fonctions précédemment créées.
3. Utilisez pytest avec la paramétrisation pour tester différentes combinaisons d'entrées 
utilisateur.
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

