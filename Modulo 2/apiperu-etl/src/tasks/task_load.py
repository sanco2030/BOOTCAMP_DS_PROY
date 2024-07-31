import mysql.connector
from config import Config
from prefect import task

config = Config()

conn = mysql.connector.connect(
            user=config.mysql_user,
            password=config.mysql_password,
            host=config.mysql_host,
            database=config.mysql_database
        )


@task(name='carga de info en bd')
def task_load_empresas(empresas):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_empresa"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_empresa(
        id INT AUTO_INCREMENT PRIMARY KEY,
        ruc VARCHAR(20),
        nombre_o_razon_social VARCHAR(255),
        departamento VARCHAR(255),
        monto VARCHAR(20),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP)
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_empresa(ruc,nombre_o_razon_social,departamento,monto)
        values(%s,%s,%s,%s)
        """

        for empresa in empresas:
            cursor.execute(query_insert,empresa)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)