import boto3
import os

def osLaunch():
    """Launches an EC2 instance and returns the instance ID."""
    ec2 = boto3.resource('ec2', region_name=os.environ['AWS_REGION'])
    instances = ec2.create_instances(
        InstanceType='t2.micro',
        ImageId='ami-0fd05997b4dff7aac',  # Replace with your desired AMI ID
        MinCount=1,
        MaxCount=1
    )
    return instances[0].id

def osTerminate(instance_id):
    """Terminates an EC2 instance."""
    ec2 = boto3.client('ec2', region_name=os.environ['AWS_REGION'])
    ec2.terminate_instances(InstanceIds=[instance_id])

def main():
    """Main function to launch and terminate instances."""
    instance_id = osLaunch()
    print(f"Launched instance: {instance_id}")
    # ... do something with the instance ...
    osTerminate(instance_id)
    print(f"Terminated instance: {instance_id}")

if __name__ == "__main__":
    main()
