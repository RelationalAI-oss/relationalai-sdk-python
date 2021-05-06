# coding: utf-8

"""
    Delve Client SDK

    This is a Client SDK for Delve API  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ClientProblem(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'error_code': 'str',
        'is_error': 'bool',
        'is_exception': 'bool',
        'message': 'str',
        'path': 'str',
        'report': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'is_error': 'is_error',
        'is_exception': 'is_exception',
        'message': 'message',
        'path': 'path',
        'report': 'report'
    }

    def __init__(self, error_code='', is_error=False, is_exception=False, message='', path='', report='', local_vars_configuration=None):  # noqa: E501
        """ClientProblem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_code = None
        self._is_error = None
        self._is_exception = None
        self._message = None
        self._path = None
        self._report = None
        self.discriminator = None

        self.error_code = error_code
        self.is_error = is_error
        self.is_exception = is_exception
        self.message = message
        self.path = path
        self.report = report

    @property
    def error_code(self):
        """Gets the error_code of this ClientProblem.  # noqa: E501


        :return: The error_code of this ClientProblem.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ClientProblem.


        :param error_code: The error_code of this ClientProblem.  # noqa: E501
        :type error_code: str
        """
        if self.local_vars_configuration.client_side_validation and error_code is None:  # noqa: E501
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def is_error(self):
        """Gets the is_error of this ClientProblem.  # noqa: E501


        :return: The is_error of this ClientProblem.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this ClientProblem.


        :param is_error: The is_error of this ClientProblem.  # noqa: E501
        :type is_error: bool
        """
        if self.local_vars_configuration.client_side_validation and is_error is None:  # noqa: E501
            raise ValueError("Invalid value for `is_error`, must not be `None`")  # noqa: E501

        self._is_error = is_error

    @property
    def is_exception(self):
        """Gets the is_exception of this ClientProblem.  # noqa: E501


        :return: The is_exception of this ClientProblem.  # noqa: E501
        :rtype: bool
        """
        return self._is_exception

    @is_exception.setter
    def is_exception(self, is_exception):
        """Sets the is_exception of this ClientProblem.


        :param is_exception: The is_exception of this ClientProblem.  # noqa: E501
        :type is_exception: bool
        """
        if self.local_vars_configuration.client_side_validation and is_exception is None:  # noqa: E501
            raise ValueError("Invalid value for `is_exception`, must not be `None`")  # noqa: E501

        self._is_exception = is_exception

    @property
    def message(self):
        """Gets the message of this ClientProblem.  # noqa: E501


        :return: The message of this ClientProblem.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClientProblem.


        :param message: The message of this ClientProblem.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def path(self):
        """Gets the path of this ClientProblem.  # noqa: E501


        :return: The path of this ClientProblem.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ClientProblem.


        :param path: The path of this ClientProblem.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def report(self):
        """Gets the report of this ClientProblem.  # noqa: E501


        :return: The report of this ClientProblem.  # noqa: E501
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this ClientProblem.


        :param report: The report of this ClientProblem.  # noqa: E501
        :type report: str
        """
        if self.local_vars_configuration.client_side_validation and report is None:  # noqa: E501
            raise ValueError("Invalid value for `report`, must not be `None`")  # noqa: E501

        self._report = report

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientProblem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientProblem):
            return True

        return self.to_dict() != other.to_dict()