# Ptsv2paymentsidcapturesMerchantInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_descriptor** | [**Ptsv2paymentsMerchantInformationMerchantDescriptor**](Ptsv2paymentsMerchantInformationMerchantDescriptor.md) |  | [optional] 
**card_acceptor_reference_number** | **str** | Reference number that facilitates card acceptor/corporation communication and record keeping.  For processor-specific information, see the card_acceptor_ref_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  | [optional] 
**category_code** | **int** | Four-digit number that the payment card industry uses to classify merchants into market segments. Visa assigned one or more of these values to your business when you started accepting Visa cards.  If you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the merchant_category_code field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  See \&quot;Aggregator Support,\&quot; page 100.  **CyberSource through VisaNet**\\ The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code  | [optional] 
**vat_registration_number** | **str** | Your government-assigned tax identification number.  For CtV processors, the maximum length is 20.  For other processor-specific information, see the merchant_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  | [optional] 
**service_fee_descriptor** | [**Ptsv2paymentsMerchantInformationServiceFeeDescriptor**](Ptsv2paymentsMerchantInformationServiceFeeDescriptor.md) |  | [optional] 
**tax_id** | **str** | Your Cadastro Nacional da Pessoa Jurídica (CNPJ) number.  This field is supported only for BNDES transactions on CyberSource through VisaNet. See BNDES.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR6 - Position: 40-59 - Field: BNDES Reference Field 1  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


