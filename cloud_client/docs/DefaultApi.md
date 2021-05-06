# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_credits_get**](DefaultApi.md#account_credits_get) | **GET** /account/credits | Get account credits consumption
[**compute_delete**](DefaultApi.md#compute_delete) | **DELETE** /compute | Delete compute
[**compute_get**](DefaultApi.md#compute_get) | **GET** /compute | List computes
[**compute_put**](DefaultApi.md#compute_put) | **PUT** /compute | Create compute
[**database_get**](DefaultApi.md#database_get) | **GET** /database | List databases
[**database_post**](DefaultApi.md#database_post) | **POST** /database | Update database
[**list_compute_events**](DefaultApi.md#list_compute_events) | **GET** /compute/{computeId}/events | List compute events
[**user_get**](DefaultApi.md#user_get) | **GET** /user | List users
[**user_put**](DefaultApi.md#user_put) | **PUT** /user | Create user


# **account_credits_get**
> GetAccountCreditsResponse account_credits_get(period=period)

Get account credits consumption

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    period = 'period_example' # str |  (optional)

    try:
        # Get account credits consumption
        api_response = api_instance.account_credits_get(period=period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->account_credits_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**|  | [optional] 

### Return type

[**GetAccountCreditsResponse**](GetAccountCreditsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Credits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_delete**
> DeleteComputeResponseProtocol compute_delete(delete_compute_request_protocol)

Delete compute

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    delete_compute_request_protocol = openapi_client.DeleteComputeRequestProtocol() # DeleteComputeRequestProtocol | Compute to be deleted

    try:
        # Delete compute
        api_response = api_instance.compute_delete(delete_compute_request_protocol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->compute_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_compute_request_protocol** | [**DeleteComputeRequestProtocol**](DeleteComputeRequestProtocol.md)| Compute to be deleted | 

### Return type

[**DeleteComputeResponseProtocol**](DeleteComputeResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compute deletion status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_get**
> ListComputesResponseProtocol compute_get(id=id, name=name, size=size, state=state)

List computes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = ['id_example'] # list[str] |  (optional)
name = ['name_example'] # list[str] |  (optional)
size = ['size_example'] # list[str] |  (optional)
state = ['state_example'] # list[str] |  (optional)

    try:
        # List computes
        api_response = api_instance.compute_get(id=id, name=name, size=size, state=state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->compute_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | [optional] 
 **name** | [**list[str]**](str.md)|  | [optional] 
 **size** | [**list[str]**](str.md)|  | [optional] 
 **state** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ListComputesResponseProtocol**](ListComputesResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Computes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_put**
> CreateComputeResponseProtocol compute_put(create_compute_request_protocol)

Create compute

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    create_compute_request_protocol = openapi_client.CreateComputeRequestProtocol() # CreateComputeRequestProtocol | New compute

    try:
        # Create compute
        api_response = api_instance.compute_put(create_compute_request_protocol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->compute_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_compute_request_protocol** | [**CreateComputeRequestProtocol**](CreateComputeRequestProtocol.md)| New compute | 

### Return type

[**CreateComputeResponseProtocol**](CreateComputeResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New compute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_get**
> ListDatabasesResponseProtocol database_get(id=id, name=name, state=state)

List databases

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = ['id_example'] # list[str] |  (optional)
name = ['name_example'] # list[str] |  (optional)
state = ['state_example'] # list[str] |  (optional)

    try:
        # List databases
        api_response = api_instance.database_get(id=id, name=name, state=state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->database_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | [optional] 
 **name** | [**list[str]**](str.md)|  | [optional] 
 **state** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ListDatabasesResponseProtocol**](ListDatabasesResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Databases |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_post**
> database_post(update_database_request_protocol)

Update database

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    update_database_request_protocol = openapi_client.UpdateDatabaseRequestProtocol() # UpdateDatabaseRequestProtocol | Database fields to be updated

    try:
        # Update database
        api_instance.database_post(update_database_request_protocol)
    except ApiException as e:
        print("Exception when calling DefaultApi->database_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_database_request_protocol** | [**UpdateDatabaseRequestProtocol**](UpdateDatabaseRequestProtocol.md)| Database fields to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_events**
> ListComputeEventsResponse list_compute_events(compute_id)

List compute events

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    compute_id = 'compute_id_example' # str | 

    try:
        # List compute events
        api_response = api_instance.list_compute_events(compute_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_compute_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_id** | **str**|  | 

### Return type

[**ListComputeEventsResponse**](ListComputeEventsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> ListUsersResponseProtocol user_get()

List users

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        # List users
        api_response = api_instance.user_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUsersResponseProtocol**](ListUsersResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_put**
> CreateUserResponseProtocol user_put(create_user_request_protocol)

Create user

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    create_user_request_protocol = openapi_client.CreateUserRequestProtocol() # CreateUserRequestProtocol | New user

    try:
        # Create user
        api_response = api_instance.user_put(create_user_request_protocol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request_protocol** | [**CreateUserRequestProtocol**](CreateUserRequestProtocol.md)| New user | 

### Return type

[**CreateUserResponseProtocol**](CreateUserResponseProtocol.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
