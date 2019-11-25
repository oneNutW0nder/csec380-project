[![Build Status](https://travis-ci.org/oneNutW0nder/firewagon.svg?branch=master)](https://travis-ci.org/oneNutW0nder/firewagon)

# csec380-project
CSEC380 Project for Simon, Mike, Robby

## Running This Project

There is some weird docker issue going on where it _**WILL NOT WORK**_ the first time you _build_ and _compose up_. You need to follow these steps:

```
docker-compose build --no-cache
docker-compose up -d
docker-compose down
docker-compose up
```

For some reason you will get `404` resposnes from the webserver the first time you compose the docker envirionment. 

## Vulnerabilities

> Classic SQL Injection  
> Blind SQL Injection  
> Command Injection  
> Server Side Request Forgery (SSRF)  
