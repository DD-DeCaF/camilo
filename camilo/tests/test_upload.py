"""
Tests for the upload module

doesn't actually test the upload since that required communication with an iloop server but checks that valid /
invalid files are detected

 """
import camilo.upload as cup
from os.path import abspath, join, dirname
import pandas as pd
import pytest
import json


@pytest.fixture(scope='session')
def examples():
    return abspath(join(dirname(abspath(__file__)), "..", "data", "examples"))


def test_media_inspection(examples):
    up = cup.MediaUploader('TST', join(examples, 'media.csv'))
    assert isinstance(up.df, pd.DataFrame)
    with pytest.raises(ValueError) as excinfo:
        cup.MediaUploader('TST', join(examples, 'media-invalid.csv'))
        report = json.loads(str(excinfo))
        assert report['error-count'] == 1
        error = report['tables']['errors'].pop()
        assert 'not a compound' in error['message']


def test_strains_inspection(examples):
    up = cup.StrainsUploader('TST', join(examples, 'strains.csv'))
    assert isinstance(up.df, pd.DataFrame)
    with pytest.raises(ValueError) as excinfo:
        cup.StrainsUploader('TST', join(examples, 'strains-invalid.csv'))
        report = json.loads(str(excinfo))
        assert report['error-count'] == 1
        error = report['tables']['errors'].pop()
        assert 'bad expected gnomic' in error['message']


def test_experiment_inspection(examples):
    up = cup.ExperimentUploader('TST', join(examples, 'samples.csv'), join(examples, 'physiology.csv'))
    assert isinstance(up.samples_df, pd.DataFrame)
    assert isinstance(up.physiology_df, pd.DataFrame)
