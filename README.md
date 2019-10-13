# Python Client SDK for the CyberSource REST API

The CyberSource Python client provides convenient access to the [CyberSource REST API](https://developer.cybersource.com/api/reference/api-reference.html) from your Python application.

## Requirements

* Python 3.4 or later

## Installation

* Install the Cybersource Python client using the below command

```
pip install cybersource-rest-client-python
```

## Registration & Configuration
Use of this SDK and the CyberSource APIs requires having an account on our system. You can find details of getting a test account and creating your keys [here](https://developer.cybersource.com/api/developer-guides/dita-gettingstarted/registration.html) 

Remember this SDK is for use in server-side Python applications that access the CyberSource REST API and credentials should always be securely stored and accessed appropriately. 


## SDK Usage Examples and Sample Code
To get started using this SDK, it is highly recommended to download our sample code repository:
* [Cybersource Python Sample Code Repository (on GitHub)](https://github.com/CyberSource/cybersource-rest-samples-python)

In that respository, we have comprehensive sample code for all common uses of our API:

Additionally, you can find details and examples of how our API is structured in our API Reference Guide:
* [Developer Center API Reference](https://developer.cybersource.com/api/reference/api-reference.html)

The API Reference Guide provides examples of what information is needed for a particular request and how that information would be formatted. Using those examples, you can easily determine what methods would be necessary to include that information in a request using this SDK.


### Switching between the sandbox environment and the production environment
Cybersource maintains a complete sandbox environment for testing and development purposes. This sandbox environment is an exact duplicate of our production environment with the transaction authorization and settlement process simulated. By default, this SDK is configured to communicate with the sandbox environment. To switch to the production environment, set the `run_environment` property in the SDK Configuration.  See our sample at https://github.com/CyberSource/cybersource-rest-samples-python/blob/master/data/Configuration.py

```python
 #For TESTING use
  self.run_environment = "CyberSource.Environment.SANDBOX"
#For PRODUCTION use
#self.run_environment = "CyberSource.Environment.PRODUCTION"
```

API credentials are different for each environment, so be sure to switch to the appropriate credentials when switching environments.



## License
This repository is distributed under a proprietary license.
