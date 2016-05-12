import argparse
import models
import logging
import importlib

def main():
    args = parse_args()
    logging.basicConfig(level=(logging.WARN if args.verbose else logging.INFO))
    model = importlib.import_module("models."+args.model_spec).Model()
    print(dir(model), args)

    model.train()

def parse_args():
    parser = argparse.ArgumentParser(description="Given a named module spec, a dataset, and some hyperparameters for training - train the model and save it to the default output directory")
    parser.add_argument("model_spec", type=str, help="the name of one of the predefined model specs, can be found in /models")
    parser.add_argument("--lr", dest="lr", default='0.001', help='the learning rate for training')
    parser.add_argument("--dataset", dest="dataset", default='data.lmdb', help='the dataset to train the model against. Must be an LMDB file with inputs and outputs to train against')
    parser.add_argument("--tag", dest="tag", help="the tag used to identify the model in the pavlov directory and to name the regularly saved checkpoint files")
    parser.add_argument("-v","--verbose", action="store_true", help="Don't log progress to stderr.")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
