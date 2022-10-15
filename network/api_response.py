import json
from requests import Response

from result_wrapper import ResultWrapper


class ApiResponse(ResultWrapper):
    def __init__(self, msg: str, status: bool, data, status_code: int = 0):
        self.msg = msg
        self.status = status
        self.data = data
        self.status_code = status_code

    def get_data(self):
        return self.data

    def get_message(self) -> str:
        return self.msg

    def get_status(self) -> bool:
        return self.status

    def get_extra_data(self) -> dict:
        return {'status_code': self.status_code}


def parse_response(json_str: str, status_code) -> ApiResponse:
    obj = json.JSONDecoder().decode(json_str)
    return ApiResponse(obj['message'], obj['status'], obj['data'], status_code)


def parse_response(response: Response) -> ApiResponse:
    return parse_response(response.text, response.status_code)
