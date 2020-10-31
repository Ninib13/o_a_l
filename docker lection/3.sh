apk update && apk upgrade
wget https://releases.hashicorp.com/terraform/0.12.28/terraform_0.12.28_linux_amd64.zip 
unzip terraform_0.12.28_linux_amd64.zip 
rm terraform_0.12.28_linux_amd64.zip 
mv terraform /usr/local/bin/
wget https://github.com/terraform-linters/tflint/releases/download/v0.16.2/tflint_linux_amd64.zip 
unzip tflint_linux_amd64.zip 
rm tflint_linux_amd64.zip
mv tflint /usr/local/bin/
apk add curl 