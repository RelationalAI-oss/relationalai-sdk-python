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
from openapi_client.models.modify_workspace_action_all_of import ModifyWorkspaceActionAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestModifyWorkspaceActionAllOf(unittest.TestCase):
    """ModifyWorkspaceActionAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModifyWorkspaceActionAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.modify_workspace_action_all_of.ModifyWorkspaceActionAllOf()  # noqa: E501
        if include_optional :
            return ModifyWorkspaceActionAllOf(
                delete_edb = '0', 
                delete_source = [
                    '0'
                    ], 
                enable_library = '0'
            )
        else :
            return ModifyWorkspaceActionAllOf(
        )

    def testModifyWorkspaceActionAllOf(self):
        """Test ModifyWorkspaceActionAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
