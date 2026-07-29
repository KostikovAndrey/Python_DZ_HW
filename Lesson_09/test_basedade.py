import uuid
from conftest import Subject


def test_add_subject(db_session):
    unique_id = str(uuid.uuid4())[:8]
    test_title = f"Математика_{unique_id}"

    new_subject = Subject(subject_title=test_title)
    db_session.add(new_subject)
    db_session.flush()

    assert new_subject.subject_id is not None

    saved_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=new_subject.subject_id)
        .first()
    )
    assert saved_subject is not None
    assert saved_subject.subject_title == test_title


def test_update_subject(db_session):
    unique_id = str(uuid.uuid4())[:8]
    original_title = f"Физика_{unique_id}"
    updated_title = f"Физика (углубленный курс)_{unique_id}"

    subject = Subject(subject_title=original_title)
    db_session.add(subject)
    db_session.flush()

    subject.subject_title = updated_title
    db_session.flush()

    updated_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject.subject_id)
        .first()
    )
    assert updated_subject is not None
    assert updated_subject.subject_title == updated_title

    old_subject = (
        db_session.query(Subject)
        .filter_by(subject_title=original_title)
        .first()
    )
    assert old_subject is None


def test_delete_subject(db_session):
    unique_id = str(uuid.uuid4())[:8]
    test_title = f"Химия_{unique_id}"

    subject = Subject(subject_title=test_title)
    db_session.add(subject)
    db_session.flush()
    subject_id = subject.subject_id

    created_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert created_subject is not None
    assert created_subject.subject_title == test_title

    db_session.delete(created_subject)
    db_session.flush()

    deleted_subject = (
        db_session.query(Subject)
        .filter_by(subject_id=subject_id)
        .first()
    )
    assert deleted_subject is None
