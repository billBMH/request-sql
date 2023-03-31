import pymysql

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="metehan", passwd="sefa25", database="CONCEPTBALL")
with connection:
    with connection.cursor() as cursor:

        sql = "INSERT INTO `Camera` (`cam_id_camera`, `cam_ip_camera`,`t_numero_Terrain`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (4.6, '10.171.25.49',2))
    connection.commit()


    with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `cam_ip_camera` FROM `Camera` WHERE `cam_id_camera`=%s"
            cursor.execute(sql, (90))
            result = cursor.fetchone()
            print(result)
