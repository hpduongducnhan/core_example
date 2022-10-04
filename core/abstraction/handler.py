# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbsHandlerManager(ABC):
    @abstractmethod
    async def process_message(self, *args, **kwargs):
        raise NotImplementedError


class AbsHandler(ABC):
    chat_type: str = None    

    @abstractmethod
    async def handle(self, *args, **kwargs):
        raise NotImplementedError

