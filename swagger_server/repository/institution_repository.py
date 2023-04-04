sql_select = "select * from institution where status = 'A'"


class IntitutionRepository:
    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        """
            resuelve la consulta a la base de datos
        return:
        """
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows
    #funcion obtener informacion por id
    def get_id_institution(self, institution_id):
        sql_select_id = "select * from institution where status = 'A' and id = '{0}'". format(institution_id)
        with self.session_factory() as session:
            rows = session.execute(sql_select_id)
            return rows

    #funcion borrar por id
    def delete_institution(self, institution_id):
        sql_select_delete = "DELETE FROM institution WHERE id = '{0}'".format(institution_id)
        with self.session_factory() as session:
            session.execute(sql_select_delete)
            session.commit()
            return {'mensaje': "institucion borrada"}

    #funcion ingresar nueva institucion
    def insert_institution(self, body):

        sql_count = "select * from institution"
        with self.session_factory() as count:
            rows = count.execute(sql_count)
            contador = len(rows.fetchall())
            new_id = int(contador) + 1

        #sql_select_insert = "INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES (3, '{0}', '{1}', '{2}', '{3}', '2023-04-04 12:24:58', null, null, 'A')".format(body['name'], body['description'], body['address'], body['createdUser'])

        sql_select_insert = "INSERT INTO institution (id, name, description, address, created_user, created_at, updated_user, updated_at, status) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '2023-04-04 12:24:58', null, null, 'A')".format(new_id, body.name, body.description, body.address, body.created_user)

        with self.session_factory() as session:
            session.execute(sql_select_insert)
            session.commit()
            return {'mensaje': "institucion ingresada con exito"}