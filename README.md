![CollaboDev](https://imgur.com/Vj1C4fO.png)
[![Build Status](https://travis-ci.org/dob9601/CollaboDev.svg?branch=master)](https://travis-ci.org/dob9601/CollaboDev) [![MIT Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/mit-license.php) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) 
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg) ![Django Version](https://img.shields.io/badge/django%20version-2.0-blue.svg)
 [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](http://www.paypal.me/dob9601)

An open source collaboration webapp built on Django.

---

## Installation

 - Clone this repository using 
 ```
 git clone https://github.com/dob9601/CollaboDev.git
 ```
 - Alternatively, if you don't wish to use Git, download the repository [here](https://github.com/dob9601/CollaboDev/archive/master.zip)
 - Open up a console to the project directory and run the following commands in order to create a superuser and run the server on 127.0.0.1:8000.
 ```
 python manage.py createsuperuser
 python manage.py runserver
 ```
 - If you wish to access the CollaboDev web app from other computers within the same network, run the command (server will be hosted on local machine's ip address):
 ```
 python manage.py runserver 0.0.0.0:80 
 ```
 
**NOTE: As this software is early access, debug mode must be enabled for it to function properly (serving of static files not setup completely). For this reason, I would advise against hosting it on the internet (instead, host it within a LAN). Fixing this issue is high up on my list of priorities**

If you aren't ready to commit yet/want to experience CollaboDev to see if you prefer CollaboDev to your current task management application, send me a message via the email associated with [my GitHub account](https://github.com/dob9601) and I'll provide you access to a temporary Heroku server.

 ---
 
My name is Daniel and I am a student in the UK. I founded this project out of boredom and have been working on it in my spare time with little to no intention of making any revenue from it. However, if you have used this webapp, any donations are greatly appreciated and can be done so via PayPal using the PayPal shield at the top of this readme file.

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
