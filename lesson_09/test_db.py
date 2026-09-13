import pytest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = (
    "postgresql://postgres:87BvggJ--kdJrYQ."
    "Ef4rxKncxyPsM9@localhost:5433/postgres"
)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    """Модель таблицы students."""

    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)


Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    """Сессия БД."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture
def created_student(db_session):
    """Создание и обязательное удаление записи после теста."""
    student = Student(first_name="Test", last_name="Student")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    yield student

    existing = (
        db_session.query(Student)
        .filter_by(student_id=student.student_id)
        .first()
    )
    if existing:
        db_session.delete(existing)
        db_session.commit()


def test_add_student(db_session):
    """1. Тест добавления."""
    new_student = Student(first_name="Ivan", last_name="Petrov")
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    assert new_student.student_id is not None

    fetched = (
        db_session.query(Student)
        .filter_by(student_id=new_student.student_id)
        .first()
    )
    assert fetched is not None
    assert fetched.first_name == "Ivan"

    db_session.delete(fetched)
    db_session.commit()


def test_update_student(db_session, created_student):
    """2. Тест изменения."""
    created_student.first_name = "UpdatedName"
    db_session.commit()

    updated = (
        db_session.query(Student)
        .filter_by(student_id=created_student.student_id)
        .first()
    )
    assert updated.first_name == "UpdatedName"


def test_delete_student(db_session, created_student):
    """3. Тест удаления."""
    student_id = created_student.student_id

    db_session.delete(created_student)
    db_session.commit()

    deleted = (
        db_session.query(Student).filter_by(student_id=student_id).first()
    )
    assert deleted is None
