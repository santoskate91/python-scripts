import boto3
import datetime

def check_active_instances(region_name):
    # Create EC2 client
    ec2_client = boto3.client('ec2', region_name=region_name)

    # Get list of all instances in the specified region
    response = ec2_client.describe_instances()

    if 'Reservations' not in response:
        print(f"No instances found in region {region_name}")
        return

    print(f"Active instances in region {region_name}:\n")
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            
            name_tag = None
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name_tag = tag.get('Value')
                        break
            
            days, hours, minutes = 0, 0, 0
            
            if state == 'running':
                launch_time_str = instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
                launch_time = datetime.datetime.strptime(launch_time_str, "%Y-%m-%d %H:%M:%S")
                
                current_time = datetime.datetime.utcnow()
                uptime_seconds= (current_time - launch_time).total_seconds()
                
                days, remainder_days= divmod(uptime_seconds , 86400)
                hours, remainder_hours= divmod(remainder_days , 3600)
                minutes , seconds= divmod(remainder_hours , 60)
                
            print(f"Instance ID: {instance_id}")
            print(f"Name: {name_tag}")  
            print(f"State: {state}")
            print(f"Uptime: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes\n")

# Example usage:
aws_region = input("Enter your AWS region name: ")
check_active_instances(aws_region)