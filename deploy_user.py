from pyinfra_users import deploy_user


deploy_user(user="rj")
deploy_user(user="nj",group="wheel")
