# List running AWS EC2 instances

This  script lists running EC2 instances ordered from the longest running first and displays the following info:
* Instance ID
* Instance type
* Instance running time in seconds
* Instance name

AWS credentials should be available as per https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration

### How to use

```
git clone git@github.com:manzoon/instancelister.git
cd instancelister
virtualenv -p python3 env
source ./env/bin/activate
pip install -r requirements.txt

# Usage:
# python ./oldest-instances.py <aws_region> <max_instances_to_show>
# i.e. ./oldest-instances.py eu-west-2 20
```