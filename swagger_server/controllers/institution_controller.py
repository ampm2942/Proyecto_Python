import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server import util
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from flask.views import MethodView
from swagger_server.models.response400 import Response400
from swagger_server.repository.institution_repository import IntitutionRepository
from swagger_server.use_case.institution_use_case import IntitutionUseCase

class IntitutionView(MethodView):

    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        intitution_repository = IntitutionRepository(sqlalchemy_client)
        intitution_usecase = IntitutionUseCase(intitution_repository)
        self.intitution_usecase = intitution_usecase

    def add_institution(self, body):  # noqa: E501
        """Agrega una nueva instituciÃ³n

        Agrega una nueva instituciÃ³n # noqa: E501

        :param body: Crea una nueva instituciÃ³n
        :type body: dict | bytes

        :rtype: InlineResponse200
        """
        if connexion.request.is_json:
            body = RequestInstitutionAdd.from_dict(connexion.request.get_json())  # noqa: E501
            try:

                response = self.intitution_usecase.insert_intitution(body)

            except Exception as ex:
                message = str(ex)
                response = Response400(
                    code=-1,
                    message=message

                )
            return response


    def delete_institution(self, institution_id):  # noqa: E501
        """Elimina una instituciÃ³n

        Elimina una instituciÃ³n # noqa: E501

        :param institution_id: Institution id to delete
        :type institution_id: int

        :rtype: InlineResponse200
        """
        #return 'do some magic!'

        try:

            response = self.intitution_usecase.delete_intitution(institution_id)

        except Exception as ex:
            message = str(ex)
            response = Response400(
                code=-1,
                message=message

            )
        return response




    def get_institution(self):  # noqa: E501
        """Lista instituciones

        Lista instituciones # noqa: E501


        :rtype: InlineResponse200
        """
        try:

            response = self.intitution_usecase.get_intitution()

        except Exception as ex:
            message = str(ex)
            response = Response400(
                code=-1,
                message=message

            )
        return response


    def get_institution_by_id(self, institution_id):  # noqa: E501
        """Busca una instituciÃ³n por ID

        Busca una instituciÃ³n por ID # noqa: E501

        :param institution_id: Busca una instituciÃ³n por ID
        :type institution_id: int

        :rtype: InlineResponse200
        """

        #
        try:

            response = self.intitution_usecase.get_id_intitution(institution_id)

        except Exception as ex:
            message = str(ex)
            response = Response400(
                code=-1,
                message=message

            )
        return response
        #
        #return 'do some magic!'


    def update_institution(self, body):  # noqa: E501
        """Actualiza una instituciÃ³n existente

        Actualiza una instituciÃ³n existente # noqa: E501

        :param body: Actualiza una instituciÃ³n existente
        :type body: dict | bytes

        :rtype: InlineResponse200
        """
        if connexion.request.is_json:
            body = RequestInstitutionUpd.from_dict(connexion.request.get_json())  # noqa: E501
        return 'do some magic!'
