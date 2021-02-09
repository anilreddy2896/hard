replicationController and replicaset do the same work it helps to maintiain the number of replicas we want if the 
pod goes down

for replicas we need is 2  
it is maintaining suddenly when the node that hosting pod goes down 
than we ask for 2 but there is only 1 running 
in this situation replicaset will create one more pod to maintain the desired state of 2 replications

-no manual intervention it is down automatically


