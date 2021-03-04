import boto3


cf_client = boto3.client('cloudformation')


def deploy():
    env_name = "dev"
    stack_name = f"{env_name}-vpc"
    parameters = [
        {
            "ParameterKey": "Env",
            "ParameterValue": env_name
        }
    ]
    tags = [
        {
            "Key": "Env",
            "Value": env_name
        }
    ]
    with open("yaml/vpc.yaml", 'r') as f:
        template_body = f.read()
    response = cf_client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Tags=tags
    )
    print(response)


if __name__ == "__main__":
    deploy()
