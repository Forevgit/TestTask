from rest_framework.exceptions import APIException

class InvalidPatientDateOfBirthEx(APIException):
    status_code = 400
    default_detail = 'Date of birth can not be in the future'
    default_code = 'invalid_date_of_birth'


class PermissionDeniedEx(APIException):
    status_code = 400
    default_detail = 'You dont have access to this patient'
    default_code = 'denied_permission'