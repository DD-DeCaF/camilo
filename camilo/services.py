from cameo.core import to_solver_based_model
from cobra.io.json import _from_dict as model_from_dict
import re
from requests import get
import pandas as pd

from camilo.settings import Default

API_ADDRESS = Default.API_ADDRESS + '/{}'


def list_experiments():
    exp = (pd.DataFrame(get(API_ADDRESS.format('experiments'),
                            headers=Default.headers).json()).
           rename(str, {'id': 'experiment', 'name': 'experiment_name'}))
    samples_list = []
    for exp_id in exp.experiment:
        sample_request = get(
            API_ADDRESS.format('experiments/{}/samples').format(exp_id),
            headers=Default.headers)
        samples_for_exp = pd.DataFrame(sample_request.json()).rename(
            str, {'id': 'sample_id'})
        samples_for_exp['experiment'] = exp_id
        phase_list = []
        for sample_id in samples_for_exp.sample_id:
            phases_json = (get(API_ADDRESS.format('samples/{}/phases')
                               .format(sample_id), headers=Default.headers)
                           .json())
            phases_for_sample = pd.DataFrame(phases_json).rename(str, {
                'id': 'phase_id', 'name': 'phase_name'})
            phases_for_sample['sample_id'] = sample_id
            phase_list.append(phases_for_sample)
        phases = pd.concat(phase_list)
        samples_list.append(pd.merge(samples_for_exp, phases, on='sample_id'))
    samples = pd.concat(samples_list)
    result = pd.merge(exp, samples, on='experiment')
    return result


def get_model(sample_id, phase_id):
    response = (get(API_ADDRESS.format('samples/{}/model')
                    .format(sample_id), headers=Default.headers)
                .json())
    return to_solver_based_model(
        model_from_dict(response[str(phase_id)]['model']))


def make_name(name):
    pattern = re.compile('\W|^(?=\d)')
    return re.sub(pattern, '_', name)


class Maps(object):
    def __init__(self):
        self._index = None
        self._model_to_map = None

    def _index_maps(self):
        self._model_to_map = get(API_ADDRESS.format('maps')).json()
        self._index = pd.DataFrame([(map_name, model) for model, map_list in
                                    self._model_to_map.items()
                                    for map_name in map_list],
                                   columns=['map', 'model'])
        self._index.index = self._index.map.apply(make_name)

    def __dir__(self):
        if self._index is None:
            self._index_maps()
        return list(self._index.index)

    def __getattr__(self, item):
        if self._index is None:
            self._index_maps()
        try:
            map_name, model = self._index.loc[item].iloc[0]
        except ValueError:
            map_name, model = self._index.loc[item]
        return get(API_ADDRESS.format('map'),
                   params={'model': model, 'map': map_name}).json()


maps = Maps()
