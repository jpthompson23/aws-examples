import os
import sys
import boto3


ec2_client = boto3.client('ec2')


def create_key_pair(name="My_Test_KeyPair", outfile="My_Test_KeyPair.pem"):
    resp = ec2_client.create_key_pair(KeyName=name)
    key = resp['KeyMaterial']
    with open(outfile, 'w') as outf:
        outf.write(key)
    os.chmod(outfile, 0o400)
    print(f"Wrote key `{name}` to file `{outfile}`")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        name = sys.argv[1]
        create_key_pair(name, f"{name}.pem")
    else:
        create_key_pair()
