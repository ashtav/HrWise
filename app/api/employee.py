from flask import Blueprint, request
from flask_restful import Resource, Api
from ..utils.employee_assessment import EmployeeAssessment

employee_bp = Blueprint('employee', __name__)
api = Api(employee_bp)


class Employee(Resource):
    @staticmethod
    def get():
        return {'hello': 'worlds'}, 200  # 200 adalah kode status HTTP untuk 'OK'

    @staticmethod
    def post():
        try:
            data = request.get_json()
            result = EmployeeAssessment(data).get_result()

            response = {
                "ok": True,
                "data": result.to_dict(orient='records'),
                "message": "Success"
            }
        except Exception as e:
            response = {
                "ok": False,
                "message": "An error occurred: " + str(e)
            }

            return response, 500

        return response, 201


api.add_resource(Employee, '/employee')
