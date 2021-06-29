# RelationalAI Python SDK

[RelationalAI Python SDK](https://github.com/RelationalAI-oss/relationalai-sdk-python)
- API version: 1.1.3

This is a Client SDK for RelationalAI API

  For more information, please visit [https://www.relational.ai](https://www.relational.ai)

## Requirements

Building the python SDK requires:
1. python 3
2. poetry

## Installation

To install the SDK to your local poetry repository, you can run from the client directory:
```shell
# using poetry
poetry add relationalai-sdk
# using pip
pip install relationalai-sdk
```

### Connecting to local rai-server

To connect to a local rai-server you need to create a `LocalConnection`:
```python
>>> from relationalai import LocalConnection
>>> conn = LocalConnection(dbname="python_sdk_db")
>>> conn.create_database(overwrite=True)
```

### Connecting to RAICloud

To connect to RAICloud you need to create two connections:
1. `ManagementConnection` to manage RAICloud resources.
2. `Connection` to connect to a RAICloud compute.
```python
>>> from relationalai import Connection, ManagementConnection, RAIComputeSize, RAIComputeFilters

>>> mngt_conn = ManagementConnection()
>>> mngt_conn.create_compute(compute_name="python_sdk_compute", size=RAIComputeSize("XS"))
>>> filters = RAIComputeFilters(state=["PROVISIONED"])
>>> mngt_conn.list_computes(filters=filters)

>>> conn = Connection(mngt_conn=mngt_conn, compute_name="python_sdk_compute", dbname="python_sdk_db")
>>> conn.create_database(overwrite=True)

>>> mngt_conn.delete_compute(compute_name="python_sdk_compute")
```

## Getting dependencies using Nix:

You can get `python3` and `poetry` using `Nix`:
```shell
nix-shell -p poetry python3
```