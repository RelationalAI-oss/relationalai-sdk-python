"""
    Delve Client SDK

    This is a Client SDK for Delve API  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: support@relational.ai
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "rai_sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="Delve Client SDK",
    author="Delve Client SDK Support",
    author_email="support@relational.ai",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Delve Client SDK"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    This is a Client SDK for Delve API  # noqa: E501
    """
)
