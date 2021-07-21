# Created by mire on 7/21/21. Copyright 2021, All rights reserved.

import shap
import methods

supported_methods = {
    'shap': methods.Shape,
    'lime': methods.Lime,
    'kernelshap': methods.KernelShap
}


class Explainer:
    def __init__(self, name):
        assert (name in supported_methods[name].keys(),
                f'This Method is not supported at the moment. Methods support are {list(supported_methods.keys())}')
        self.name = name
        self.method = lambda clf, data: supported_methods[name](clf, data)
