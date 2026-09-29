"""Tests unitaires de la calculatrice."""
import pytest

from app.calculatrice import additionner, soustraire, multiplier, diviser


def test_additionner():
    assert additionner(2, 3) == 5


def test_soustraire():
    assert soustraire(10, 4) == 6


def test_multiplier():
    assert multiplier(3, 4) == 12


def test_diviser():
    assert diviser(10, 2) == 5


def test_diviser_par_zero():
    with pytest.raises(ValueError):
        diviser(10, 0)
