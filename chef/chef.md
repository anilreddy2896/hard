* chef is a pull based configuration management tool
* it is used to automate the configuration in the hosts and maintain the idempotancy

in this type of configuration management set up node will check with the sever is there any configuration available to install for this process to happen we install agent the the node machine .

*** the nodes communicate with the cm server  by default every 30min . we can change it 

cm server will not maintain any list of nodes ,it just needs to validate that the request is comming from right agent  

* chef architecture contain :
      1. chef server:
          1.1 hosted server 
          1.2 self managed server
      2. nodes
      3. work station

we develop cookbooks which have recipes in the chef client in our own laptop and we upload this cookbook to the chef sever ,later when nodes asks for configuration chef server responds by giving the recipes to be executed on the node.

chef uses the terminology of kitchen and chef

1. we will install chef client on the nodes
2. we will install chef dk(development kit) on the work station
3. we will install chef server on the server

we will also configure on which node which reciepe has to be executed 
 step1: 
 * https://manage.chef.io/organizations/crazymind/nodes

step 2:
After creating the account 
install chef dk in the workstation .
* chef server must be linux server
* work station can be any os
* chef node can be any os ,switch,router as well

step 3:
* install chef client on the nodes  and setup authentication b/w server and node. This process is called as bootstrapping
  and this boot strapping is done from the chef worksttion by installing chef starter kit .
     * this starter kit has .chef folder which contains 
         1. .pem file which is a private key for enabling authentication with chef server 
         2. config.rb which has info about server 

chef dk tool:  
   1. knife:
         knife node list : to list tj

