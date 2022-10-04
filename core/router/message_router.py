from .base import BaseRouter
from core.schema import CoreChatInputMessage
from core.aa_handler import AaManager
from core.bb_handler import BbManager


class MessageTextRouter(BaseRouter):
    msg_type: str = 'text'

    def _singleton_init(self, **kwargs):
        self.aa_manager = AaManager()
        self.bb_manager = BbManager()
        
    async def initialize(self, *args, **kwargs):
        await self.aa_manager.initialize()
        await self.bb_manager.initialize()


    async def process_message(self, message: CoreChatInputMessage, **kwargs):
        await self.bb_manager.process_message(message)
        await self.aa_manager.process_message(message)
        