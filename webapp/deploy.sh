sudo apt install python-is-python3
sudo apt install python3-pip
echo 'PATH=$PATH:~/.local/bin' >> .profile

pip install requests flask waitress
sudo cp app.service /etc/systemd/system/zadanie.service

sudo systemctl enable --now zadanie