import random
from app import app
from flask import render_template, request, redirect
from app.configuraciones import *
import psycopg2


conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" %(host, database, user, passwd)) #Iniciar conexión con la base de datos.
cur = conn.cursor()		#Permite que el código Python ejecute el comando PostgreSQL en una sesión de base de datos.


@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html")


@app.route('/clinicas')	 #Búsqueda de las clínica. 21.
def clinicas():
	#Obtiene la entidad clínica con sus respectivos atributos.
	sql = ''' 
	select * from clinica order by id
	''' 
	cur.execute(sql) 
	clinica  = cur.fetchall() #retorna toda la consulta.
	
	conn.commit()
	return render_template("clinicas.html", clinica=clinica) 


@app.route('/medicos')	#Búsqueda de los médicos de la clínica. 12.
def medicos():
	#obtiene la entidad medico con sus atributos.
	sql = '''
    select * from medico order by id;
	'''
	cur.execute(sql)
	medico  = cur.fetchall()

	conn.commit()
	return render_template("medicos.html", medico=medico)

@app.route('/borrar_medico/<medico_id>', methods=['GET','POST'])	#Borrar un médico de una clínica. 8.
def borrar_medico(medico_id):   
	#Actualiza el id del medico que se borró a nulo, en los pacientes que tengan ese medico.
	sql = '''
	update paciente set medico_id = null where medico_id = %s;
	''' %(medico_id)
	cur.execute(sql)
	
	#Buscar el id de la clínica donde se encuentra un médico.
	sql = '''
	select clinica.id from clinica join medico on clinica.id = medico.clinica_id where medico.id = %s;
	''' %(medico_id)
	cur.execute(sql)
	clinica_medico  = cur.fetchone()
	
	#Borramos el medico de la clinica encontrada en la linea 47.
	sql = '''
	delete from medico where id = %s and clinica_id = %s;
	''' %(medico_id, clinica_medico[0])
	cur.execute(sql)

	conn.commit()
	return  redirect(request.referrer)


@app.route('/pacientes')	#Búsqueda de los pacientes de la clínica. 10.
def pacientes():
	#obtiene la entidad paciente con sus respectivos atributos.
	sql = '''
	select * from paciente order by id;
	'''
	cur.execute(sql)
	paciente  = cur.fetchall()

	conn.commit()
	return render_template("pacientes.html", paciente=paciente)


@app.route('/ficha')	#Búsqueda de las fichas médicas de la clínica. 13.
def ficha():
	#obtiene la entidad ficha_medica con sus respectivos atributos.
	sql = '''
	select * from ficha_medica order by id;
	'''
	cur.execute(sql)
	ficha_medica  = cur.fetchall()

	conn.commit()
	return render_template("ficha.html", ficha_medica=ficha_medica)


@app.route('/habitaciones')		#Búsqueda de las habitaciones disponibles en la clínica. 11
def habitaciones():
	#obtiene la entidad habitacion_paciente con sus respectivod atributos.
	sql = '''
	select * from habitacion_paciente order by id;
	'''
	cur.execute(sql)
	habitacion  = cur.fetchall()

	conn.commit()
	return render_template("habitaciones.html", habitacion=habitacion)


@app.route('/entrada')	#Muestra el registro de entrada y salida. 19, 20
def entrada():
	#obtiene la entidad entrada_salida_paciente con sus respectivos atributos.
	sql = '''
	select * from entrada_salida_paciente order by id;
	'''
	cur.execute(sql)
	entrada_salida  = cur.fetchall()

	conn.commit()
	return render_template("entrada.html", entrada_salida=entrada_salida)



@app.route('/registro_clinica', methods=['GET', 'POST']) #registrar una clinica 17.
def registro_clinica():
	if request.method == 'POST': #Recibe lo rellenado en el formulario.
		nombre = request.form['nombre'] 
		direccion = request.form['direccion']
		telefono = request.form['telefono']
		
        #Inserta los datos del formulario en la base de datos.
		sql = '''
		insert into clinica (nombre, direccion, telefono, cantidad_habitaciones) values ('%s','%s', %s, 0);
		''' %(nombre, direccion, telefono)
		cur.execute(sql)

	conn.commit()
	return render_template("registro_clinica.html")


@app.route('/registro_medico', methods=['GET', 'POST'])  #registrar una medico 7.
def registro_medico():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		edad = request.form['edad']
		rut = request.form['rut']
		dv = request.form['dv']
		especialidad = request.form['especialidad']
		
        #Obtiene el id de la última clínica que se encuentra en la entidad clinica.
		sql = '''
		select max(id) from clinica; '''
		cur.execute(sql)
		ult_clinica  = cur.fetchone()  #Almacerna el id de la última clínica que se encuentra en la entidad clinica.

		clinica = random.randint(1, ult_clinica[0]) #Ramdom para asignar un médico a una clinica.
        
		#inserta un medico.
		sql = '''
		insert into medico (nombre, apellido, edad, rut, dv, especialidad, clinica_id) values ('%s','%s', %s, %s, %s,'%s', %s);
		''' %(nombre, apellido, edad, rut, dv, especialidad, clinica)
		cur.execute(sql)

	conn.commit()
	return render_template("registro_medico.html")


@app.route('/registro_paciente', methods=['GET', 'POST'])	#Registro de paciente, registro de ficha médica y registro de entrada. 6 , 18 y 15.
def registro_paciente():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		edad = request.form['edad']
		rut =  request.form['rut']
		dv =  request.form['dv']
		prevision =  request.form['prevision']
		
        #Obtiene el id del último médico que se encuentra en la entidad medico.
		sql = '''
		select max(id) from medico;
		'''
		cur.execute(sql)
		ult_medico = cur.fetchone()		#Almacerna el id del último médico que se encuentra en la entidad medico.

		medico = random.randint(1, ult_medico[0])	#Ramdom para asignar un médico a un paciente.
        
		#inserta un paciente.
		sql = '''
		insert into paciente (nombre, apellido, edad, rut, dv, prevision_medica, 
		medico_id, ficha_medica_id) values ('%s', '%s', %s, %s, %s, '%s', %s, null);
		''' %(nombre, apellido, edad, rut, dv, prevision, medico)
		cur.execute(sql)

		#Obtiene el id del último paciente que se encuentra en la entidad paciente.
		sql = '''
		select max(id) from paciente; '''
		cur.execute(sql)
		ult_paciente  = cur.fetchone()	#Almacerna el id del último paciente que se encuentra en la entidad paciente.

		#Generar ficha médica (sin datos) del paciente registrado.
		sql = '''
		insert into ficha_medica (diagnostico, alergias, tipo_sangre, peso, inter_quirurgica, 
		enfer_cronica, paciente_id) values (null, null, null, null, null, null, %s);
		''' %(ult_paciente[0])
		cur.execute(sql)

		#Obtiene el id de la última ficha médica que se encuentra en la entidad ficha_medica.
		sql = '''
		select max(id) from ficha_medica; '''
		cur.execute(sql)
		ult_ficha  = cur.fetchone()	#Almacerna el id de la última ficha médica que se encuentra en la entidad ficha_medica.

		#Actualiza el atributo ficha_medica_id del paciente generado, con la finalidad de asignarle la ficha médica generada anteriormente.
		sql = '''
		update paciente set ficha_medica_id = %s
		where paciente.id = %s;
		''' %(ult_ficha[0], ult_paciente[0])
		cur.execute(sql)

		#Obtiene el id de la última clínica que se encuentra en la entidad clinica.
		sql = '''
		select max(id) from clinica; '''
		cur.execute(sql)
		ult_clinica  = cur.fetchone()	#Almacerna el id de la última clínica que se encuentra en la entidad clinica.

		clinica = random.randint(1, ult_clinica[0])	#Ramdom para asignar una clínica a la entidad entrada_salida_paciente del paciente ingresado.
		
		#Registro de entrada del paciente.
		sql = '''
		insert into entrada_salida_paciente (fecha_entrada, fecha_salida, paciente_id, clinica_id, estado) 
		values (NOW(), null, %s, %s, true);
		''' %(ult_paciente[0], clinica)
		cur.execute(sql)

	conn.commit()

	return render_template("registro_paciente.html")


@app.route('/editar_ficha/<paciente_id>', methods=['GET', 'POST'])	#Actualización de ficha médica. 1.
def editar_ficha_medica(paciente_id): 
	if request.method == 'POST':
		diagnostico = request.form['diagnostico']
		alergias = request.form['alergias']
		tipo_sangre = request.form['tipo_sangre']
		peso =  request.form['peso']
		inter_quirurgica =  request.form['inter_quirurgica']
		enfer_cronica =  request.form['enfer_cronica']
		
        #Actualizar un dato de la ficha médica del paciente.
		if diagnostico:
			sql = ''' update ficha_medica set diagnostico = '%s'
			where paciente_id = %s ''' %(diagnostico, paciente_id)
			cur.execute(sql)

		if alergias:
			sql = ''' update ficha_medica set alergias = '%s'
			where paciente_id = %s ''' %(alergias, paciente_id)
			cur.execute(sql)

		if tipo_sangre:
			sql = ''' update ficha_medica set tipo_sangre = '%s'
			where paciente_id = %s ''' %(tipo_sangre, paciente_id)
			cur.execute(sql)

		if peso:
			sql = ''' update ficha_medica set peso = '%s'
			where paciente_id = %s ''' %(peso, paciente_id)
			cur.execute(sql)

		if inter_quirurgica:
			sql = ''' update ficha_medica set inter_quirurgica = '%s'
			where paciente_id = %s ''' %(inter_quirurgica, paciente_id)
			cur.execute(sql)

		if enfer_cronica:
			sql = ''' update ficha_medica set enfer_cronica = '%s'
			where paciente_id = %s ''' %(enfer_cronica, paciente_id)
			cur.execute(sql)

	#Selecciona el id y el nombre del paciente para mostrar en editar_ficha.html
	sql = '''
	select id,nombre from paciente where id = %s ''' %(paciente_id)
	cur.execute(sql)
	paciente  = cur.fetchone()
	
	conn.commit()

	return render_template("editar_ficha.html", paciente=paciente)


@app.route('/registro_habitacion/<clinica_id>', methods=['GET', 'POST']) #Registro de habitacion 9.
def registro_habitacion(clinica_id):
	#Buscar la cantidadd de habitaciones que tiene una clínica.
	sql = '''
	select cantidad_habitaciones from clinica where clinica.id = %s;
	''' %(clinica_id)
	cur.execute(sql)

	cantidad_hab  = cur.fetchone()		#Almacenar la cantidad de habitaciones de la clínica.
	nueva_hab = cantidad_hab[0] + 1		#Sumar uno a la cantidad de habitaciones de la clínica, ya que se está registrando una nueva habitación.

	#Insertar en la entidad habitacion_paciente la habitación nueva de la clínica.
	sql = '''
	INSERT INTO habitacion_paciente (clinica_id, numero_habitacion, paciente_id, estado) 
	VALUES (%s, %s, null, false);
	''' %(clinica_id, nueva_hab)
	cur.execute(sql)

	#Actualizar en la entidad clinica la cantidad de habitaciones que tiene la clínica.
	sql = '''
	update clinica set cantidad_habitaciones = %s where id = %s ;
	''' %(nueva_hab, clinica_id)
	cur.execute(sql)

	conn.commit()
	return redirect(request.referrer) 


@app.route('/registro_salida/<paciente_id>', methods=['GET', 'POST']) 	#registro salida (dar de alta) y actualizacion de estado de la habitacion (cuando es dado de alta). 16 y 2
def registro_salida(paciente_id):
	#Actualizar en la entidad entrada_salida_paciente la salida del paciente.
	sql = '''
	update entrada_salida_paciente set fecha_salida = NOW(), estado = false where paciente_id= %s;
	''' %(paciente_id)
	cur.execute(sql)

	#Actualiza el medico del paciente a null cuando este es dado de alta.
	sql = '''
	update paciente set medico_id = null where id = %s;
	''' %(paciente_id)
	cur.execute(sql)

	#Buscar la habitación del paciente que se da de alta.
	sql = '''
	select habitacion_paciente.id from habitacion_paciente join paciente 
	on habitacion_paciente.paciente_id = paciente.id where paciente.id = %s;
	''' %(paciente_id)
	cur.execute(sql)
	habitacion = cur.fetchone();	#Almacenar habitación del paciente dado de alta.

	#Actualizar la habitación del paciente que fue dado de alta para marcar como desocupada.
	sql = '''
	UPDATE habitacion_paciente set paciente_id = null, estado = false 
	where id = %s;
	''' %(habitacion[0])
	cur.execute(sql)

	conn.commit()
	
	return redirect(request.referrer)


@app.route('/ingreso_habitacion/<habitacion_id>', methods=['GET', 'POST'])	#Actualización de estado de la habitación (cuando esta ocupada) 2.
def ingreso_habitacion(habitacion_id):
	if request.method == 'POST':
		nombre = request.form['nombre']
		rut = request.form['rut']
		dv = request.form['dv']

		#Buscar el id de los datos del paciente recibidos por el formulario.
		sql = '''
		SELECT id from paciente where nombre = '%s' AND rut = %s AND dv = '%s';
		''' %(nombre, rut, dv)
		cur.execute(sql)
		paciente_id  = cur.fetchone()

		#Actualizar el estado y el paciente_id de la entidad habitacion_paciente, con la información del paciente a ingresar.
		sql = ''' 
		UPDATE habitacion_paciente set paciente_id = %s, estado = true
		where id = %s;
		''' %(paciente_id[0], habitacion_id)
		cur.execute(sql)

		conn.commit()
		
	return render_template("ingreso_habitacion.html")


@app.route('/actualizar_medico/<paciente_id>', methods=['GET', 'POST']) #Actualizar el medico del paciente. 3.
def actualizar_medico(paciente_id):
	#Obtener el id del último médico de la entidad medico.
	sql = '''
	select max(id) from medico;
	'''
	cur.execute(sql)
	ult_medico = cur.fetchone()	#Almacenar el id del último médico.
	
	medico = random.randint(1, ult_medico[0])	#Random para asignar un médico aleatorio nuevo a un paciente.
	
    #Actualiza el medico en la entidad paciente, entregandole un medico aleatorio al paciente.
	sql = '''
	update paciente set medico_id = %s where id = %s;
	''' %(medico, paciente_id)
	cur.execute(sql)

	conn.commit()
	
	return redirect(request.referrer)


@app.route('/actualizar_ingreso/<paciente_id>', methods=['GET', 'POST']) #actualizar el ingreso del paciente. 4.
def actualizar_ingreso(paciente_id):
	#Actualizar la fecha_entrada en la entidad entrada_salida_paciente, en el caso de que un paciente regrese a la clinica.
	sql = '''
	update entrada_salida_paciente set fecha_entrada = NOW() where paciente_id = %s;
	''' %(paciente_id)
	cur.execute(sql)

	conn.commit()
	
	return redirect(request.referrer)
