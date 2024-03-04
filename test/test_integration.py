import subprocess
import time

import bentoml


def test_iris():
    with subprocess.Popen(["bentoml", "serve", "-p", "50001"]) as server_proc:
        try:
            time.sleep(8)  # wait for server to start
            with bentoml.SyncHTTPClient("http://localhost:50001") as client:
                # Test predict
                assert client.classify(input_series=[[5.1, 3.5, 1.4, 0.2]]) == [0]
        finally:
            server_proc.terminate()
