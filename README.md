# JFlapweb: future gadget #1, JFlap in the web

## PURPOSE

This repository has the purpose of abstracting the
program called `JFlap` making it runnable in the web
context. This program has usage in the field of computer
science at the university, being required to be able to
run in the web browser context means, that it's required
mostly because of the main interest of the students,
this implies that most of the studends want: the tool
more accesible to them, using the application without
most of the installation steps and being capable to do
the same as the main implementation programm. The tool
is useful for researching the complexity of the
programming languages in a virtual environment. The
scope for this project is being scalable without a
server overloading, all of this is posible in the client
leaving the server as light as possible.


## OVERVIEW

`JFLap` is a java program for building and rendering all
kinds of: automatas, grammars, turing machines, etc.
Also being capable to test the created machines with
user defined data in the same interface that `JFlap`
offers. With this project we can get the `JFlap` tool to
be able to run exactly like in the java version, but now
in the web browser (with some disadvantages). This is
all possible thanks to the tools: `Cheerpj` and the
original `JFlap` software.


## INSTALLATION

```bash
#!/bin/sh


# get the source code, you can also clone the repo
# from https://git.sr.ht/~drnyanpassu/jflapweb

REPO="https://git.sr.ht/~drnyanpassu/jflapweb"


# versions can be found with the next command:
# curl ${REPO}/refs/rss.xml | grep -Eo "v[0-9.]+"

curl -O ${REPO}/archive/<version>.tar.gz

mkdir /opt/jflapweb
tar axvf <version>.tar.gz -C /opt/jflapweb
cd /opt/jflapweb


# this step is optional if you maintain your own server,
# this is only for isolation purposes.

virtualenv env
source ./env/bin/activate
pip install -r requirements.txt


# you can generate the certificate files for https
# (optional if you don't want to reverse-proxy the app)

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# running the main application

gunicorn -c gunicorn.conf.py
```

the application will run at
[localhost](https://127.0.0.1:8080)


## HEROKU-CLI

```bash
#/bin/sh


# add the heroku-cli program with npm

npm install -g heroku


# or with yarn

yarn global add heroku


# heroku will need your credentials to proceed

heroku login -i


# app name is optional, heroku will throw you a random one

heroku create <app_name>


# create and fetch the remote heroku git repository

heroku git:remote --app <app_name>


# to obtain current branch: git branch

git push heroku master


# this will take a while to respond

curl https://<app_name>.herokuapp.com
```


## HEADLESS INSTALL

This tool is defined in one plain `HTML` file, meaning
that you can deploy this with any server language,
framework or server stack of your choice. But it will be
required to follow certain steps to work properly. This
repository has done the implementation using `Flask`,
`Python`, `Bootstrap` and `Linux` as the webstack
(mainly for compatibility reasons) following the the
next steps to do it work.


#### STEPS TO REPRODUCE THIS REPOSITORY

- First you will need to download JFlap (version used in
  this project: 7.0) jar from
  [here](http://www.jflap.org/getjflap.html).

- Install the cheerpj (version used in this project:
  1.4) program from
  [here](https://www.leaningtech.com/pages/cheerpj.html#Download).

- Compile JFlap with cheerpj (this will require python
  anyway).

  ```bash
  cheerpj_<version>/cheerpjfy.py jflap_<version>.jar
  ```

- Create a default route for the `*.jar` and the
  `*.jar.js` as the following output, like this:
  `/<file>` or `/resources/<file>`.

- Host the following
  [HTML](https://git.sr.ht/~drnyanpassu/jflapweb/blob/master/resources/reference.html)

- Run the main server and test the output.

- Now you can edit the `HTML` page, setup the server,
  reverse proxy or even making to be able install it
  headless in a way of a service (like host the `HTML`
  itself).

> `NOTE`: you can do this with any old java program (but
> not all will be compatible).


## REFERENCES

Live preview at: <https://jflapweb.herokuapp.com>.

for more information check the documentation at the
reference implementation:
<https://git.sr.ht/~drnyanpassu/moeflask.skuld>.


#### LIVE EXAMPLES

![example no. 1](https://git.sr.ht/~drnyanpassu/jflapweb/blob/master/resources/jflap-example1.png)

![example no. 2](https://git.sr.ht/~drnyanpassu/jflapweb/blob/master/resources/jflap-example2.png)


## CONTACT

<drnyanpassu@tfwno.gf>

<https://drnyanpassu.herokuapp.com/contact>