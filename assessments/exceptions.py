from rest_framework.exceptions import APIException

class InvalidScoreEx(APIException):
    status_code = 400
    default_detail = 'The final score can not be lower than 0'
    default_code = 'invalid_score'