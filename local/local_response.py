from result_wrapper import ResultWrapper


class LocalResponse(ResultWrapper):
    def __init__(self, msg: str, status: bool, data):
        self.msg = msg
        self.status = status
        self.data = data

    def get_extra_data(self) -> dict:
        return {}

    def get_status(self) -> bool:
        return self.status

    def get_data(self):
        return self.data

    def get_message(self) -> str:
        return self.msg