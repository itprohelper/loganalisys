#!/usr/bin/env python
import psycopg2
import math

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute("""
SELECT title, count(*) AS views
FROM articles JOIN log
ON log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY views DESC LIMIT 3;
""")

results = cursor.fetchall()

# print results

print
print "Most popular three articles of all time"
for title, views in results:
    print('"{}" - {} views'.format(title, views))

print
cursor.execute("""
SELECT name, count(*) AS views
FROM authors, articles JOIN log
ON log.path = '/article/' || articles.slug
WHERE authors.id = articles.author
GROUP BY authors.name
ORDER BY views DESC LIMIT 3;
""")

results = cursor.fetchall()

print
print "Most popular article authors of all time"
for name, views in results:
    print('"{}" - {} views'.format(name, views))

print
cursor.execute("""
select to_char(date, 'FMMonth FMDD, YYYY'), err/total as ratio
       from (select time::date as date,
                    count(*) as total,
                    sum((status != '200 OK')::int)::float as err
                    from log
                    group by date) as errors
       where err/total > 0.01;
""")

results = cursor.fetchall()

print
print "Days did more than 1% of requests lead to errors"
for date,err in results:

    print ('{}  -- {} % errors'.format(date, round(err*100)))

conn.close()
