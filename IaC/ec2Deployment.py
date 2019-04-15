import boto3

ec2object = boto3.resource('ec2')

myUbuntuInstance = ec2object.create_instances(
    ImageId = 'ami-0535e2ddd3ef26bb6',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.nano',
    KeyName = 'btcProj',
    SubnetId = 'subnet-0f1119801c607d988'
)