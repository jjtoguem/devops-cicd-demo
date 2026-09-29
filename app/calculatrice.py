"""Petite calculatrice pour apprendre le CI/CD."""


def additionner(a: float, b: float) -> float:
    """Retourne la somme de a et b."""
    return a + b


def soustraire(a: float, b: float) -> float:
    """Retourne la différence a - b."""
    return a - b


def multiplier(a: float, b: float) -> float:
    """Retourne le produit de a et b."""
    return a * b


def diviser(a: float, b: float) -> float:
    """Retourne a / b. Lève une erreur si b vaut 0."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
