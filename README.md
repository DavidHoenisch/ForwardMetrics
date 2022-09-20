## Forward Metrics


### Running the Web app

1. install python3 from here: https://www.python.org/downloads/
2. reboot
3. install all the required packages by running `pip3 install -r requirements.txt` from the root of the application directory
4. move into that application directory `forward-metrics-web-application/app` and run `python3 .\app.py`

this will spin up a local working version of the application.  The url will be noted in the command out put but will most likely be `http://127.0.0.1:5000`



### NOTES

```
<a href="{{ url_for('user', Users_username = current_user.username ) }}" 
target="_blank" rel="noopener noreferrer">Settings</a>

```
