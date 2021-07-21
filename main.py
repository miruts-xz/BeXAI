import sys
import os
import json
import argparse


def get_args():
    parser = argparse.ArgumentParser("Main driver for BeXAI")
    parser.add_argument("--type",
                        default='classification',
                        choices=['classification', 'regression'],
                        help="Type of task, classification or regression?",
                        )
    parser.add_argument('--dataset',
                        help='Name of the dataset to train on',
                        )
    parser.add_argument('--model',
                        help='Algorithm to use for training',
                        )
    parser.add_argument('--metric',
                        default='shapley',
                        choices=['shapley', 'faithfulness'],
                        )
    args = parser.parse_args()
    return args


def process_args():
    pass
