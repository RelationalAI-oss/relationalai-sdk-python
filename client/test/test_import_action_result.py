# coding: utf-8

"""
    Delve Client SDK

    This is a Client SDK for Delve API  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.import_action_result import ImportActionResult  # noqa: E501
from openapi_client.rest import ApiException

class TestImportActionResult(unittest.TestCase):
    """ImportActionResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImportActionResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.import_action_result.ImportActionResult()  # noqa: E501
        if include_optional :
            return ImportActionResult(
                dummy = '0'
            )
        else :
            return ImportActionResult(
        )

    def testImportActionResult(self):
        """Test ImportActionResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()