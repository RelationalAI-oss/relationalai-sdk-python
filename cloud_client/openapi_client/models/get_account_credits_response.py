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


class GetAccountCreditsResponse(object):
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
        'start_period': 'datetime',
        'end_period': 'datetime',
        'compute': 'ComputeCreditsInfo',
        'storage': 'StorageCreditsInfo'
    }

    attribute_map = {
        'start_period': 'start_period',
        'end_period': 'end_period',
        'compute': 'compute',
        'storage': 'storage'
    }

    def __init__(self, start_period=None, end_period=None, compute=None, storage=None, local_vars_configuration=None):  # noqa: E501
        """GetAccountCreditsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_period = None
        self._end_period = None
        self._compute = None
        self._storage = None
        self.discriminator = None

        if start_period is not None:
            self.start_period = start_period
        if end_period is not None:
            self.end_period = end_period
        if compute is not None:
            self.compute = compute
        if storage is not None:
            self.storage = storage

    @property
    def start_period(self):
        """Gets the start_period of this GetAccountCreditsResponse.  # noqa: E501


        :return: The start_period of this GetAccountCreditsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._start_period

    @start_period.setter
    def start_period(self, start_period):
        """Sets the start_period of this GetAccountCreditsResponse.


        :param start_period: The start_period of this GetAccountCreditsResponse.  # noqa: E501
        :type start_period: datetime
        """

        self._start_period = start_period

    @property
    def end_period(self):
        """Gets the end_period of this GetAccountCreditsResponse.  # noqa: E501


        :return: The end_period of this GetAccountCreditsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._end_period

    @end_period.setter
    def end_period(self, end_period):
        """Sets the end_period of this GetAccountCreditsResponse.


        :param end_period: The end_period of this GetAccountCreditsResponse.  # noqa: E501
        :type end_period: datetime
        """

        self._end_period = end_period

    @property
    def compute(self):
        """Gets the compute of this GetAccountCreditsResponse.  # noqa: E501


        :return: The compute of this GetAccountCreditsResponse.  # noqa: E501
        :rtype: ComputeCreditsInfo
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """Sets the compute of this GetAccountCreditsResponse.


        :param compute: The compute of this GetAccountCreditsResponse.  # noqa: E501
        :type compute: ComputeCreditsInfo
        """

        self._compute = compute

    @property
    def storage(self):
        """Gets the storage of this GetAccountCreditsResponse.  # noqa: E501


        :return: The storage of this GetAccountCreditsResponse.  # noqa: E501
        :rtype: StorageCreditsInfo
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this GetAccountCreditsResponse.


        :param storage: The storage of this GetAccountCreditsResponse.  # noqa: E501
        :type storage: StorageCreditsInfo
        """

        self._storage = storage

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
        if not isinstance(other, GetAccountCreditsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAccountCreditsResponse):
            return True

        return self.to_dict() != other.to_dict()