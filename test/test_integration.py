import subprocess
import time

import bentoml


def test_iris():
    with subprocess.Popen(
        ["bentoml", "serve", "-p", "50001"],
    ) as server_proc:
        print("Waiting for server to be ready")
        time.sleep(8)

        with bentoml.SyncHTTPClient("http://localhost:50001") as client:
            print("Begin testing")
            result = client.classify(
                input_series=[[5.1, 3.5, 1.4, 0.2]],
            )
            assert result == [0]

        print("Waiting for server to shutdown")
        server_proc.terminate()
