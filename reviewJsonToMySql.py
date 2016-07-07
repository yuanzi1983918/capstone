import json
import MySQLdb
import pprint

db = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="918918",
                       db="amazon")
                       
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS reviews_Clothing_Shoes_and_Jewelry")

create_sql = """CREATE TABLE reviews_Clothing_Shoes_and_Jewelry (
         helpful VARCHAR(255),
         reviewerName  VARCHAR(255),
         reviewerID VARCHAR(255),  
         reviewTime VARCHAR(255),
         reviewText TEXT,
         overall FLOAT,
         summary VARCHAR(255),
         asin VARCHAR(255),
         unixReviewTime LONG)"""

cursor.execute(create_sql)

file_path = "reviews_Clothing_Shoes_and_Jewelry_5.json"
with open(file_path) as f:
    for line in f:
        value_list = []
        j_content = json.loads(line)
        #pprint.pprint( j_content)
        placeholders = ', '.join(['%s']* len(j_content))
        columns = ', '.join(j_content.keys())
        for key in j_content.keys():
            value = j_content[key]
            if type(value) is list:
                value = str(value)
            value_list.append(value)
        altuple = tuple(value_list)
        insert_sql =  "INSERT INTO reviews_Clothing_Shoes_and_Jewelry ( %s ) VALUES ( %s )" % (columns, placeholders)
        pprint.pprint(insert_sql)
        #pprint.pprint( altuple)
        cursor.execute(insert_sql, altuple)
        db.commit()

db.close()