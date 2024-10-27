# JFlap in the web

> [!NOTE]
> Forked from https://git.sr.ht/~drnyanpassu/jflapweb

This project runs the JFlap program within a browser environment making it easier for students to use.

## OVERVIEW

JFLap is a Java application for creating and visualizing various computational models, including automata, grammars, and Turing machines. It also supports testing these models with user-defined data within the same interface JFLap provides. This project brings JFLap's functionality to the web browser, closely replicating the Java version's capabilities (with some limitations). This is achieved using CheerpJ along with the original JFLap software.

## INSTALLATION

1. Install [Docker](https://www.docker.com/)
2. Build the container image `docker build -t jflapweb .`
3. Run the image `docker run --rm -it -p 3000:5000 --name jflapweb-container jflapweb`
4. The application will now be live at <http:localhost:3000>

#### LIVE EXAMPLES

![example no. 1](https://raw.githubusercontent.com/memoalv/jflapweb/refs/heads/main/resources/jflap-example1.png)

![example no. 2](https://raw.githubusercontent.com/memoalv/jflapweb/refs/heads/main/resources/jflap-example2.png)
