 gcloud compute networks subnets subnet1 name=vpc-1 range=10.2.0.0/24
   gcloud compute networks subnets vpc-1 name=subnet1 range=10.2.0.0/24
gcloud compute networks subnets  create subnet-a  name=vpc-1 range=10.2.0.0/24
gcloud compute networks subnets  create subnet-a  --network=vpc-1 --range=10.2.0.0/24
   24  gcloud compute networks subnets  create subnet-b  --network=vpc-2 --range=10.2.1.0/24 --region=us-central1
   25  gcloud compute instances create instance-1a --subnet=subnet-a --zone=us-central1-a -no-address
   26  gcloud compute instances create instance-1a --subnet=subnet-a --zone=us-central1-a -no-ipaddress
   27  gcloud compute instances create instance-1a --subnet=subnet-a --zone=us-central1-a --no-address
   28  gcloud compute instances create instance-1b --subnet=subnet-a --zone=us-central1-a --no-address
   29  gcloud compute instances create instance-1c --subnet=subnet-a --zone=us-central1-a --no-address
   30  gcloud compute instances create instance-1 --subnet=subnet-b --zone=us-central1-a
   31  gcloud compute instances create instance-2 --subnet=subnet-b --zone=us-central1-a