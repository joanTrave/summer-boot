from summer.patterns.singleton_meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        ...


def test_singleton_meta():
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)