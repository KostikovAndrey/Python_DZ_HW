from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pytest

DATABASE_URL = "postgresql://postgres:ndr@localhost:5432/postgres"

Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_title = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Subject(id={self.subject_id}, title='{self.subject_title}')>"


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.begin()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
