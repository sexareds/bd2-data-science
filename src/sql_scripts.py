sql_script_1 = '''
    SELECT Respuesta.num_encuesta, 
        Respuesta.num_pregunta, 
        Respuesta.num_opcion, 
        Respuesta.respuesta
    FROM Encuesta
    INNER JOIN Respuesta
    ON Encuesta.num_encuesta = Respuesta.num_encuesta
    INNER JOIN Opcion
    ON Respuesta.num_pregunta = Opcion.num_pregunta
    AND Respuesta.num_opcion = Opcion.num_opcion
    AND Respuesta.num_pregunta IN (1, 2, 4);
'''

sql_script_2 = '''
    SELECT respuesta
    FROM Respuesta
    WHERE num_pregunta = 6;
'''

sql_script_3 = '''
    SELECT respuesta
    FROM Respuesta
    WHERE num_pregunta = 7;
'''

# sql_script_1 = '''
#     SELECT Opcion.titulo AS Titulo
#     FROM Encuesta
#     INNER JOIN Respuesta
#     ON Encuesta.num_encuesta = Respuesta.num_encuesta
#     INNER JOIN Opcion
#     ON Respuesta.num_pregunta = Opcion.num_pregunta
#     AND Respuesta.num_opcion = Opcion.num_opcion
#     AND Opcion.num_pregunta = 4
# '''

# sql_script_2 = '''
#     SELECT T1.num_pregunta, T1.femenino, T2.masculino
# 	FROM (
# 		SELECT Respuesta.num_pregunta, COUNT(Respuesta.num_opcion) AS femenino
# 		FROM Respuesta
# 		INNER JOIN Opcion
# 		ON Respuesta.num_pregunta = Opcion.num_pregunta
# 		AND Respuesta.num_opcion = Opcion.num_opcion
# 		AND Opcion.titulo LIKE 'Femenino'
# 	) AS T1
# 	INNER JOIN (
# 		SELECT Respuesta.num_pregunta, COUNT(Respuesta.num_opcion) AS masculino
# 		FROM Respuesta
# 		INNER JOIN Opcion
# 		ON Respuesta.num_pregunta = Opcion.num_pregunta
# 		AND Respuesta.num_opcion = Opcion.num_opcion
# 		AND Opcion.titulo LIKE 'Masculino'
# 	) AS T2
# 	ON T1.num_pregunta = T2.num_pregunta
# '''