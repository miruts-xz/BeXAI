# Created by mire on 7/21/21. Copyright 2021, All rights reserved.
import pandas as pd
import numpy as np
import sklearn.datasets
import os
import datasets

supported_datasets = {
    'regression': {

    },
    'classification': {

    }
}


class Data:
    def __init__(self, name: str, task_type: str):
        assert name in supported_datasets[
            task_type].keys(), f'The dataset is not supported at the moment. Datasets supported are: {list(supported_datasets.keys())}'
        self.name = name
        self.task_type = task_type
        self.data = supported_datasets[task_type][name]()
        self.data_class = None
