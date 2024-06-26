import taosrest

# db_config = {
#     'url': 'http://124.70.89.186:6041',
#     'user': 'root',
#     'password': 'taosdata',
#     'database': 'ht2_data'
#
# }
conn = taosrest.connect(url='http://124.70.89.186:6041',
                        user='root',
                        password='taosdata',
                        database='ht2_data')

db = "power"
print(conn)
conn.execute(f"DROP DATABASE IF EXISTS {db}")
conn.execute(f"CREATE DATABASE {db}")
# create super table
conn.execute(
    f"CREATE STABLE {db}.meters (ts TIMESTAMP, current FLOAT, voltage INT, phase FLOAT) TAGS (location BINARY(64), groupId INT)"
)

# create table
conn.execute(f"CREATE TABLE `{db}`.`d0` USING `{db}`.`meters` TAGS('Los Angles',0 )")

# rest insert data
sql = """
INSERT INTO
power.d1001 USING power.meters TAGS('California.SanFrancisco', 2)
    VALUES ('2018-10-03 14:38:05.000', 10.30000, 219, 0.31000)
    ('2018-10-03 14:38:15.000', 12.60000, 218, 0.33000) ('2018-10-03 14:38:16.800', 12.30000, 221, 0.31000)
power.d1002 USING power.meters TAGS('California.SanFrancisco', 3)
    VALUES ('2018-10-03 14:38:16.650', 10.30000, 218, 0.25000)
power.d1003 USING power.meters TAGS('California.LosAngeles', 2)
    VALUES ('2018-10-03 14:38:05.500', 11.80000, 221, 0.28000) ('2018-10-03 14:38:16.600', 13.40000, 223, 0.29000)
power.d1004 USING power.meters TAGS('California.LosAngeles', 3)
    VALUES ('2018-10-03 14:38:05.000', 10.80000, 223, 0.29000) ('2018-10-03 14:38:06.500', 11.50000, 221, 0.35000)
"""

inserted = conn.execute(sql)
print(inserted)

conn.close()
