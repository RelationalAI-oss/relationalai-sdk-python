# openapi_client.DefaultApi

All URIs are relative to *http://127.0.0.1:8010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_post**](DefaultApi.md#transaction_post) | **POST** /transaction | Issues a transaction to be executed


# **transaction_post**
> TransactionResult transaction_post(transaction)

Issues a transaction to be executed

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8010
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:8010"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    transaction = openapi_client.Transaction() # Transaction | Optional description in *Markdown*

    try:
        # Issues a transaction to be executed
        api_response = api_instance.transaction_post(transaction)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->transaction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction** | [**Transaction**](Transaction.md)| Optional description in *Markdown* | 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful result is wrapped inside a TransactionResult |  -  |
**422** | The transaction was aborted. The result is wrapped inside a TransactionResult |  -  |
**403** | Unauthorized |  -  |
**0** | All errors are also wrapped inside a TransactionResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

