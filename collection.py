import h2oai_client
import numpy as np
import pandas as pd
# import h2o
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('settings', type=str, nargs='')
parser.add_argument('train', type=str, nargs='')
parser.add_argument('test', type=str, nargs='')

address = 'http://localhost:8080'
username = 'username'
password = 'password'
h2oai = Client(address = address, username = username, password = password)

train = h2oai.create_dataset_sync(args.train)
test = h2oai.create_dataset_sync(args.test)

target="default payment next month"
exp_preview = h2oai.get_experiment_preview_sync(dataset_key= train.key,
                                                validset_key='',
                                                classification=True,
                                                dropped_cols = [],
                                                target_col=target,
                                                time_col = '',
                                                enable_gpus = True,
                                                accuracy = 5,
                                                time = 5,
                                                interpretability = 5,
                                                config_overrides = None)

experiment = h2oai.start_experiment_sync(dataset_key = train.key,
                                         testset_key = test.key,
                                         target_col = target,
                                         is_classification = True,
                                         accuracy = 6,
                                         time = 3,
                                         interpretability = 6,
                                         scorer = "AUC",
                                         seed = 1234)

print("Final Model Score on Validation Data: " + str(round(experiment.valid_score, 3)))
print("Final Model Score on Test Data: " + str(round(experiment.test_score, 3)))
