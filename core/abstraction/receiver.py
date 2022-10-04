# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbsMessageReceiver(ABC):

    @abstractmethod
    async def initialize(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def process_message(self, *args, **kwargs):
        raise NotImplementedError

