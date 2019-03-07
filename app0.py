import sys
import logging
import rds_config
import pymysql
import json 

#rds settings
rds_host  = rds_config.rds_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = rds_config.port

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, port=port, connect_timeout=5)
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
    cur.execute("SELECT year, organization_count FROM cio4good WHERE size = 'Group';")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data
    # result = cur.fetchall()
    # return result
