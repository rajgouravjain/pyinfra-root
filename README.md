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

deploy configuration and hirarchy
---------------------------------
- inventories/*.py
- group_data/*.py
- config.py # config file
- deploy_demo.py # deploy file
- tasks/*.py 
- files/*
- templates/*
- utils.py
