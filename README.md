## Log Analisys
This Python script will report the following:

1. What are the most popular three articles of all time.
2. Who are the most popular article authors of all time.
3. On which days did more than 1% of requests lead to errors.

This reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Requiments
This project uses the following:

1. Python version 2.7
2. PostgreSQL
3. psycopg2 Python module

You will need to manually create a database in PostgreSQL using this following command:

   ` create database news;`

Once you have created the empty database go to the following link and download `newsdata.sql` from the following URL:

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Unzip the newsdata.zip. This will give you a `newsdata.sql` which you can then import to your empty database by running the below command:

   ` psql -d news -f newsdata.sql`

This fictional PostgreSQL database is for a news website.


## Usage
Once you have the data loaded into your database. Connect to your database using:

    psql -d news 

Explore the tables using the \dt and \d table commands and select statements.


    \dt — display tables — lists the tables that are available in the database.
    \d table — (replace table with the name of a table) — shows the database schema for that particular table.
 

The database includes three tables:

    The authors table includes information about the authors of articles.
    The articles table includes the articles themselves.
    The log table includes one entry for each time a user has accessed the site.


On your terminal type: `python logAnalysis.py`


## Views created in the database
***errorsperday:***
*create view errorsPerday as select date(time), count(status) as num from log where status like '404%' group by status, time order by time desc;*



