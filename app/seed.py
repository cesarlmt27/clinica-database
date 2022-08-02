from configuraciones import *
import psycopg2
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s"%(host,database,user,passwd))
cur = conn.cursor()

cur.execute(open("./SQLs/clinica.sql", "r").read())

cur.execute(open("./SQLs/entrada_salida_paciente.sql", "r").read())

cur.execute(open("./SQLs/ficha_medica.sql", "r").read())

cur.execute(open("./SQLs/habitacion_paciente.sql", "r").read())

cur.execute(open("./SQLs/medico.sql", "r").read())

cur.execute(open("./SQLs/paciente.sql", "r").read())

conn.commit()
cur.close()
conn.close()
