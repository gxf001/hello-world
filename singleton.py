"""The singleton metaclass for ensuring only one instance of a class."""
import abc


class Singleton(abc.ABCMeta, type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method for the singleton metaclass."""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AbstractSingleton(abc.ABC, metaclass=Singleton):
    """
    Abstract singleton class for ensuring only one instance of a class.
    """

    pass

# 这段代码实现了一个单例模式的元类（metaclass）。元类是 Python 中比较高级的概念，它可以用来控制类的创建过程。

# 该元类的作用是确保一个类只有一个实例，并提供了一种方式来访问该实例。在该元类中，使用了 Python 的多重继承和元类机制，定义了一个 `Singleton` 类，它同时继承了 `abc.ABCMeta` 和 `type` 类。

# 当一个类使用了该元类时，该类在实例化时只会生成一个实例，该实例将被缓存起来。如果下次需要该类的实例时，直接返回之前缓存的实例，从而保证了该类只有一个实例存在。

# 此外，该元类还定义了一个抽象单例类 `AbstractSingleton`，当一个类需要实现单例模式时，可以继承该类，并实现自己的业务逻辑。