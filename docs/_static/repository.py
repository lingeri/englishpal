import abc
import model
import pickle

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()

class PickleRepository(AbstractRepository):

    def __init__(self, path = None):
        self.path = path

    def add(self, batch):
        batch_lst = list()
        batch_lst.append(batch)
        with open(self.path, 'wb') as f:
            pickle.dump(batch_lst, f)

    def get(self, reference):
        batch_lst = list()
        for batch in batch_lst:
            if reference == batch.reference:
                return batch

    def list(self):
        lst = []
        with open(self.path, 'rb') as f:
            lst = pickle.load(f)
        return lst