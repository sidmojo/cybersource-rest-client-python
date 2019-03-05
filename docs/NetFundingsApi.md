# CyberSource.NetFundingsApi

All URIs are relative to *https://apitest.cybersource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_net_funding_info**](NetFundingsApi.md#get_net_funding_info) | **GET** /reporting/v3/net-fundings | Get Netfunding information for an account or a merchant


# **get_net_funding_info**
> ReportingV3NetFundingsGet200Response get_net_funding_info(start_time, end_time, organization_id=organization_id, group_name=group_name)

Get Netfunding information for an account or a merchant

Get Netfunding information for an account or a merchant.

### Example 
```python
from __future__ import print_function
import time
import CyberSource
from CyberSource.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = CyberSource.NetFundingsApi()
start_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX 
end_time = '2013-10-20T19:20:30+01:00' # datetime | Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ssXXX 
organization_id = 'organization_id_example' # str | Valid Cybersource Organization Id (optional)
group_name = 'group_name_example' # str | Valid CyberSource Group Name. (optional)

try: 
    # Get Netfunding information for an account or a merchant
    api_response = api_instance.get_net_funding_info(start_time, end_time, organization_id=organization_id, group_name=group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFundingsApi->get_net_funding_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX  | 
 **end_time** | **datetime**| Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX  | 
 **organization_id** | **str**| Valid Cybersource Organization Id | [optional] 
 **group_name** | **str**| Valid CyberSource Group Name. | [optional] 

### Return type

[**ReportingV3NetFundingsGet200Response**](ReportingV3NetFundingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
