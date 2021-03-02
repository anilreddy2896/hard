#!/bin/bash
for name in swift bmw skoda tayota 
do 
   aws iam create-user --user-name $name
   aws iam create-login-profile --user-name $name --password Anil@289 --no-password-reset-required
   aws iam attach-user-policy --user-name $name --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
done