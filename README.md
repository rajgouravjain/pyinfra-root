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
- demo_app # deploy module with mix of @deploy syntax and tasks/*.py syntax
- demo_app/tasks/*.py
- team_user # deploy module with mix of @deploy syntax and tasks/*.py syntax
- team_user/tasks/*.py 

Benefit of hirarchy:
--------------------
- You can write both @deploy and tasks/*.py based deploy

Drawbacks:
---------
Since DEFAULTS variables cannot be passed to tasks/*.py, it cause sometime unexpected outputs.

