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
from rai_api.model.action import Action
from rai_api.model.query_action_all_of import QueryActionAllOf
from rai_api.model.relation import Relation
from rai_api.model.source import Source
globals()['Action'] = Action
globals()['QueryActionAllOf'] = QueryActionAllOf
globals()['Relation'] = Relation
globals()['Source'] = Source
from rai_api.model.query_action import QueryAction


class TestQueryAction(unittest.TestCase):
    """QueryAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueryAction(self):
        """Test QueryAction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueryAction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
