# Projet: Les Tests Unitaires et la Qualité

## Les membres du groupe

- Kartik Kartik
- Chetana OLI
- Krishnaraj KONGANAPURAM CHIDAMBARAM
- Alioune badara FALL


## Description du projet

Ce projet se concentre sur la mise en œuvre de tests unitaires et l'amélioration de la qualité du code dans un projet Python. Les outils utilisés incluent SonarQube, pytest, couverture et Flake8. Le projet comprend une simple calculatrice qui interagit avec l'utilisateur pour effectuer des opérations mathématiques de base.

## Instructions d'installation et d'exécution

1. Clonez ce référentiel sur votre ordinateur local.
2. Accédez au répertoire du projet.
3. Installez les dépendances requises :

```bash
pip install pytest coverage flake8 pytest-html
```

4. si vous voulez avoir un rapport pytest-html

```bash
python -m pytest --html=report.html
```

5. si vous voulez avoir un rapport flake8 -html

```bash
python -m flake8 --format=html --htmldir=flake8-report .
```

5. si vous souhaitez avoir un rapport HTML de couverture

```bash
coverage html
```

6. Exécutez le projet à l'aide de la commande suivante :
   ```bash
   python main.py
   ```

## Unit Testing and Code Quality

#### Exo 1 : Création de tests pour les opérations de base :
1. Créez une classe MathOperations dans un fichier main.py contenant des méthodes pour 
l'addition, la soustraction, la multiplication et la division.
2. Utilisez pytest pour écrire une suite de tests pour chaque opération, couvrant différents cas 
(entiers, décimaux, négatifs, etc.).
3. Assurez-vous de tester les cas limites et les cas d'erreur.
   
#### Exo 2 : Ajout de la puissance avec paramétrisation :
1. Ajoutez une méthode power à la classe MathOperations pour le calcul de la puissance.
2. Utilisez pytest avec la paramétrisation pour créer des tests avec différents jeux de données 
afin de vous assurer que la méthode fonctionne correctement.

#### Exo 3 : Amélioration avec le calcul du modulo et rapport HTML :
1. Ajoutez une méthode modulo à la classe MathOperations pour le calcul du modulo.
2. Utilisez pytest avec la paramétrisation pour tester différentes combinaisons de nombres 
pour cette nouvelle méthode.

#### Exo 4 : Fonction main interactive :
1. À la suite de vos fonctions, créez une fonction main qui ne prend aucun argument.
2. Cette méthode demande à l'utilisateur de saisir des éléments à calculer et effectue 
l’opération demandée en utilisant les fonctions précédemment créées.
3. Utilisez pytest avec la paramétrisation pour tester différentes combinaisons d'entrées 
utilisateur.

#### Exo 5 : Évaluation de la couverture des tests :
1. Utilisez pytest pour exécuter les tests.
2. Utilisez le module coverage pour mesurer la couverture des tests.
3. Modifiez vos tests si nécessaire pour atteindre une couverture complète.
4. Générez un rapport de couverture pour évaluer la qualité des tests.
5. Générez un rapport de style de code avec flake8-html pour identifier les violations de la PEP 
8 et corrigez-les. 
6. Intégrez également le rapport HTML avec pytest-html pour visualiser les résultats.
7. Votre code devra être testé sur sonar Qube et présenter la meilleure note possible.
## Exercise 5: Evaluating test coverage

- Utilisé pytest pour exécuter des tests et mesurer la couverture des tests.
  ```bash
   coverage run -m pytest -v
  Generated coverage report-html.
  ```

```bash
python -m pytest --html=report.html
```

![pytest report](./images/coverage.png)

- Génération d'un rapport de couverture et intégration avec pytest-html.

```bash
coverage html
```

![coverage report](./images/coverage.png)

- Vérification des violations de style de code à l'aide de Flake8 et génération d'un rapport HTML

```bash
python -m flake8 --format=html --htmldir=flake8-report .
```

![flake8 report](./images/flake8.png)

- Le résultat des calculs :

```bash
python main.py
```

![output calulation](./images/output.png)


Veuillez vous assurer de mettre à jour les tests le cas échéant.


