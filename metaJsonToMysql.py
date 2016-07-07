import json
import MySQLdb
import pprint

db = MySQLdb.connect(host="localhost",
                       user="root",
                       passwd="918918",
                       db="amazon")
                       
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS meta_Clothing_Shoes_and_Jewelry")

create_sql = """CREATE TABLE meta_Clothing_Shoes_and_Jewelry(
         asin VARCHAR(255),
         title TEXT,
         price VARCHAR(255),
         imUrl VARCHAR(255),
         related TEXT,
         salesRank VARCHAR(255),
         brand VARCHAR(255),
         categories TEXT)"""
         
cursor.execute(create_sql)

columns = ["asin", "title", "price", "imUrl", "related", "salesRank", "brand", "categories"]
columns_str = ', '.join(columns)
placeholders = ', '.join(['%s']* len(columns))
file_path = "meta_Clothing_Shoes_and_Jewelry.json"
with open(file_path) as f:
    for line in f:
        value_list = []
        j_content = json.loads(line)
        for key in columns:
            if key in j_content.keys():    
                value = j_content[key]
                if type(value) is list or type(value) is dict or type(value) is float:
                    value = str(value)
                value_list.append(value)
            else:
                value_list.append("novalue")
        altuple = tuple(value_list)
        insert_sql =  "INSERT INTO meta_Clothing_Shoes_and_Jewelry ( %s ) VALUES ( %s )" % (columns_str, placeholders)
        pprint.pprint(insert_sql)
        #pprint.pprint( altuple)
        cursor.execute(insert_sql, altuple)
        db.commit()

db.close()