import abc


class BaseGenerator(abc.ABC):
    """
    This class will be used a base class for any ETL process the app uses
    """

    @abc.abstractmethod
    def extract(self) -> None:
        pass

    @abc.abstractmethod
    def transform(self) -> None:
        pass

    @abc.abstractmethod
    def load(self) -> None:
        pass

    def run(self):
        self.extract()
        self.transform()
        self.load()
