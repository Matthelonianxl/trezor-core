# Automatically generated by pb2py
import protobuf as p


class StellarAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 208
    FIELDS = {
        1: ('address', p.UnicodeType, 0),
    }

    def __init__(
        self,
        address: str = None
    ) -> None:
        self.address = address