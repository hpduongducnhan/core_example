from core.abstraction import AbsHandler




class BaseBbHandler(AbsHandler):
    async def handle(self, message, **kwargs):
        print(f'{self.__class__.__name__} handle message {message}')