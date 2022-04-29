from cmath import isnan
import boto3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ec2')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    
    ec2client = boto3.client(
        'ec2',
        aws_access_key_id='<access-key>',
        aws_secret_access_key='<secret-key>',
        region_name='us-west-2'
    )

    ec2detailsDict=dict()

    response = ec2client.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance)
            ec2detailsList=list()
            ec2detailsList.append(instance["InstanceId"])
            ec2detailsList.append(instance["PrivateIpAddress"])
            ec2detailsList.append(instance["Tags"])
            ec2detailsDict[instance["InstanceId"]]=[]
            ec2detailsDict[instance["InstanceId"]].extend(ec2detailsList)
    return jsonify(ec2detailsDict)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)




