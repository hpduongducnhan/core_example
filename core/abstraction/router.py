# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from .validator import AbsValidator


class AbsRouter(ABC):
    msg_type: str = None

    @abstractmethod
    async def initialize(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def process_message(self, *args, **kwargs):
        raise NotImplementedError

