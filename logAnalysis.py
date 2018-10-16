import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute ("select title, count(*) as views from articles join log on log.path like concat('%',articles.slug) group by articles.title order by views desc limit 3")

results = cursor.fetchall()

#print results

print
print "Most popular three articles of all time"
for results in results:
  print " ", results[0], results[1],("-- views")

print
cursor.execute ("select name, count(*) as views from authors, articles join log on log.path like concat('%',articles.slug) where authors.id = articles.author group by authors.name order by views desc limit 3")

results = cursor.fetchall()


print
print "Most popular article authors of all time"
for results in results:
  print " ", results[0], results[1],("-- views")

print
cursor.execute ("select date, avg(num) from errorsperday where num > 1.0 group by date order by date desc")

results = cursor.fetchall()


print
print "Days did more than 1% of requests lead to errors"
for results in results:
  print " ", results[0], "{0:.0%}".format(results[1]/100)

conn.close()
