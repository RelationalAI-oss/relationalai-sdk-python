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


class OutputProblemAllOf(object):
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
        'exception': 'str',
        'exception_stacktrace': 'str',
        'name': 'str'
    }

    attribute_map = {
        'exception': 'exception',
        'exception_stacktrace': 'exception_stacktrace',
        'name': 'name'
    }

    def __init__(self, exception='', exception_stacktrace=None, name='', local_vars_configuration=None):  # noqa: E501
        """OutputProblemAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exception = None
        self._exception_stacktrace = None
        self._name = None
        self.discriminator = None

        self.exception = exception
        self.exception_stacktrace = exception_stacktrace
        self.name = name

    @property
    def exception(self):
        """Gets the exception of this OutputProblemAllOf.  # noqa: E501


        :return: The exception of this OutputProblemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this OutputProblemAllOf.


        :param exception: The exception of this OutputProblemAllOf.  # noqa: E501
        :type exception: str
        """
        if self.local_vars_configuration.client_side_validation and exception is None:  # noqa: E501
            raise ValueError("Invalid value for `exception`, must not be `None`")  # noqa: E501

        self._exception = exception

    @property
    def exception_stacktrace(self):
        """Gets the exception_stacktrace of this OutputProblemAllOf.  # noqa: E501


        :return: The exception_stacktrace of this OutputProblemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._exception_stacktrace

    @exception_stacktrace.setter
    def exception_stacktrace(self, exception_stacktrace):
        """Sets the exception_stacktrace of this OutputProblemAllOf.


        :param exception_stacktrace: The exception_stacktrace of this OutputProblemAllOf.  # noqa: E501
        :type exception_stacktrace: str
        """

        self._exception_stacktrace = exception_stacktrace

    @property
    def name(self):
        """Gets the name of this OutputProblemAllOf.  # noqa: E501


        :return: The name of this OutputProblemAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OutputProblemAllOf.


        :param name: The name of this OutputProblemAllOf.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, OutputProblemAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OutputProblemAllOf):
            return True

        return self.to_dict() != other.to_dict()
