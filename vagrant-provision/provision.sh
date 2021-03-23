echo "==================Update apt-get================================"
sudo apt-get update
sudo apt install net-tools
echo "====================End of Updating apt-get========================="

echo "==================Install Python================================"
# Install pip3, virtualenv
sudo apt -y install python3.8 python3-pip python3-venv
echo "====================End of Python Installation========================="

echo "==================Install Django and Mod_wsgi================================"
sudo pip3 install Django==3.0.8
echo "====================End of Django and Mod_wsgi========================="

echo "==================Create Python Virtual Env================================"
# create virtual python env
sudo python3 -m venv /env38
echo "====================End of Python virtual Env Creation========================="