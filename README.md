# RIT COVID Daily Assessment

RIT has [released](https://www.rit.edu/news/rit-launches-daily-health-screen-monitoring-covid-19-symptoms?utm_source=twitter&utm_medium=social&utm_campaign=mc-ritready&utm_term=&utm_content=daily_health_screen) a daily health screening website. Requiring everyone to complete 7 days a week. 

> This applies to everyone whether they are working remotely or taking online classes and is required on weekends and vacation days - [source](https://www.rit.edu/news/rit-launches-daily-health-screen-monitoring-covid-19-symptoms?utm_source=twitter&utm_medium=social&utm_campaign=mc-ritready&utm_term=&utm_content=daily_health_screen)

This script will complete the screening for you and send you a text message when it is completed. **Note:** please fill out the form yourself if you do have any of the symptoms outlined here. 

> Have you had any of the following symptoms in the last 24 hours that are new or unusual for you?

> Loss of sense of taste or smell.
> Chills or fever of 100F (37.8C) or higher.
> Sore throat (not due to allergies).
> Feeling like coming down with an illness. (Ex. Fatigue or muscle aches)
> Unusual headache or eye pain.
> New cough or change in your cough.
> New or worsening shortness of breath (difficulty breathing).
> Abdominal pain, nausea, vomiting, diarrhea or loss of appetite.
> Learned that you had contact with a confirmed case of COVID-19 in the last week.

This script simply fills out the form if you do not have any of the above symptoms. 

## Running the script
First make a ```.env``` file and copy the ```.env.example``` fill out your email, email password, phone number to receive alerts, rit username, and rit password. 

The text messages are sent using [smtplib](https://docs.python.org/3/library/smtplib.html) and relayed through Google's smtp servers. You can change this to a custom server if you would like. Also for Gmail accounts you have to set up a app specific password which can be done at [myaccount.google.com](https://myaccount.google.com/) > Security > App Passwords select custom password generate and then copy  the password into the .env (you will only see this password once). 

You will need to install the following packages: 

```
pip3 install smtplib
pip3 install python-dotenv
pip3 install selenium
```

The script uses [selenium](https://selenium-python.readthedocs.io/) for filling out the form. You will need to install a driver for this by default using ```chromeDriver```. Which can be downloaded from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Unzip and place the driver in the same directory as the script. 

Run the script with ```python3 ritcovidassessment.py```. You will receive a text when the form is complete. 

You can continually run the script with cron

```
# edit your cronjobs
crontab -e

# on the bottom add
10 0 * * * python3 <path to script>
```

to run the script everyday at 0:10