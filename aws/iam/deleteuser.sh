#!/bin/bash
for name in swift bmw skoda tayota 
do 
   aws iam delete-user --user-name $name
done