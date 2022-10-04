from typing import Dict
from core.abstraction import SingletonClass
from core.abstraction import AbsHandlerManager
from core.abstraction import AbsHandler
from .aa_facebook_handler import AaFacebookHandler
from .aa_livechat_handler import AaLiveChatHandler
from .aa_zalo_handler import AaZaloHandler
from core.schema import CoreChatInputMessage


class BaseAaManager(SingletonClass, AbsHandlerManager):

    def _singleton_init(self, **kwargs):
        self._initialized: bool = False
        self._chat_type_handlers: Dict[str, AbsHandler] = {}

    async def _get_handlers(self):
        handlers: Dict[str, AbsHandler] = {}
        for handler_class in (AaZaloHandler, AaLiveChatHandler, AaFacebookHandler,):
            handler_instance = handler_class()
            handlers.update({handler_instance.chat_type: handler_instance})
        return handlers

    async def initialize(self, *args, **kwargs):
        if self._initialized:
            return
        self._chat_type_handlers = await self._get_handlers()
        self._initialized = True
        print(f'initialize {self.__class__.__name__} {self._chat_type_handlers=}')

    async def process_message(self, message: CoreChatInputMessage, **kwargs):
        handler = self._chat_type_handlers.get(message.chat_type)
        if handler:
            # print(f'{self.__class__.__name__} {message.chat_type=} found {handler=}')
            await handler.handle(message, **kwargs)
        else:
            print(f'{self.__class__.__name__} not found handler for {message.chat_type=}')

