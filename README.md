# Pyrkov

Generate new tweets based on old ones using a custom Markov Chains implementation.

Pyrkov uses Twitter's REST API 1.1 and has been made to be executed in a CRON task. The best frequency is something like every 30 minutes to avoid any restriction.

# Prerequisites
- Python 3 (tested with Python 3.4)
- Tweepy (installation explained below)
# Installation guide
## Create a Twitter app
Pyrkov, and every application that uses Twitter API, requires some access keys. To get these keys, you have to create an application on your Twitter account and ask Twitter for your keys. Here is how you do it.

- Go on [Twitter App](https://apps.twitter.com/) and log in into your Twitter account
- Next to the title **Twitter Apps**, click on the "Create New App" button
- You'll have to type some informations :
    - **Name:** Name that will be showed for your application (visible on Tweetdeck for example)
    - **Description:** Write something to remember what is this application for
    - **Website:** Link to redirect users who have clicked on your application name
- Once your application is created, go into its settings then in the **Keys and Access Tokens** tab.
- Under **Application Settings**, you have the two first needed keys (Consumer Key, Consumer Secret)
- Under **Your Access Token**, you will have to create your access token. Then you'll get two more keys (Access Token, Access Token Secret)

Keep these keys, this application will need these.

## Windows
### 1. Install / Update tweepy
Use your favorite Git client and clone the tweepy repository in a folder. If you use git in a terminal:
```bash
git clone https://github.com/tweepy/tweepy.git
```

Get into the created "tweepy" folder in a terminal and use Python to install it *(assuming that Python3 is your default Python installation)*
```bash
cd tweepy
python setup.py install
```
*Note: Tweepy is available on Pypi (and pip), but the package is currently outdated and doesn't work anymore. The manual installation is now required.*

## 2. Install Pyrkov
Now, clone Pyrkov with your Git client in a folder. If you use git in a terminal:
```bash
git clone https://github.com/MayakoLyyn/Pyrkov.git
cd Pyrkov
```

You now have to configure the application. A configuration template is available in the *config_template.ini* file, copy and rename it to *config.ini*, then, open it with your favorite text editor (Notepad is fine). Then, set up your keys and you're ready to go!

To execute Pyrkov from a terminal, go into its folder then simply type this:
```bash
python main.py
```

## Linux server
> /!\ This is based on a Debian 8 server

### 1. Install / Update tweepy

First, clone the repo somewhere
```bash
git clone https://github.com/tweepy/tweepy.git
```

A folder "tweepy" will be created and the code will be downloaded there.

As we're going to use Python3, install Tweepy using Python3.

```bash
cd tweepy
sudo python3 setup.py install
```

*Note: Tweepy is available on Pypi (and pip), but the package is currently outdated and doesn't work anymore. The manual installation is now required.*

### 2. Install Pyrkov

Move to the folder where Pyrkov's folder will be created and clone the repository:
```bash
git clone https://github.com/MayakoLyyn/Pyrkov.git
cd Pyrkov
```

You now have to configure the application. A configuration template is available in the *config_template.ini* file, copy and rename it to *config.ini*, then, open it.
```bash
cp config_template.ini config.ini
nano config.ini
```
> I use nano, but you obviously can use your favorite text editor.

Set up your keys and you're ready to use Pyrkov!

#### Bonus: Add Pyrkov to crontab
*I recommand to execute Pyrkov every half-hour, not more, or you'll exceed the API Rate Limit.*

Open crontab and add an entry for Pyrkov:
```bash
sudo nano /etc/crontab
```

I set up my crontab to execute Pyrkov every 30 minutes and to write a new log at each execution
```
*/30 * * * *    lyyn    python3 /home/lyyn/Pyrkov/main.py > /home/lyyn/Pyrkov/crontab.log
```

# config.ini structure
## [auth]
All these key are required and available in your Twitter Application on https://apps.twitter.com
- **consumer_key**: your Consumer Key
- **consumer_secret**:  your Consumer Secret Key
- **access_token**:  your Access Token
- **access_secret**:  your Access Token Secret

## [preferences]
- **local**: If its set to *True*, the generated tweet will be posted on your account once it's created. Otherwise, Pyrkov will create a *temp.txt* containing 100 generated tweet.

# Side notes

This project has been made with Visual Studio 2015. Use Markov.sln to open it! :)
