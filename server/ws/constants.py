from enum import Enum


class OrderEvent(Enum):
    Created = 1
    Updated = 2
    Deleted = 3
