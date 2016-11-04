""" cp_sdk_examples.py is a set of simple working examples to
    illustrate the use of the cloudpassage sdk."""

# cloudpassage SDK Examples (cp_sdk_examples.py)
#
# The cloudpassage sdk allows you to make Halo API calls with a
# minimal knowledge of REST and REST APIs. The cloudpassage sdk
# does all the "initialization" scaffolding work for you in
# several simple method calls.
#
# cp_sdk_examples.py is a set of simple examples that show you how to
# use the cloudpassage sdk. From creating your initial session object
# and then using it to make cloudpassage sdk method calls that in turn
# make Halo REST API calls.
#
# Initialization of the session object (session) is one line of code.
# Getting the authorization token is one line of code.
# Making a Halo API call using a cloudpassage sdk method call -- is
# typically only one line of code.
# Many of the classes in the cloudpassage sdk have a list_all() method
# that allows you to get most of the data associated with the endpoint
# represented by that class. The data returned by the list_all()
# methods can then be manipulated using Python list and dictionary
# indexing operations.
#
# The Halo API makes heavy use of JSON.  JSON is the data
# format that you use to transfer data to and from the Halo API server.
# Thus, you need to import Python's json module so you can work with
# data that is in the JSON format, and of course you also need to
# import the cloudpassage module. Recommend the use PIP to install the
# cloudpassage sdk library. See the cloudpassage sdk documentation for
# detailed installation instructions. You need to make sure your
# Python interpreter can find the cloudpassage sdk library.
#
# For simplicity (ease of use) this set of examples makes use of a
# pre-created Apache CSM policy, to illustrate loading and deletng
# Halo policies. Place this example policy file where your Python
# interpreter can find it. Usually the best place is to use the
# same location where cp_sdk_examples.py is being executed from.
#
# Created: 2015.12.14
# Last Modified: 2016.11.03.0

# Python built-in modules:
import json

# Third-party modules:
import cloudpassage

# Note: The cloudpassage SDK has a few dependencies, one is that
# pyyaml must be installed.


def create_api_session(session):
    """Get keys from config file, create session and get authtoken."""

    # A Halo API key (id key and secret) can be obtained via the
    # Halo user interface (UI). Just cut-and-paste them from the
    # Halo UI from your Halo account into a cloudpassage.yaml config
    # file. See the attached cloudpassage.yaml sample file included
    # in this project, to see how the yaml config file should be
    # populated.
    # You can set the value of the variable "config_file_location"
    # to the full path to the cloudpassage.yaml config file.
    # The APIKeyManager class then allows you to read the key
    # informationfrom the clouspassage.yaml config file. The
    # api_key and secret_key are set in two of the instance
    # variables of the ApiKeyManager object, you can access them
    # and pass them into the call that creates the session object.
    # The default is just to set the configuration file location
    # to the file name. In this case the config file must be in
    # the same location you are running the example progam from.
    # This is an example of a path that is written to work on
    # MS Windows. You see the double backslashes, because
    # inside of a string the backslash is a special character
    # and you need to escape the backslashes.
    # config_file_loc = "c:\\users\\john blake\\desktop\\" \
    #                   "python\\examples\\cloudpassage.yaml"
    # An example of a string that will work on Linux or Mac OS X
    # is included, here forward slashes are used which are not
    # special characters in a string.
    # config_file_loc = "/home/jalex/scripts/cloudpassage.yaml"

    config_file_loc = "cloudpassage.yaml"

    config_info = cloudpassage.ApiKeyManager(config_file=config_file_loc)

    print config_info.key_id
    print config_info.secret_key
    print config_info.api_hostname

    session = cloudpassage.HaloSession(config_info.key_id, config_info.secret_key)

    return session


# ----EXAMPLE #1 ------------------------
# Creating a server object by using the "Server"
# Class gives you a list of all the servers in your Halo account.
# You can then list the servers using the list_all() method.

# Note: The list_all() method returns a list of dictionaries,
# where each dictionary represents the information for a single
# server. You can just "print list_of_servers" in this code
# to see which key/value pairs are available, i.e what
# information you can get at.

def ex1(session):
    """List the active and deactivated servers in the Halo account."""

    print "\nExample#1: List the names of the 'active' servers " \
          "what group they are in."

    server = cloudpassage.Server(session)

    # Get a list of all the active servers and display them.
    list_of_servers = server.list_all(state='active')
    # print list_of_servers
    print "List of active servers:"
    for serv in list_of_servers:
        print "ID: %s   Server Name: %s is in Group: %s  State" \
            ": %s" % (serv["id"], serv["hostname"],
                      serv["group_name"], serv["state"])


# ----EXAMPLE #2------------------------
# Creating a server_group object by using the"ServerGroup"
# Class gets the list of server groups. You can then list the
# server groups by using the list_all() method.
# This example gets several pieces of information out of each
# server group by using dictionary indexing, i.e. indexing by
# key. You can add print list_of_server_groups to see what
# information, i.e. key/value pairs are available, so that
# you can access them.


def ex2(session):
    """List the server groups in the Halo account."""

    print "\nExample#2: List the Server Groups in your Halo account."

    server_group = cloudpassage.ServerGroup(session)

    # Get a list of all the active servers and print them out.
    list_of_server_groups = server_group.list_all()
    print "List of server groups:"
    for group in list_of_server_groups:
        print "ID: %s   Server Group Name: %s, has " \
            "Active:%s, Deactivated:%s, Missing:%s" % (
                group["id"], group["name"],
                group["server_counts"]["active"],
                group["server_counts"]["deactivated"],
                group["server_counts"]["missing"])


# ----EXAMPLE #3------------------------
# Thi list_all() method of the FirewallPolicy Class gets the list of
# all the firewall policies in your account.
# This example creates a FirewallPolicy object, and then uses its
# list_all() method to get the data, and then pulls out and displays
# some of the received data.

def ex3(session):
    """List all firewall policies in the Halo account."""

    print "\nExample#3: List the firewall policies in the Halo account."

    firewalls = cloudpassage.FirewallPolicy(session)

    # Get a list of all the active servers and display them.
    list_of_firewalls = firewalls.list_all()
    for fwall in list_of_firewalls:
        print "ID: %s   Policy Name: %s, Platform: %s" % (
            fwall["id"], fwall["name"],
            fwall["platform"])


# ----EXAMPLE #4-----------------------
# Here we load a CSM policy that is in JSON format and load it
# into Halo. This is an example of using the cloudpassage sdk
# to insert data into Halo.
# For this example to work you have to have a Halo CSM policy.
# The easiest way to get one is to export one out from the Halo UI
# and save it somewhere where your Python interpreter can find it.
# We use the JSON load() method to place the policy into memory in
# the variable called "data", and then we make a create() method
# call using our ConfigurationPolicy object to load the
# JSON-formatted data that is in the "data" variable into Halo.
#
# This is the REST API call that is essentially being made:
# i.e. a POST call to the /policies endpoint.
# POST https://api.cloudpassage.com/v1/policies/
#
# Note: Halo won't let you load a policy if a policy with that
# name already exists in your account!! It is always a good policy
# to check and make sure the policy doesn't already exist before
# you try and load it into Halo.

def ex4(session, policy_file):
    """Load a CSM Policy into Halo."""

    print "\nExample#4: Loading a CSM policy into Halo."
    ifile = open(policy_file, 'rU')
    print "Processing the input file.... %s" % (policy_file)

    data = json.load(ifile)
    print "Loading the policy: %s" % (data['policy']['name'])
    conf_policies = cloudpassage.ConfigurationPolicy(session)
    policy_id = conf_policies.create(data)

    if policy_id:
        print "Policy: %s, was loaded succesfully." % (data['policy']['name'])

    ifile.close()


# ----EXAMPLE #5-----------------------
#  List configuration policies in a Halo account.
#  You are essentially making the following REST API Call using
#  the /policies endpoint.
#
#  GET https://api.cloudpassage.com/v1/policies
#
#  You can use this call to, for example, obtain the ID of an
#  individual policy so that you can then view it or manipulate
#  it by using some of the methods in the cloudpassage sdk.

def ex5(session):
    """List all the CSM configuration policies."""

    print "\nExample#5: Listing the Configuration Policies."

    conf_policies = cloudpassage.ConfigurationPolicy(session)
    list_of_policies = conf_policies.list_all()
    for policy in list_of_policies:
        print "name=%-40s, id=%s, platform=%s" % (policy['name'],
                                                  policy['id'],
                                                  policy['platform'])


# ----EXAMPLE #6-----------------------------------------
#  Delete a Configuration Policy.
#  Requires that you pass this method the policy id of the policy
#  you want to delete. Note: To delete a policy you need to have
#  its policy id. Essentially you ar emaking the following REST
#  API call:
#
#  DELETE https://api.cloudpassage.com/v1/policies/{policy_id}

def ex6(session, policy_name):
    """Delete a configuration policy."""

    print "\nExample#6: Deleting a Configuration (CSM) Policy"

    conf_policies = cloudpassage.ConfigurationPolicy(session)

    # First we need to get the policy_id of the policy we want
    # to delete. If the policy we want to delete doesn't exist
    # then don't try to delete it.
    policy_id = 0
    list_of_policies = conf_policies.list_all()
    # print list_of_policies # For debug purposes.

    for policy in list_of_policies:
        if policy['name'] == policy_name:
            policy_id = policy['id']
            print "Name=%s, policy_id=%s" % (policy['name'], policy_id)

    # Note: if the policy_id is non zero (i.e. True) then the
    # policy exists. So now that we have the policy_id of the
    # policy we want to delete, we can go ahead and delete it
    # if it exists.
    if policy_id:
        success = conf_policies.delete(policy_id)
        if success is None:
            print "Policy: %s was deleted." % (policy_name)
        else:
            print "Unable to delete policy."
    else:
        print "The policy you are trying to delete does not exist in Halo."


# ----EXAMPLE #7-------------------------------------------

def ex7(session, server_name, group_name):
    """Move a specified server to a specified server group."""

    print "\nExample#7: Move a server to the specified group."
    print "Attempting to move server: %s to group: %s" % (server_name,
                                                          group_name)

    # First we need to get the server_id of the policy we want to move
    # and the group_id of the group we want to move the server to.
    # If the server or the group don't exist then don't try to move
    # the server.
    server_id = 0
    group_id = 0

    # Get the server id.
    server = cloudpassage.Server(session)
    list_of_servers = server.list_all(state='active')
    for serv in list_of_servers:
        if serv['hostname'] == server_name:
            server_id = serv['id']

    # Get the group id.
    server_group = cloudpassage.ServerGroup(session)
    list_of_server_groups = server_group.list_all()
    for group in list_of_server_groups:
        if group['name'] == group_name:
            group_id = group['id']

    print "Server id: %s" % server_id
    print "Group id: %s" % group_id

    # if both the server and group exist then move the server.
    if server_id and group_id:
        success = server.assign_group(server_id, group_id)
        if success:
            print "Server moved succesfully."
    else:
        print "Unable to move server."
        if not server_id:
            print "Server: %s does not exist." % server_name
        if not group_id:
            print "Group: %s does not exist." % group_name


# ---MAIN---------------------------------------------------------

def main():
    """main() function."""

    # Create the variable api_session. Setting it to None is a simple
    # placeholder trick, where it will then be initialized later.
    # If you don't do this pylint will complain about using a
    # variable without assigning it first.

    api_session = None
    api_session = create_api_session(api_session)

    # Note: you can comment out the examples that you don't want
    # to run. This lets you experiment independently with different
    # examples, to make it easier to learn how each one works.

    # Get a list of servers and what group they are in.
    ex1(api_session)

    # Get a list of server groups and print them.
    ex2(api_session)

    # Get a list of firewall policies and print them.
    ex3(api_session)

    # Check if the CSM policy exists, if it does delete it.
    # Here we are passing in the name of the policy that
    # we want to check to see if it already exists.
    ex6(api_session, "Apache for Debian, Ubuntu Linux - v2")

    # Load a CSM policy into Halo.
    # Here we pass in the name of the CSM policy
    # file that we want to load into Halo.
    ex4(api_session, "apache-linux-v2.policy.json")

    # List the configuration policies in your Halo account.
    # You will see that the Apache CSM policy gets loaded.
    ex5(api_session)

    # Delete the Apache CSM Policy
    # Here we pass in the name of the CSM policy that
    # we want to delete.
    ex6(api_session, "Apache for Debian, Ubuntu Linux - v2")

    # List the configuration policies in your Halo account.
    # You will see that the Apache CSM policy was deleted.
    ex5(api_session)

    # Move a server to a different server group and then back again.
    # Note: Make sure the server and groups names used in the ex7()
    # function call actually exist.
    # Note: By default the calls for this example are commented out
    # to run this code uncomment the calls that run the example code,
    # i.e. the calls to ex1() and ex7().

    # List the servers and what server groups they are in.
    # ex1(api_session)

    # Move a server to a given server group.
    # 'WIN-HIT7R77CFH8' is the name of the server in this example.
    # "KE core" and "HC-971] MS Patch Tuesday Server" are the names
    # of server groups in this example. To get this to work you will
    # have to change these names to names that exist in your Halo
    # account.
    # ex7(api_session, 'WIN-HIT7R77CFH8', 'KE core')

    # List the servers to show that the server was moved.
    # ex1(api_session)

    # Move a server to a given server group.
    # ex7(api_session, 'WIN-HIT7R77CFH8', '[HC-971] MS Patch Tuesday Server')

    # List the servers to show that the server was moved back.
    # ex1(api_session)

# -----------------------------------------------------

if __name__ == "__main__":
    main()


