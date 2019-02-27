import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = rds_config.rds_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, port=3306, connect_timeout=5)
    print('SUCCESS')
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print('FAILURE')
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0
    cur = conn.cursor()
    # with conn.cursor() as cur:
    #     cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
    #     cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
    #     cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
    #     cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
    #     conn.commit()
    #     cur.execute("select * from Employee3")
    #     for row in cur:
    #         item_count += 1
    #         logger.info(row)
    # conn.commit()

    cur.execute("SELECT * FROM cio4good WHERE year = 2013")
    result = cur.fetchall()
    return result
