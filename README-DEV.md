# README for Developers

This project uses [Pelican](https://docs.getpelican.com/en/latest/).

Follow the instruction below to properly setup this project.

## Python Setup
 
Setup Python, then upgrade pip and install virtualenv to properly handle the dependencies.

````
pip install --upgrade pip
pip install virtualenv
````

## Project Setup

This setup should be execute typically for the first time.
Once the project was built this setup won't be necessary anymore.

### Virtualenv

Use virtualenv and install the dependencies.

````
virtualenv env
source env/bin/activate
````

### Dependencies

Install the bumped dependencies
````
pip install -r requirements.txt
````

## Project local Build

To build the website run the command below, a folder called `output` will be
created and will containg the static website.

````
pelican content
````

## Preview the Web Site

To serve the website using the integrated pelican httpd server, you can
use the following command.

````
pelican --listen
````

You will be able to connect to `https://localhost:8000` to navigate the
website.
