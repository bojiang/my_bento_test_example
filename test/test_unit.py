import numpy as np


def test_preprocessing():
    from service import Preprocessing

    preprocessing_service = Preprocessing()

    example_input = np.random.rand(10, 10)
    assert (preprocessing_service.preprocess(example_input) == example_input).all()


def test_iris():
    from service import IrisClassifier

    iris_service = IrisClassifier()

    example_input = np.random.rand(1, 4)
    assert iris_service.classify(example_input) == [0]
