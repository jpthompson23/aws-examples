# aws-examples
AWS deployment examples using ansible

Example .ansible.cfg file (copy to home directory):
```
[defaults]
host_key_checking = false
remote_user = ec2-user
ask_pass = false
private_key_file = /path/to/aws-examples/My_Test_KeyPair.pem

[privilege_escalation]
become_method = sudo
become_user = root
become_ask_pass = false
```
