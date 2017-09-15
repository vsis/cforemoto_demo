# UF API

This is an small app to scrap UF values from bcentral.cl and expose an small api to retrieve UF values.

## Run with docker

First, build and run the image:

```bash
./docker-build.sh
./docker-run.sh
```

Now, you should get data from bcentral.cl
```bash
./docker-scrap.sh
```

It takes a while, because scraping bcentral.cl is a bit tricky. So I use a Selenium webdriver with Firefox.
That means, it opens X11 and Firefox inside a container, get the webpage from bcentral.cl, parse data and put it on database.

It finishes with a `Done` message.

Then, you may use the api:
```bash
curl "localhost:8080/uf/price?value=1.5&date=20170915"
curl "localhost:8080/uf/list"
```

## Run without docker

This app uses Selenium webdriver with Firefox to get data, so you need to install some dependencies if you want to run it without Docker.

This app was developed with:

    - python 3.6.2
    - virtualenv 15.1.0
    - firefox 54.0.1
    - geckodriver 0.17.0

First, let's build a virtualenv:
```bash
virtualenv virtualenv
virtualenv/bin/pip install -r requirements.txt
```

Then, scrap data
```bash
rm -f src/uf_api/db.sqlite3  # remove if it exists
virtualenv/bin/python src/uf_api/manage.py migrate
virtualenv/bin/python src/uf_api/manage.py scrap
```

Now, we may use the api
```bash
curl "localhost:8080/uf/price?value=1.5&date=20170915"
curl "localhost:8080/uf/list"
```

## Some possible improvements

 - [ ] Data is stored inside a docker container. It's easy to fix by the way
 - [ ] The scraper script get all 2017 data. None from previous years.
 - [ ] It doesn't try to scrap again for a not-found date
 - [ ] Uses Selenium with an entire browser. I couldn't do it with simple HTTP requests.
