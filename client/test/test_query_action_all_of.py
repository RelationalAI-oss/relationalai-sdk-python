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
from openapi_client.models.query_action_all_of import QueryActionAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestQueryActionAllOf(unittest.TestCase):
    """QueryActionAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test QueryActionAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.query_action_all_of.QueryActionAllOf()  # noqa: E501
        if include_optional :
            return QueryActionAllOf(
                inputs = [
                    openapi_client.models.relation.Relation(
                        columns = [
                            [
                                null
                                ]
                            ], 
                        rel_key = openapi_client.models.rel_key.RelKey(
                            keys = [
                                '0'
                                ], 
                            name = '0', 
                            values = [
                                '0'
                                ], 
                            type = 'RelKey', ), 
                        type = 'Relation', )
                    ], 
                outputs = [
                    '0'
                    ], 
                persist = [
                    '0'
                    ], 
                source = openapi_client.models.source.Source(
                    name = '0', 
                    path = '0', 
                    value = '0', 
                    type = 'Source', )
            )
        else :
            return QueryActionAllOf(
                source = openapi_client.models.source.Source(
                    name = '0', 
                    path = '0', 
                    value = '0', 
                    type = 'Source', ),
        )

    def testQueryActionAllOf(self):
        """Test QueryActionAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
