import pandas as pd
from cobra.core import Model

from camilo import maps, list_experiments, get_model


def test_maps():
    assert 'Core_metabolism' in dir(maps)
    assert isinstance(maps.Core_metabolism, list)


def test_experiments():
    assert isinstance(list_experiments(), pd.DataFrame)


def test_model():
    assert isinstance(get_model(162, 22), Model)
