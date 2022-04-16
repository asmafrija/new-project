from enum import Enum

class ReclamationStatus(str, Enum):
    pending = "pending"
    treated = "treated"
