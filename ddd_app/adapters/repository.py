import abc

from ddd_app.domain import models


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, entry):
        self.session.add(entry)

    def get(self, reference):
        return self.session.query(models.User).filter_by(id=reference).one()

    def list(self):
        return self.session.query(models.User).all()
