# coding: utf-8

"""
    RAI Cloud SDK

    This is a Client SDK for RAI Cloud  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DeleteComputeRequestProtocol(object):
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
        'name': 'str',
        'dryrun': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'dryrun': 'dryrun'
    }

    def __init__(self, name=None, dryrun=None, local_vars_configuration=None):  # noqa: E501
        """DeleteComputeRequestProtocol - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._dryrun = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dryrun is not None:
            self.dryrun = dryrun

    @property
    def name(self):
        """Gets the name of this DeleteComputeRequestProtocol.  # noqa: E501


        :return: The name of this DeleteComputeRequestProtocol.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteComputeRequestProtocol.


        :param name: The name of this DeleteComputeRequestProtocol.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def dryrun(self):
        """Gets the dryrun of this DeleteComputeRequestProtocol.  # noqa: E501


        :return: The dryrun of this DeleteComputeRequestProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._dryrun

    @dryrun.setter
    def dryrun(self, dryrun):
        """Sets the dryrun of this DeleteComputeRequestProtocol.


        :param dryrun: The dryrun of this DeleteComputeRequestProtocol.  # noqa: E501
        :type dryrun: bool
        """

        self._dryrun = dryrun

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
        if not isinstance(other, DeleteComputeRequestProtocol):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteComputeRequestProtocol):
            return True

        return self.to_dict() != other.to_dict()
