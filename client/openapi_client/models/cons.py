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


class Cons(object):
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
        'head': 'SyntaxNode',
        'tail': 'LinkedList'
    }

    attribute_map = {
        'head': 'head',
        'tail': 'tail'
    }

    def __init__(self, head=None, tail=None, local_vars_configuration=None):  # noqa: E501
        """Cons - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._head = None
        self._tail = None
        self.discriminator = None

        self.head = head
        self.tail = tail

    @property
    def head(self):
        """Gets the head of this Cons.  # noqa: E501


        :return: The head of this Cons.  # noqa: E501
        :rtype: SyntaxNode
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this Cons.


        :param head: The head of this Cons.  # noqa: E501
        :type head: SyntaxNode
        """
        if self.local_vars_configuration.client_side_validation and head is None:  # noqa: E501
            raise ValueError("Invalid value for `head`, must not be `None`")  # noqa: E501

        self._head = head

    @property
    def tail(self):
        """Gets the tail of this Cons.  # noqa: E501


        :return: The tail of this Cons.  # noqa: E501
        :rtype: LinkedList
        """
        return self._tail

    @tail.setter
    def tail(self, tail):
        """Sets the tail of this Cons.


        :param tail: The tail of this Cons.  # noqa: E501
        :type tail: LinkedList
        """
        if self.local_vars_configuration.client_side_validation and tail is None:  # noqa: E501
            raise ValueError("Invalid value for `tail`, must not be `None`")  # noqa: E501

        self._tail = tail

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
        if not isinstance(other, Cons):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cons):
            return True

        return self.to_dict() != other.to_dict()
