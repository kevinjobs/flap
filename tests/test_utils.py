from app.utils.short_uuid import short_uuid


def test_short_uuid():
    print(short_uuid())
    assert len(short_uuid()) == 8
