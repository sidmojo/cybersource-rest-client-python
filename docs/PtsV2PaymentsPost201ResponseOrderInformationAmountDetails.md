# PtsV2PaymentsPost201ResponseOrderInformationAmountDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_amount** | **str** | Amount you requested for the payment or capture.  This value is returned for partial authorizations.  | [optional] 
**authorized_amount** | **str** | Amount that was authorized.  | [optional] 
**currency** | **str** | Currency used for the order. Use the three-character ISO Standard Currency Codes.  For an authorization reversal (&#x60;reversalInformation&#x60;) or a capture (&#x60;processingOptions.capture&#x60; is set to &#x60;true&#x60;), you must use the same currency that you used in your request for Payment API.  **DCC for First Data**\\ Your local currency. For details, see \&quot;Dynamic Currency Conversion for First Data,\&quot; page 113.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


