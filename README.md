#CloudPassage SDK Examples

Version: *2.0 - 2016.11.03*
<br />
Author: *John Alexander* - *jalexander@cloudpassage.com*

The CloudPassage SDK was authored by Ash Wilson. This Python script (cp_sdk_examples.py) includes
examples of using the CloudPasage SDK library to call the CloudPassage REST API.

The CloudPassage SDK is an SDK for using the CloudPassage Halo REST API. The primary purpose
of the CloudPassage SDK is to make the CloudPassage API much easier to use, and it can help get you up
and running in as little as 30 minutes. 

The CloudPassage SDK provides a method to do authentication to the Halo API server, and provides
a significant number of methods that can easily be used to make Halo API calls. 
This example code is heavily documented and meant to serve as a tutorial on how to use the
CloudPassage SDK and to help get started very quickly with it.

##Requirements and Dependencies

To run, the (cp_sdk_examples.py) script requires:

* Python installed on the host that runs the script. (Python 2.7.11 or a higher 2.7.x version)
* The Python built-in module: json (note: All of these Python modules come with the standard default installation of Python, so you shouldn't need to do anything to include them.)
* A Halo API Key: read-only key (for GETs) or full-access key (For PUTs, POSTs, and DELETEs); Get the key and copy it from the Halo Portal.


##List of Files

* **The CloudPassage SDK** - See Toolbox for instructions on how to install it.
* **cp_sdk_examples.py**  -  The Python script that provides examples on how to use the CloudPassage SDK. This is the script you want to run.
* **cassandra-linux-v1.policy.json**  -  This is a pre-built Halo CSM policy that is used in several of the examples.
* **README.md**  -  This ReadMe file
* **LICENSE.txt**  -  License from CloudPassage



##Usage

1. Copy the two-part Halo API key from the Halo Portal into the proper location in the cpapi_example.py script.
2. Copy cpapi_examples.py, cpapi.py, and the cassandra-linux-v1.policy.json file to your host.
2. Make sure Python can find the cassandra-linux-v1.policy.json file (i.e. path is set correctly)
3. Make sure Python can find the cpapi.py file (i.e. path is set correctly)
4. Execute the cpapi_example.py script.

##Acknowledgements
Thanks to Ash Wilson for creating the Python CloudPassage SDK.
Note: Apurva Singh wrote CPAPI, which pre-dates CloudPassage SDK.

<!---
#CPTAGS:community-supported api-example
#TBICON:images/python_icon.png
-->
