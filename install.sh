#!/bin/bash
echo "Installing emergency-response-system..."

# Move to appropriate directory
sudo mkdir -p /var/www/emergency-response-system
sudo chown $USER:$USER /var/www/emergency-response-system
cd /var/www/emergency-response-system

# Clone the repository
git clone https://github.com/ParaCryptid/emergency-response-system.git .

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
elif [ -f "package.json" ]; then
    npm install
fi

# Create systemd service file
sudo bash -c 'cat <<EOF > /etc/systemd/system/emergency-response-system.service
[Unit]
Description=emergency-response-system Service
After=network.target

[Service]
ExecStart=/var/www/emergency-response-system/start.sh
Restart=always
User=$USER
WorkingDirectory=/var/www/emergency-response-system

[Install]
WantedBy=multi-user.target
EOF'

# Enable and start service
sudo systemctl enable emergency-response-system.service
sudo systemctl start emergency-response-system.service

echo "emergency-response-system installed and running!"
