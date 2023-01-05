sql_script_1 = '''
    SELECT Opcion.titulo AS Titulo
    FROM Encuesta
    INNER JOIN Respuesta
    ON Encuesta.num_encuesta = Respuesta.num_encuesta
    INNER JOIN Opcion
    ON Respuesta.num_pregunta = Opcion.num_pregunta
    AND Respuesta.num_opcion = Opcion.num_opcion
    AND Opcion.num_pregunta = 4
'''