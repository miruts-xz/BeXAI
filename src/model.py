# Created by mire on 7/21/21. Copyright 2021, All rights reserved.
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

supported_models = {
    'regression': {
        'lr': LinearRegression,
        'mlp': MLPRegressor,
        'dt': DecisionTreeRegressor,
        'rf': RandomForestRegressor,
    },
    'classification': {
        'lr': LinearRegression,
        'mlp': MLPClassifier,
        'dt': DecisionTreeClassifier,
        'rf': RandomForestClassifier
    }
}


class Model:
    def __init__(self, name, task_type):
        assert (name in supported_models[task_type].keys())
        self.name = name
        self.task_type = task_type
        self.model = supported_models[task_type][name]()
        self.predict = self.model.predict
        if self.model.fit:
            self.train = self.model.fit
