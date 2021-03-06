"""
    Delve Client SDK

    This is a Client SDK for Delve API  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rai_api
from rai_api.model.azure_integration import AzureIntegration
from rai_api.model.default_integration import DefaultIntegration
from rai_api.model.s3_integration import S3Integration
globals()['AzureIntegration'] = AzureIntegration
globals()['DefaultIntegration'] = DefaultIntegration
globals()['S3Integration'] = S3Integration
from rai_api.model.integration import Integration


class TestIntegration(unittest.TestCase):
    """Integration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIntegration(self):
        """Test Integration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Integration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
