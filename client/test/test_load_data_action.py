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
from openapi_client.models.load_data_action import LoadDataAction  # noqa: E501
from openapi_client.rest import ApiException

class TestLoadDataAction(unittest.TestCase):
    """LoadDataAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoadDataAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.load_data_action.LoadDataAction()  # noqa: E501
        if include_optional :
            return LoadDataAction(
                rel = '0', 
                value = openapi_client.models.load_data.LoadData(
                    content_type = '0', 
                    data = '0', 
                    file_schema = openapi_client.models.file_schema.FileSchema(
                        type = '0', ), 
                    file_syntax = openapi_client.models.file_syntax.FileSyntax(
                        type = '0', ), 
                    integration = openapi_client.models.integration.Integration(
                        type = '0', ), 
                    key = null, 
                    path = '0', 
                    type = 'LoadData', )
            )
        else :
            return LoadDataAction(
                rel = '0',
                value = openapi_client.models.load_data.LoadData(
                    content_type = '0', 
                    data = '0', 
                    file_schema = openapi_client.models.file_schema.FileSchema(
                        type = '0', ), 
                    file_syntax = openapi_client.models.file_syntax.FileSyntax(
                        type = '0', ), 
                    integration = openapi_client.models.integration.Integration(
                        type = '0', ), 
                    key = null, 
                    path = '0', 
                    type = 'LoadData', ),
        )

    def testLoadDataAction(self):
        """Test LoadDataAction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()