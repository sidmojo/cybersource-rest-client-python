# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2paymentsMerchantInformationServiceFeeDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'contact': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'state': 'state'
    }

    def __init__(self, name=None, contact=None, state=None):
        """
        Ptsv2paymentsMerchantInformationServiceFeeDescriptor - a model defined in Swagger
        """

        self._name = None
        self._contact = None
        self._state = None

        if name is not None:
          self.name = name
        if contact is not None:
          self.contact = contact
        if state is not None:
          self.state = state

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        Name of the service provider that is collecting the service fee. The service provider name must consist of 3, 7, or 12 characters followed by an asterisk (*). This value must also include the words “Service Fee.”  When you include more than one consecutive space, extra spaces are removed. Use one of the following formats for this value: - <3-character name>*Service Fee - <7-character name>*Service Fee - <12-character name>*Service Fee  When payments are made in installments, this value must also include installment information such as “1 of 5” or “3 of 7.” For installment payments, use one of the following formats for this value: - <3-character name>*Service Fee*<N> of <M> - <7-character name>*Service Fee*<N> of <M> - <12-character name>*Service Fee*<N> of <M>  where <N> is the payment number and <M> is the total number of payments.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :return: The name of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        Name of the service provider that is collecting the service fee. The service provider name must consist of 3, 7, or 12 characters followed by an asterisk (*). This value must also include the words “Service Fee.”  When you include more than one consecutive space, extra spaces are removed. Use one of the following formats for this value: - <3-character name>*Service Fee - <7-character name>*Service Fee - <12-character name>*Service Fee  When payments are made in installments, this value must also include installment information such as “1 of 5” or “3 of 7.” For installment payments, use one of the following formats for this value: - <3-character name>*Service Fee*<N> of <M> - <7-character name>*Service Fee*<N> of <M> - <12-character name>*Service Fee*<N> of <M>  where <N> is the payment number and <M> is the total number of payments.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :param name: The name of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :type: str
        """
        if name is not None and len(name) > 22:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `22`")

        self._name = name

    @property
    def contact(self):
        """
        Gets the contact of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        Contact information for the service provider that is collecting the service fee. when you include more than one consecutive space, extra spaces are removed.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :return: The contact of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        Contact information for the service provider that is collecting the service fee. when you include more than one consecutive space, extra spaces are removed.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :param contact: The contact of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :type: str
        """
        if contact is not None and len(contact) > 11:
            raise ValueError("Invalid value for `contact`, length must be less than or equal to `11`")

        self._contact = contact

    @property
    def state(self):
        """
        Gets the state of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        State or territory in which the service provider is located.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :return: The state of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        State or territory in which the service provider is located.  When you do not include this value in your request, CyberSource uses the value that is in your CyberSource account.  This value might be displayed on the cardholder’s statement. 

        :param state: The state of this Ptsv2paymentsMerchantInformationServiceFeeDescriptor.
        :type: str
        """
        if state is not None and len(state) > 20:
            raise ValueError("Invalid value for `state`, length must be less than or equal to `20`")

        self._state = state

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2paymentsMerchantInformationServiceFeeDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other