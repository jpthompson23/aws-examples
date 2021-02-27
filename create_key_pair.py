import boto3


ec2_client = boto3.client('ec2')

def create_key_pair(name="My_Test_KeyPair", outfile="My_Test_KeyPair.pem"):
    resp = ec2_client.create_key_pair(KeyName=name)
    key = resp['KeyMaterial']
    with open(outfile, 'w') as outf:
        outf.write(key)

if __name__ == "__main__":
    create_key_pair()

