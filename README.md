# RESTful API for Lucky Draw
* Python 3.8.1
* virtualenv 16.7.9
* Django 3.1.7
* djangorestframework 3.12.2

## Requirements
1. [Virtualbox 6.1.16](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant 2.2.14](https://www.vagrantup.com/downloads)
3. Use with **cshimegi/lucky-draw-gui**

## Installation from scratch
##### Notification
If you want to install from scratch, please refer to branch **master**.

##### Steps
* Step 1
`git clone https://github.com/cshimegi/lucky-draw-api.git`

* Step 2
```bash
$  cd /to/Vagrantfile/path
$  vagrant up --provision
```

* Step 3
```bash
$  vagrant ssh
$  source /env38/bin/activate
$  sudo pip3 install -r /vagrant/requirements.txt
$  sudo python3 /vagrant/manage.py makemigrations
$  sudo python3 /vagrant/manage.py migrate
$  sudo python3 /vagrant/manage.py runserver 0.0.0.0:8080
```

## Access to Django WEB
After dev django server is ready, you can access API page from browser.

`http://192.168.12.2:8080/api/v1`

## Useful Commands
### Vagrant
```bash
$  vagrant up  //  to strat
$  vagrant up --provision //  to strat and provision
$  vagrant ssh  //  connect by SSH
$  vagrant halt // to halt
```

### Ubuntu (bento/ubuntu-20.10)
```bash
$  source /env38/bin/activate // activate virtual python3 env
$ (env38) deactivate // deactivate virtual python3 env
```
