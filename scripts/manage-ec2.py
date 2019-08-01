import boto3
import click


# create a session
session = boto3.Session(profile_name='innovation')
# create a resource
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)
        ))

if __name__ == '__main__':
    list_instances()

