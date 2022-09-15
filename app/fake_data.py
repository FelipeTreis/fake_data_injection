from faker import Faker

from connect import con, cur

fake = Faker()

base_sql = '''INSERT INTO customer (name, email) VALUES ('{}', '{}')'''

for i in range(1000):
    name = fake.name()
    email = fake.email()
    sql = base_sql.format(name, email)
    cur.execute(sql)

con.commit()
con.close()
