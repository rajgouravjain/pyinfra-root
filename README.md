### pyinfra 

Requirements:
------------
pyinfra

Basic excution of pyinfra:
---------------------------
```sh
pyinfra inventories/test_instance.py exec -- hostname
pyinfra inventories/test_instance.py deploy_demo.py

pyinfra --dry @local   deploy_demo.py
```

Different ways to write deploy:
-------------------------------
There are two major way of writing deploy in pyinfra. 
* using tasks/*.py files
* using @deploy decoratoer -> preffered way

- writing all deploy using @deploy syntax
Can be shared as python packages
please refer https://docs.pyinfra.com/en/1.x/api/deploys.html

- creating deploy with tasks/*.py
please refer hirarchy at https://docs.pyinfra.com/en/1.x/deploys.html

- Writing mix of @deploy and tasks/*.py 
These kind of deploys can be shared as python packages
plesae visit branch v1 for this experiement

