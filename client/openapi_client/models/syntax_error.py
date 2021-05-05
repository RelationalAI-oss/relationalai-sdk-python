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


class SyntaxError(object):
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
        'next': 'SyntaxNode',
        'node': 'SyntaxNode',
        'trace': 'LinkedList'
    }

    attribute_map = {
        'next': 'next',
        'node': 'node',
        'trace': 'trace'
    }

    def __init__(self, next=None, node=None, trace=None, local_vars_configuration=None):  # noqa: E501
        """SyntaxError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next = None
        self._node = None
        self._trace = None
        self.discriminator = None

        if next is not None:
            self.next = next
        self.node = node
        self.trace = trace

    @property
    def next(self):
        """Gets the next of this SyntaxError.  # noqa: E501


        :return: The next of this SyntaxError.  # noqa: E501
        :rtype: SyntaxNode
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this SyntaxError.


        :param next: The next of this SyntaxError.  # noqa: E501
        :type next: SyntaxNode
        """

        self._next = next

    @property
    def node(self):
        """Gets the node of this SyntaxError.  # noqa: E501


        :return: The node of this SyntaxError.  # noqa: E501
        :rtype: SyntaxNode
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SyntaxError.


        :param node: The node of this SyntaxError.  # noqa: E501
        :type node: SyntaxNode
        """
        if self.local_vars_configuration.client_side_validation and node is None:  # noqa: E501
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def trace(self):
        """Gets the trace of this SyntaxError.  # noqa: E501


        :return: The trace of this SyntaxError.  # noqa: E501
        :rtype: LinkedList
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this SyntaxError.


        :param trace: The trace of this SyntaxError.  # noqa: E501
        :type trace: LinkedList
        """
        if self.local_vars_configuration.client_side_validation and trace is None:  # noqa: E501
            raise ValueError("Invalid value for `trace`, must not be `None`")  # noqa: E501

        self._trace = trace

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
        if not isinstance(other, SyntaxError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SyntaxError):
            return True

        return self.to_dict() != other.to_dict()
