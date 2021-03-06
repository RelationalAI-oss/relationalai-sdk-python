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
from rai_api.model.client_problem import ClientProblem
from rai_api.model.exception_problem import ExceptionProblem
from rai_api.model.integrity_constraint_problem import IntegrityConstraintProblem
from rai_api.model.integrity_constraint_violation import IntegrityConstraintViolation
from rai_api.model.output_problem import OutputProblem
from rai_api.model.persist_problem import PersistProblem
from rai_api.model.storage_problem import StorageProblem
from rai_api.model.syntax_error import SyntaxError
from rai_api.model.workspace_load_problem import WorkspaceLoadProblem
globals()['ClientProblem'] = ClientProblem
globals()['ExceptionProblem'] = ExceptionProblem
globals()['IntegrityConstraintProblem'] = IntegrityConstraintProblem
globals()['IntegrityConstraintViolation'] = IntegrityConstraintViolation
globals()['OutputProblem'] = OutputProblem
globals()['PersistProblem'] = PersistProblem
globals()['StorageProblem'] = StorageProblem
globals()['SyntaxError'] = SyntaxError
globals()['WorkspaceLoadProblem'] = WorkspaceLoadProblem
from rai_api.model.abstract_problem import AbstractProblem


class TestAbstractProblem(unittest.TestCase):
    """AbstractProblem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAbstractProblem(self):
        """Test AbstractProblem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AbstractProblem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
