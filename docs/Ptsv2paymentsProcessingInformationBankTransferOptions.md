# Ptsv2paymentsProcessingInformationBankTransferOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decline_avs_flags** | **str** | List of AVS flags that cause the request to be declined for AVS reasons. Use a space to separate the flags in the list. Important Make sure that you include the value N in the list if you want to receive declines for the AVS code N.  | [optional] 
**sec_code** | **str** | Authorization method used for the transaction. See \&quot;SEC Codes,\&quot; page 89.  TeleCheck Accepts only the following values: - **PPD** - **TEL** - **WEB**  | [optional] 
**terminal_city** | **str** | City in which the terminal is located. If more than four alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters.  | [optional] 
**terminal_state** | **str** | State in which the terminal is located. If more than two alphanumeric characters are submitted, the transaction will be declined.  You cannot include any special characters.  | [optional] 
**effective_date** | **str** | Effective date for the transaction. The effective date must be within 45 days of the current day. If you do not include this value, CyberSource sets the effective date to the next business day.  Format: &#x60;MMDDYYYY&#x60;  Supported only for the CyberSource ACH Service.  | [optional] 
**partial_payment_id** | **str** | Identifier for a partial payment or partial credit.  The value for each debit request or credit request must be unique within the scope of the order. See \&quot;Multiple Partial Credits,\&quot; page 41.  | [optional] 
**customer_memo** | **str** | Payment related information.  This information is included on the customer’s statement.  | [optional] 
**payment_category_code** | **str** | Flag that indicates whether to process the payment.  Use with deferred payments. See \&quot;Deferred and Partial Payments,\&quot; page 37.  Possible values: - **0**: Standard debit with immediate payment (default). - **1**: For deferred payments, indicates that this is a deferred payment and that you will send a debit request with &#x60;paymentCategoryCode &#x3D; 2&#x60; in the future. - **2**: For deferred payments, indicates notification to initiate payment.  Chase Paymentech Solutions and TeleCheck Use for deferred and partial payments.  CyberSource ACH Service Not used.  RBS WorldPay Atlanta Not used.  | [optional] 
**settlement_method** | **str** | Method used for settlement.  Possible values: - **A**: Automated Clearing House (default for credits and for transactions using Canadian dollars) - **F**: Facsimile draft (U.S. dollars only) - **B**: Best possible (U.S. dollars only) (default if the field has not already been configured for your merchant ID)  See \&quot;Settlement Delivery Methods,\&quot; page 44.  | [optional] 
**fraud_screening_level** | **str** | Level of fraud screening.  Possible values: - **1**: Validation — default if the field has not already been configured for your merchant ID - **2**: Verification  For a description of this feature and a list of supported processors, see \&quot;Verification and Validation,\&quot; page 24.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


