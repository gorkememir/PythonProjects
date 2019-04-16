import boto3

ec2 = boto3.resource('ec2')
nicAutoDeployed = ec2.NetworkInterface('eni-0837e2835d2430423')

nicAutoDeployed.modify_attribute(
    Description={
        'Value': 'Primary network interface'
    },
)

print(nicAutoDeployed.description)