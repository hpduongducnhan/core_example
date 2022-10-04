from typing import Dict
from core.abstraction import AbsMessageReceiver
from core.abstraction import SingletonClass
from core.abstraction import AbsRouter
from core.router import MessageTextRouter, MessageEmojiRouter
from core.schema import CoreChatInputMessage


class BaseMessageReceiver(SingletonClass, AbsMessageReceiver):
    def _singleton_init(self, **kwargs):
        self._initialized: bool = False
        self._routers: Dict[str, AbsRouter] = {}

    async def _get_routers(self) -> Dict[str, AbsRouter]:        
        router: Dict[str, AbsRouter] = {}
        for router_class in (MessageTextRouter, MessageEmojiRouter,):
            router_instance = router_class()
            await router_instance.initialize()
            router.update({router_instance.msg_type: router_instance})
        return router

    async def initialize(self, *args, **kwargs):
        # call this method right after init class
        if self._initialized:
            return 

        self._routers = await self._get_routers()

        self._initialized = True

    async def process_message(self, message: CoreChatInputMessage, **kwargs):
        router = self._routers.get(message.msg_type)
        if router:
            # print(f'{message.msg_type=} found {router=}')
            await router.process_message(message)
        else:
            print(f'not found router for {message.msg_type=}')
        