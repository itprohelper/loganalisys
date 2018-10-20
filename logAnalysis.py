#!/usr/bin/env python
import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute ("""
SELECT title, count(*) AS views 
FROM articles JOIN log 
ON log.path = '/article/' || articles.slug 
GROUP BY articles.title 
ORDER BY views DESC LIMIT 3;
""")

results = cursor.fetchall()

#print results

print
print "Most popular three articles of all time"
#for results in results:
#  print " ", results[0], results[1],("-- views")
for title, views in results:
    print('"{}" - {} views'.format(title, views))


print
cursor.execute ("""
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
for results in results:
  print " ", results[0], results[1],("-- views")

print
cursor.execute ("""
SELECT date, avg(num) 
FROM errorsperday 
WHERE num > 1.0 
GROUP BY date 
ORDER BY date DESC;
""")

results = cursor.fetchall()


print
print "Days did more than 1% of requests lead to errors"
for results in results:
  print " ", results[0], "{0:.0%}".format(results[1]/100)

conn.close()
