# linkedin-request-automation
This script uses the Selenium library to automate the web browser and log in to your LinkedIn account. It then navigates to the "My Network" page and searches for suggested software engineers to connect with. The script iterates through the list of suggested engineers, and for each engineer, it clicks the "Connect" button and sends a connection request.

#The script will prompt you to enter your LinkedIn email and password. Once you have entered your credentials, the script will automatically navigate to the LinkedIn website, login to your account, and send connection requests to suggested software engineers.

#The script is designed to send connection requests to only two suggested software engineers, to avoid potential account blocking or suspension. If the script sends connection requests to more than two engineers, it will break out of the loop and stop sending requests.

#Once the script has sent the connection requests, it will pause for 5 seconds and then exit. You can modify the number of seconds to pause by changing the value in the time.sleep() function at the end of the script.

#Installation:
To use this script, you will need to have the following installed:

*Python 3
*selenium library for python
*ChromeDriver



