import mysql.connector

bbdd_club = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bbdd_club"
)

micursor = bbdd_club.cursor()

micursor.execute("CREATE TABLE socio( ID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, NOMBRE VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, APELLIDO VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, DNI VARCHAR(30) NOT NULL, TELEFONO VARCHAR(30) NOT NULL, EMAIL VARCHAR(128) NOT NULL, DIRECCION VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ESTADO_DE_CUENTA INT(40) NOT NULL)")