from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData

class IntitutionUseCase:
    def __init__(self, intitution_repository):
        self.intitution_repository = intitution_repository

    def get_intitution(self):
        """"
            resuelve los casos de uso del endpoint get
        :return:
        """
        data_response = []
        institutions = self.intitution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address
                )

            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response

        )

        return response

    def get_id_intitution(self, institution_id):

        data_response = []
        institutions = self.intitution_repository.get_id_institution(institution_id)

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                    created_user=i.created_user,
                    created_at=i.created_at,
                    updated_user=i.updated_user,
                    updated_at=i.updated_at,
                    status=i.status

                )

            )

        if not data_response:
            return {'mensaje': "id no encontrado"}

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response

        )

        return response

    def delete_intitution(self, institution_id):
        self.intitution_repository.delete_institution(institution_id)
        return {'mensaje': "institucion eliminada"}

    def insert_intitution(self, body):
        self.intitution_repository.insert_institution(body)
        return {'mensaje': "institucion ingresada con exito"}