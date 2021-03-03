#!/bin/python3
import boto3


ec2_client = boto3.client('ec2')


def get_subnet_id():
    # get id of default vpc:
    vpcs_resp = ec2_client.describe_vpcs(Filters=[{
        "Name": "isDefault", "Values": ['true']
    }])
    default_vpc = vpcs_resp['Vpcs'][0]
    default_vpc_id = default_vpc['VpcId']

    sn_resp = ec2_client.describe_subnets(Filters=[{
        "Name": "vpc-id", "Values": [default_vpc_id]
    }])
    # pick whatever the first subnet is:
    subnet = sn_resp['Subnets'][0]
    return subnet['SubnetId']


if __name__ == "__main__":
    print(get_subnet_id())
