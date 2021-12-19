import boto3

client = boto3.client("ec2")


def get_instance_ids(client):
    my_instances = client.describe_instances()
    instance_ids_to_return = []
    for reservation in my_instances["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["InstanceType"] == "t2.micro" and instance["State"]["Name"] == "running":
                instance_ids_to_return.append({"id": instance["InstanceId"], "ip": instance["PublicIpAddress"]})
    return instance_ids_to_return
 
print(get_instance_ids(client))
   
ec2 = boto3.resource('ec2') 
   
def create_instance(ec2):
response = ec2.create_instances(SubnetId="subnet-06cfb6d887ac1cae8", InstanceType="t2.micro", ImageId="ami-0ed9277fb7eb570c9", MaxCount=1, MinCount=1)
return response
    
print(create_instance(ec2))
