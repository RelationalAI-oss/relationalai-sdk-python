# coding: utf-8

"""
    RAI Cloud SDK

    This is a Client SDK for RAI Cloud  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.delete_compute_status import DeleteComputeStatus  # noqa: E501
from openapi_client.rest import ApiException

class TestDeleteComputeStatus(unittest.TestCase):
    """DeleteComputeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeleteComputeStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.delete_compute_status.DeleteComputeStatus()  # noqa: E501
        if include_optional :
            return DeleteComputeStatus(
                name = '0', 
                state = '0', 
                message = '0'
            )
        else :
            return DeleteComputeStatus(
        )

    def testDeleteComputeStatus(self):
        """Test DeleteComputeStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()