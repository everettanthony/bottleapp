import sqlite3
db = sqlite3.connect('picnic.db')
db.execute("INSERT INTO picnic (item,quant) VALUES ('heroin', 995)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('crackrock', 65)")
db.commit()