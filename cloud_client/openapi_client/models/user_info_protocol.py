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


class UserInfoProtocol(object):
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
        'account_name': 'str',
        'username': 'str',
        'status': 'str',
        'access_key1': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'username': 'username',
        'status': 'status',
        'access_key1': 'access_key1',
        'created_by': 'created_by'
    }

    def __init__(self, account_name=None, username=None, status=None, access_key1=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """UserInfoProtocol - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_name = None
        self._username = None
        self._status = None
        self._access_key1 = None
        self._created_by = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if access_key1 is not None:
            self.access_key1 = access_key1
        if created_by is not None:
            self.created_by = created_by

    @property
    def account_name(self):
        """Gets the account_name of this UserInfoProtocol.  # noqa: E501


        :return: The account_name of this UserInfoProtocol.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this UserInfoProtocol.


        :param account_name: The account_name of this UserInfoProtocol.  # noqa: E501
        :type account_name: str
        """

        self._account_name = account_name

    @property
    def username(self):
        """Gets the username of this UserInfoProtocol.  # noqa: E501


        :return: The username of this UserInfoProtocol.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserInfoProtocol.


        :param username: The username of this UserInfoProtocol.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def status(self):
        """Gets the status of this UserInfoProtocol.  # noqa: E501


        :return: The status of this UserInfoProtocol.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserInfoProtocol.


        :param status: The status of this UserInfoProtocol.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def access_key1(self):
        """Gets the access_key1 of this UserInfoProtocol.  # noqa: E501


        :return: The access_key1 of this UserInfoProtocol.  # noqa: E501
        :rtype: str
        """
        return self._access_key1

    @access_key1.setter
    def access_key1(self, access_key1):
        """Sets the access_key1 of this UserInfoProtocol.


        :param access_key1: The access_key1 of this UserInfoProtocol.  # noqa: E501
        :type access_key1: str
        """

        self._access_key1 = access_key1

    @property
    def created_by(self):
        """Gets the created_by of this UserInfoProtocol.  # noqa: E501


        :return: The created_by of this UserInfoProtocol.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserInfoProtocol.


        :param created_by: The created_by of this UserInfoProtocol.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

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
        if not isinstance(other, UserInfoProtocol):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInfoProtocol):
            return True

        return self.to_dict() != other.to_dict()