from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, Session

engine = create_engine("sqlite+pysqlite:///tarefas.db", echo=True, future=True)
session = Session(engine)
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoa'
    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome_pessoa = Column(String(45), nullable=False)

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f'nome: {self.nome_pessoa}'


class Tarefa(Base):
    __tablename__ = 'tarefa'
    id_tarefa = Column(Integer, primary_key=True, autoincrement=True)
    nome_tarefa = Column(String(45), nullable=False)
    status = Column(String(20), nullable=False)
    id_pessoa = Column(Integer, ForeignKey('pessoa.id_pessoa'))
    pessoa = relationship('Pessoa')

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f'tarefa: {self.nome_tarefa}\nstatus: {self.status}'


Base.metadata.create_all(engine)
