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

#### using @deploy decorator

- writing all deploy using @deploy syntax
Can be shared as python packages
please refer https://docs.pyinfra.com/en/1.x/api/deploys.html

* extra parameter can be passed to deployment easily
* easy to convert code in reusable modules
