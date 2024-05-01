from sqlalchemy import text

from ddd_app.domain import models


def test_orderline_mapper_can_load_lines(session):
    session.execute(text(
        "INSERT INTO address (id, country, city, street, post_code, house, apartment) VALUES "
        '(1, "UK", "London", "BakerStreet", 12345, 1, 1),'
        '(2, "GB", "Berlin", "Baker_2", 12345, 1, 2),'
        '(3, "RUS", "Moscow", "Baker_3", 12345, 1, 3)'
    ))
    expected = [
        models.Address(1, "UK", "London", "BakerStreet", 12345, 1, 1),
        models.Address(2, "GB", "Berlin", "Baker_2", 12345, 1, 2),
        models.Address(3, "RUS", "Moscow", "Baker_3", 12345, 1, 3),
    ]
    assert session.query(models.Address).all() == expected