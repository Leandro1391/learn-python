class NumbersEqualsException(Exception):

    def __init__(self, msg: str):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, msg):
        self._msg = msg

    def __str__(self) -> str:
        return f'NumbersEqualsException(Exception): [msg: {self._msg}]'