from sdk import RAIRequest, RAICredentials, RAIConfig

import unittest
import datetime

class TestSignature(unittest.TestCase):

    def testSignature(self):
        t = datetime.datetime(2020, 5, 4, 10, 36, 0)
        method = "GET"
        body = "{}"
        url = "http://127.0.0.1:8010/database"

        headers = dict()
        headers["host"] = "127.0.0.1"
        headers["content-type"] = "application/json"

        query_params = []

        rai_credentials = RAICredentials(
            private_key = "krnXRBoE0lX6NddvryxKIE+7RWrkWg6xk8NcGaSOdCo=", # pragma: allowlist secret
            access_key = "e3536f8d-cbc6-4ed8-9de6-74cf4cb724a1" # pragma: allowlist secret
        )
        rai_config = RAIConfig()
        rai_config.creds = rai_credentials
        rai_config.region = "us-east"

        rai_request = RAIRequest(rai_config=rai_config, method=method, url=url, body=body, headers=headers, service="database+list")

        rai_request.sign(t=t, debug_level=2)

        self.assertEqual(rai_request.headers["authorization"], "RAI01-ED25519-SHA256 Credential=e3536f8d-cbc6-4ed8-9de6-74cf4cb724a1/20200504/us-east/database+list/rai01_request, SignedHeaders=content-type;host;x-rai-date, Signature=77d211417454ded42dc931d25c57af6cab6cbc70f75bef4c849d37585188d659158c8c944eab866e3147bbcde21257ae0a1dfece3c0f3f43a838b3f9524e0f0a")

if __name__ == '__main__':
    unittest.main()

