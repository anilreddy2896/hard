#!/bin/bash
aws iam create-group --group-name cars
for name in swift bmw skoda tayota 
do
  aws iam add-user-to-group --user-name $name --group-name cars
done