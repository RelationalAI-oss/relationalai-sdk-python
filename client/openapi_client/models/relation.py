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


class Relation(object):
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
        'columns': 'list[list[object]]',
        'rel_key': 'RelKey',
        'type': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'rel_key': 'rel_key',
        'type': 'type'
    }

    def __init__(self, columns=None, rel_key=None, type='Relation', local_vars_configuration=None):  # noqa: E501
        """Relation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._columns = None
        self._rel_key = None
        self._type = None
        self.discriminator = None

        self.columns = columns
        self.rel_key = rel_key
        self.type = type

    @property
    def columns(self):
        """Gets the columns of this Relation.  # noqa: E501


        :return: The columns of this Relation.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Relation.


        :param columns: The columns of this Relation.  # noqa: E501
        :type columns: list[list[object]]
        """

        self._columns = columns

    @property
    def rel_key(self):
        """Gets the rel_key of this Relation.  # noqa: E501


        :return: The rel_key of this Relation.  # noqa: E501
        :rtype: RelKey
        """
        return self._rel_key

    @rel_key.setter
    def rel_key(self, rel_key):
        """Sets the rel_key of this Relation.


        :param rel_key: The rel_key of this Relation.  # noqa: E501
        :type rel_key: RelKey
        """
        if self.local_vars_configuration.client_side_validation and rel_key is None:  # noqa: E501
            raise ValueError("Invalid value for `rel_key`, must not be `None`")  # noqa: E501

        self._rel_key = rel_key

    @property
    def type(self):
        """Gets the type of this Relation.  # noqa: E501


        :return: The type of this Relation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Relation.


        :param type: The type of this Relation.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Relation"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, Relation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Relation):
            return True

        return self.to_dict() != other.to_dict()
