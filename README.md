# Python CGI Programming

### Steps to create

1. Install Apache2 Web Server `sudo apt-get install apache2`
2. Check the firewall `sudo ufw allow list`
3. Check if Apache2 is running `sudo systemctl status apache2`
4. If Apache2 is stopped, run `sudo systemctl start apache2`
5. Open `nano /var/www/html/index.html` and add the content 
6. Create a directory `mkdir /var/www/cgi-bin`
7. Add content `nano /var/www/cgi-bin/test.py`

Now run the script at yourlocalhost or the Public Ip if is running in the VM
