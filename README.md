# JFlap in the web

> [!NOTE]
> Forked from https://git.sr.ht/~drnyanpassu/jflapweb


## PURPOSE

This repository aims to create a web-based abstraction of the JFlap program, allowing it to run within a browser environment. JFlap is widely used in university-level computer science for exploring topics in automata theory and formal languages. Making it accessible in a web browser responds to a significant demand from students, who seek a more accessible tool without complex installation steps, yet with functionality equivalent to the original program. This tool also facilitates research into programming language complexity in a virtual environment. The project is designed to be scalable, keeping the server load minimal by offloading as much processing as possible to the client side


## OVERVIEW

JFLap is a Java application for creating and visualizing various computational models, including automata, grammars, and Turing machines. It also supports testing these models with user-defined data within the same interface JFLap provides. This project brings JFLap's functionality to the web browser, closely replicating the Java version's capabilities (with some limitations). This is achieved using CheerpJ along with the original JFLap software.

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


## REFERENCES

Live preview at: <https://jflapweb.herokuapp.com>.

#### LIVE EXAMPLES

![example no. 1](https://git.sr.ht/~drnyanpassu/jflapweb/blob/master/resources/jflap-example1.png)

![example no. 2](https://git.sr.ht/~drnyanpassu/jflapweb/blob/master/resources/jflap-example2.png)
