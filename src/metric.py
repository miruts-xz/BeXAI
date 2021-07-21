# Created by mire on 7/21/21. Copyright 2021, All rights reserved.
import metrics

supported_metrics = {
    'shapley': metrics.Shapley
}


class Metric:
    def __init__(self, name):
        assert name in supported_metrics.keys(), f'This metric is not supported. supported metrics are {list(supported_metrics.keys())}'
        self.name = name
        self.metric = lambda model, trained_model, data_class: supported_metrics[name](model, trained_model, data_class)
        self.evaluate = supported_metrics[name].evaluate
