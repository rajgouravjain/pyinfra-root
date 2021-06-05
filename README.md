# pyinfra-root 

### Requirements:

* pyinfra
* pyinfra-docker

### Basic excution of pyinfra:
---------------------------
```sh
pyinfra inventories/test_instance.py exec -- hostname
pyinfra inventories/test_instance.py deploy_demo.py
pyinfra --dry @local   deploy_demo.py
```

=======
### Different ways to write deploy:

There are two major way of writing deploy in pyinfra. 
* using deploy with tasks/*.py files
* using @deploy decoratoer syntax -> preffered way
* writing mix of @deploy and tasks/*.py 

##### using deploy with tasks/*.py

* please refer hirarchy at https://docs.pyinfra.com/en/1.x/deploys.html
* visit branch v1 in this repository

##### using @deploy decorator

* Can be shared as python packages
* please refer https://docs.pyinfra.com/en/1.x/api/deploys.html
* two deploy packages team_user and demo_app are available

##### Writing mix of @deploy and tasks/*

* extra parameter can be passed to deployment easily
* easy to convert code in reusable modules
* plesae visit branch v3 for this experiement
