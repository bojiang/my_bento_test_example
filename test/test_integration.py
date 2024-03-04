import subprocess
import time

import bentoml


def test_iris():
    with subprocess.Popen(
        ["bentoml", "serve", "-p", "50000"],
    ):
        with bentoml.SyncHTTPClient("http://localhost:50000") as client:
            print("Waiting for server to be ready")
            time.sleep(5)
            print("Begin testing")
            result = client.classify(
                input_series=[[5.1, 3.5, 1.4, 0.2]],
            )
            assert result == [0]
