#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# Checks if nginx is installed.
if ! nginx -v &> /dev/null; then
    sudo apt-get update
    sudo apt install nginx -y
fi

# Creates directories folders
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Creating a fake HTML file
echo "<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is a fake website</title>
</head>
<body>
    <div>
        <h1>Hello... This is a fake website.</h1>
        <style>
            body {
                background-color: beige;
            }
        </style>
    </div>
</body>
</html>" > /data/web_static/releases/test/index.html

# Creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving ownership to ubuntu user recursively
chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
config="location https://dabetterman.tech/hbnb_static {
    alias /data/web_static/current;
}
"
echo "$config" | tee /etc/nginx/sites-available/default > /dev/null

# Restarting nginx
sudo systemctl restart nginx
