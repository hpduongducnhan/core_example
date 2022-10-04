# -*- coding: utf-8 -*-
from abc import ABC
from .validator import AbsValidator


class AbsAppContext(ABC):
    pass


# for circular import
class AppContextValidator(AbsValidator):
    def __init__(self) -> None:
        self.default = None

    def validate(self, value):
        if not isinstance(value, AbsAppContext):
            raise TypeError(f'Expected {value!r} to be an instance of AbsAppContext')
