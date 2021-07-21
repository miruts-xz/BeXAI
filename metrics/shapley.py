# Created by mire on 7/21/21. Copyright 2021, All rights reserved.
import numpy as np
import enum


class ShapleyMode(enum.Enum):
    MSE = 1  # Mean squared error
    RMSE = 2  # Root mean squared error
    MAE = 3  # Mean absolute error


class Shapley:
    def __init__(self, model, trained_model, dataset, mode='mse'):
        self.model = model
        self.trained_model = trained_model
        self.dataset = dataset
        self.mode = mode

    def evaluate(self, X, y, feature_weights, gt_weights, X_train=None, y_train=None, X_train_feature_weights=None):
        error = None
        if self.mode == ShapleyMode.MSE:
            error = np.sum(np.square(feature_weights - gt_weights))
        elif self.mode == ShapleyMode.RMSE:
            error = np.sqrt(np.sum(np.square(feature_weights - gt_weights)))
        elif self.mode == ShapleyMode.MAE:
            error = np.sum(np.abs(feature_weights - gt_weights))
        error /= (feature_weights.shape[0] * feature_weights.shape[1])
        return error
