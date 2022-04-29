# python-listEC2-instances
This is an basic application which uses flask and boto3 to list details about EC2 instances in an region

Use these basic docker commands to deploy and check in your local

sudo docker build -t <image-name>:<tag> .
  
sudo docker run -it -p 8000:8000 <image-name>:<tag>

It should load the application at port 8000 in your local

Hit 127.0.0.1:8000/ec2 to check if the resposne
