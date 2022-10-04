from core.abstraction import SingletonClass
from core.abstraction import AbsAppContext


class BaseAppContext(SingletonClass, AbsAppContext):
    def _singleton_init(self, **kwargs):
        pass

    