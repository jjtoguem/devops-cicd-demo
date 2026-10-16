# DevOps CI/CD Demo

Projet fil rouge pour apprendre le CI/CD avec GitHub Actions.

## Prérequis
- Python 3.12 (obligatoire)
- pip

## Contenu
- app/ : code Python
- tests/ : tests unitaires
- .github/workflows/ : pipelines CI/CD

## Installation

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Lancer les tests en local

    python3 -m pytest -v
    <!-- Test de la protection de branche -->
    <!-- Test bypass : refus attendu -->
