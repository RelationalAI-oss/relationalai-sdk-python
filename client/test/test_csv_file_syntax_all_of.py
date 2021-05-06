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
from openapi_client.models.csv_file_syntax_all_of import CSVFileSyntaxAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestCSVFileSyntaxAllOf(unittest.TestCase):
    """CSVFileSyntaxAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CSVFileSyntaxAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.csv_file_syntax_all_of.CSVFileSyntaxAllOf()  # noqa: E501
        if include_optional :
            return CSVFileSyntaxAllOf(
                datarow = 56, 
                delim = '0', 
                escapechar = '0', 
                header = [
                    '0'
                    ], 
                header_row = 56, 
                ignorerepeated = True, 
                missingstrings = [
                    '0'
                    ], 
                normalizenames = True, 
                quotechar = '0'
            )
        else :
            return CSVFileSyntaxAllOf(
                datarow = 56,
                delim = '0',
                escapechar = '0',
                header_row = 56,
                ignorerepeated = True,
                normalizenames = True,
                quotechar = '0',
        )

    def testCSVFileSyntaxAllOf(self):
        """Test CSVFileSyntaxAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()