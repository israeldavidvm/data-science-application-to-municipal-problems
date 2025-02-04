<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Data-Science-Application-to-Municipal-Problems](#data-science-application-to-municipal-problems)
  - [Data-Science-Application-to-Municipal-Problems](#data-science-application-to-municipal-problems-1)
  - [License](#license)
  - [Characteristics What does it offer?](#characteristics-what-does-it-offer)
  - [features to implement / characteristics to be implemented](#features-to-implement--characteristics-to-be-implemented)
  - [Planning, Requirements Engineering and Risk Management / Planning, Requirements Engineering and Risk Management](#planning-requirements-engineering-and-risk-management--planning-requirements-engineering-and-risk-management)
  - [Use:](#use)
    - [Install units:](#install-units)
    - [Execute the project projectidvm.py](#execute-the-project-projectidvmpy)
    - [Structure of the app:](#structure-of-the-app)
    - [We need to analyze what are the types of problems that have been made more difficult to solve in each state.](#we-need-to-analyze-what-are-the-types-of-problems-that-have-been-made-more-difficult-to-solve-in-each-state)
    - [Perform an analysis of the main problems of the provinces: Caracas, Bolívar and Portuguese.](#perform-an-analysis-of-the-main-problems-of-the-provinces-caracas-bol%C3%ADvar-and-portuguese)
      - [Image of the search engine without specifying a province (makes a small summary of all)](#image-of-the-search-engine-without-specifying-a-province-makes-a-small-summary-of-all)
      - [Image of the search engine specifying Bolívar as province](#image-of-the-search-engine-specifying-bol%C3%ADvar-as-province)
    - [Analyze the “resolved” reports and what average time elapsed since its creation, broken down by subcategory.](#analyze-the-resolved-reports-and-what-average-time-elapsed-since-its-creation-broken-down-by-subcategory)
      - [Interactive histogram of resolution times:](#interactive-histogram-of-resolution-times)
    - [Server configuration requirements](#server-configuration-requirements)
      - [LIFT BASIC local web server:](#lift-basic-local-web-server)
      - [Create tunnel with remote server with HTTPS](#create-tunnel-with-remote-server-with-https)
      - [Access to app](#access-to-app)
  - [Design Software / Software Design](#design-software--software-design)
    - [Structural perspective](#structural-perspective)
      - [Logica view of software architecture](#logica-view-of-software-architecture)
    - [Behavior perspective](#behavior-perspective)
  - [Technical Decions / Technical Decisions](#technical-decions--technical-decisions)
    - [Make to Donation. Your Contribution Will Make to Difference.](#make-to-donation-your-contribution-will-make-to-difference)
    - [Find me on:](#find-me-on)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-Start doctoc generated touch please keep comment here to allow Auto Update->
<!-Don's Edit This Section, Instead Re-Run Doctor to Update->
** Table of content ***generated with [doctoc] (https://github.com/thlorenz/doctoc)*

-[Calculator-with-ooc] (#Calculator-With-Oc)
-[Calculator-With-Oc] (#Calculator-With-Oc-Orry)
- [License] (#license)
-[CHARACTERISTICS WHAT OFFER YOU?] (#CHARACTERISTICS-%C2%BFQU%C3%A9-TE-DEFREE)
-[features to implement / characteristics to be implemented] (#features-to-implement-caracteristic-to-implement)
-[Planning, Requirements Engineering and Risk Management / Planning, Requirements Engineering and Risk Management] (#Planning-Requirements-Engineering-And-Risk-Management-Planning-Ingenieria-De-Requerlations-Y-Gestion-Del-Riesgo )
-[Software Design / Software Design] (#Software-Design-Dise%C3%B1O-De-Software)
- [Structural Perspective] (#perspective-structural)
-[Logic view of software architecture] (#-logic-of-the-architecture-del-software)
-[behavior perspective] (#perspective-of-behavior)
-[Stages of the Machine Learning project:] (#Stages-Del-Project-De-Machine-Learning)
-[Definition of the problem:] (#definition%c3%b3n-of-problem)
-[Identification of information needs:] (#Identification%C3%B3n-de-Las-Necesities-Informaci%C3%B3n)
-[Obtaining and preparation of data:] (#obtanci%c3%b3n-y-preparation%C3%b3n-datos)
-[Input and output data processing:] (#Processing-of-Data-Entrada-Y-Salida)
-[Construction of the model:] (#Construcci%C3%B3n-Del-Model)
-[Compile the model:] (#compile-el-model)
-[Train the model:] (#train-al-model)
-[Generation of predictions:] (#generation%C3%B3n-de-Predictions)
-[Store the model and training registration:] (#Store-the-Model-and-Registration-Decreasing)
-[Example inputs and outputs] (#inputs-and-salides-of-example)
-[Technical Decions / Technical Decisions] (#Technical-Decisions-Decisions-Tecnic)
- [Make to Donation. Your Contribution Will Make A Difference.] (#Make-A-Donation-Your-Contribution-Will-Make-A-Difference)
-[Find me on:] (#Find-me-on)
-[Technologies used / used technologies] (#Technologies-ined-Tecnologias-Usadas)

<!-End doctoc generated touch please keep comment here to allow Auto Update->

# Data-Science-Application-to-Municipal-Problems

[Readme version in English] (./ Readme-en.md)

## Data-Science-Application-to-Municipal-Problems

! [alt text] (image-4.png)
! [alt text] (image-3.png)

This application in Python is designed to analyze a database of user reports that describe problems and needs in their communities.


## License

This Code is licensed under the general public license of GNU version 3.0 or posterior (LGPLV3+). You can find a complete copy of the license at https://www.gnu.org/licenses/lgPl-3.0-standalone.htmlalone.html0-standalone.html

## Characteristics What does it offer?

- Interactive histogram of the types of problems:

! [Image of the interactive histogram of the types of problems] (image.png)

This histogram is interactive, allowing zoom to move between the different provinces etc.

[Image of the interactive histogram of the types of problems with zoom and showing graphics information] (image-1.png)

- Problematic analyzing component by province

Uncomplicated search engine (makes a small summary of all)

[Image of the search engine without specifying a province (performs a small summary of all)] (image-2.png)

[Image of the search engine without specifying a province (performs a small summary of all)] (Image-3.png)

Search engine specifying Bolívar as province

[Image of the search engine specifying Bolívar as province] (Image-4.png)

[Image of the search engine specifying Bolívar as province] (Image-5.png)


- Interactive histogram of resolution times:

! [alt text] (image-6.png)

## features to implement / characteristics to be implemented

## Planning, Requirements Engineering and Risk Management / Planning, Requirements Engineering and Risk Management

These sections of the project will be carried out through a site in Notion so that they can be easily accessible by non -technical staff.

Request access link to authorized personnel

## Use:

### Install python

sudo apt update
sudo apt install python3

### Install pip3
sudo apt update
sudo apt install python3-pip

### Install units:
Pip3 Install Dash
PIP3 Install Pandas

### Execute the project projectidvm.py
Within the folder where the project we invoke the interpreter of Python passing the project file
Python3 Proyectoidvm.py which should generate an output like the one shown on screen

Note that the warning is born that Flash is being used that provides a local server that does not have the protections to be used in production to operate the app to take the app to production we should use a server dedicated to these purposes.

### Structure of the app:

ASSETS:
folder with styles files and app images
PROJECTOIDVM.PY:
Archive with the Python script
reports_test.xlsx:
Archive with the calculation sheet where the data is found

### We need to analyze what are the types of problems that have been made more difficult to solve in each state.

Interactive histogram of the types of problems:
To solve the requirement, a histogram is implemented where the types of problems are shown.

Interactive histogram of the types of problems:

! [Image of the interactive histogram of the types of problems] (image.png)

This histogram is interactive, allowing zoom to move between the different provinces etc.

[Image of the interactive histogram of the types of problems with zoom and showing graphics information] (image-1.png)

Problematic Analyzer Component By Province

### Perform an analysis of the main problems of the provinces: Caracas, Bolívar and Portuguese.

Problematic analyzing component by province:

For this, a component capable of generating 2 types of visualizations is implemented: a graph that summarizes the main problems, a table where these problems are detailed.

These visualizations are generated dynamically through a search engine that is capable of generating dynamic changes according to a province.

This component works as follows:
If you want to obtain the information for a certain province, one of them is selected through the search engine, which adjusts the 2 previous visualizations adjusted to the specified province.
In case of not specifying a specific province, it shows a summary of the problems of all provinces.

#### Image of the search engine without specifying a province (makes a small summary of all)

[Image of the search engine without specifying a province (performs a small summary of all)] (image-2.png)

[Image of the search engine without specifying a province (performs a small summary of all)] (Image-3.png)

#### Image of the search engine specifying Bolívar as province

[Image of the search engine specifying Bolívar as province] (Image-4.png)

[Image of the search engine specifying Bolívar as province] (Image-5.png)

### Analyze the “resolved” reports and what average time elapsed since its creation, broken down by subcategory.

#### Interactive histogram of resolution times:

For this, another histogram is implemented, as shown in the following figure.

! [alt text] (image-6.png)

<!-
### Server configuration requirements
Given some of the computer security settings

Therefore and for the purposes of this project a basic local http server will be lifted that only loads the page and connected by means of the ngrok tool a tunnel to a server that if https offers

#### LIFT BASIC local web server:

For this you can use any server, but here is a way to do it:

- Download python3

- Open a command line or terminal

- Save to the folder where

- Execute the command
`` python3 -m http.Server <numberpuertoservidorlocal> `` `` ``

#### Create tunnel with remote server with HTTPS

You can make an HTTPS tunnel following the following steps

- Download Ngrok on your computer, and decompress it

- Open a command line or terminal

- Save to the folder where you downloaded ngrok

- Execute the command
`` ngrok http <numberpuertosavidorlocal> ``

Since we have a domain associated with NGROK we will use the command

`` NGROK HTTP-DOMAIN = APT-KID-PRIVATELY.NGROK-FREE.App <NUMBERTOSSERVIDORLOCAL> `` `` `` `` `` `` ``

#### Access to app
It is important to have both assets: the Python server, and the Ngrok tunnel

After executing Ngrok's command, an HTTPS link will appear.

Open an explorer on your cell phone and go to the HTTPS link indicated in our case since we already had an associated domain will be https://apt-kid-privately.ngrok-free.app->>


## Design Software / Software Design

### Structural perspective

#### Logica view of software architecture

In the following class diagram, key abstractions will be seen in the system, their responsibilities.

! [alt text] (image.png)



<!- Class Diagram

class databaseauditor {

}

Note for database auditor "seeks to be the context for the different strategies used
and a medium that encapsulates utilitarian functions
common for all algorithms "

Databaseauditor ..> databaseschemagenerator

class database schema generator {
<< abstract>>
+Databaseauditor
+Generate ()
}

Note for database schema generator "provides the strategy interface
which is common to all concrete strategies
For the generation of
Database schemes "

Databaseschemagenerator ..> schemafromdbusingname
Databaseschemagenerator ..> Schemafromjson

Class Schemafromjson {
+Databaseauditor
+Generate ()
}

Class schemafromdbusingname {
+Databaseauditor
+Generate ()
}

Note for schemafromdbusingname "is one of the specific strategies
that generates the schemes by means of the names
of the name conventions of the database "

Databaseauditor ..> Validationalgorithm

Note for Validation Algorithm "provides the strategy interface
which is common to all concrete strategies
For the generation of
Validations of the database "

Class Validation Algorithm {
<< abstract>>
+Execute ()
}

Validationalgorithm <|- NonadditIVeconcatenation
Validationalgorithm <|- Verificationbcnf


Class Verification Nonadditive Concatenation {
+Databaseauditor
+Execute ()
}


Note for non additive concatenation "encapsulates algorithm 11.1 verification
of the non -additive concatenation property proposed by Ramez Elmasri
and Shamkant B. Navathe "

CLASS VERIFICATIONBCNF {
+Databaseauditor
+Execute ()
}

Note for non additive concatenation "encapsulates the algorithm that validates that each
Decomposition possesses the BCNF
Based on the definition presented
By Ramez Elmasri and Shamkant B. Navathe "

Databaseauditor <.. client

Class client {

} ->


### Behavior perspective


## Technical Decions / Technical Decisions

To solve the problem, an application was built in Python using:
The Dash bookstore which made possible the creation of interactive dashboards, graphics, tables and other visual elements. It should be noted that internally Dash uses the Microframework Flask and the React.js library.
The Plotly Express bookstore which allows a little more to facilitate the creation of complex graphics, it should be noted that this is in turn based on the Plotly Graphics Library
The Pandas bookstore that facilitated working with tabular data, such as the present file sheet , etc.

### Make to Donation. Your Contribution Will Make to Difference.
[! [ko-fi] (https://ko-fi.com/img/githubutton_sm.svg)] (https://ko-fi.com/israeldavidvm)
[! [PayPal] (https://img.shields.io/badge/paypal-@israeldavidvm-0077b5?style=for-the-badge&ogo=paypal&logocolor=white&labelColor=101010)] (https://paypal.me/israeldavidvm )
[! [Binance] (https://img.shields.io/badge/binance_id-809179020-1010 ?style=for Activity/Referral-Entry/CPa? Ref = CPA_004ZGH9EIS)

### Find me on:
[! [Github] (https://img.shields.io/badge/github-israeldavidvm-gray?
[! [LinkedIn] (https://img.shields.io/badge/linkedIn-israeldavidvm-0077b5?style=for-the-badge&ogo=LinkedI in/Israeldavidvm/)
[! [Twitter] (https://img.shields.io/badge/twitter-@israeldavidvm-1da1f2?style=FOR-the-badge&ogo=twitter&logocolor=white&labelColor=101010)] (https://twitter.com/israeldavidvm )
[! [Facebook] (https://img.shields.io/badge/facebook-israeldavidvm-1877f2? Israeldavidvm)
[! [Instagram] (https://img.shields.io/badge/instagram-@israeldavidvmv-gray?style=for-the-badge&ogo=instagram&logocolor=White&labelColor=101010)] (https://www.instagram.com /Israeldavidvm/)
[! [Tiktok] (https://img.shields.io/badge/tiktok-@israeldavidvm-e4405f?style=FOR-the-badge&ogo=tiktok&logocolor=white&labelColor=101010)] (https://www.tiktok.com /@Israeldavidvm)
[! [YouTube] (https://img.shields.io/badge/youtube-@israeldavidvm-ff0000?style=FOR-the-badge&ogo=youtube&logocolor=white&labelcolor=101010)] (https://www.youtube.com /Channel/UCMZLFPENPDWPJOHAL0WRY7A)

