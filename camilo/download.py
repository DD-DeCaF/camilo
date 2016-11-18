import pandas as pd
from camilo import iloop_client

iloop = iloop_client()


def scalar_data_frame(experiments):
    for exp_id in experiments:
        exp_obj = iloop.Experiment.first(where={'identifier': exp_id})
        operations = pd.melt(pd.DataFrame(exp_obj.attributes['operation'], index=[0]),
                             var_name='reactor', value_name='operation')

