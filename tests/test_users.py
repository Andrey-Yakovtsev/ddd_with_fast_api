from sqlalchemy import text

from ddd_app.domain import clear_models
from ddd_app.adapters import declarative_orm as orm


def test_orderline_mapper_can_load_lines(session):
    session.execute(text(
        "INSERT INTO address (id, country, city, street, post_code, house, apartment) VALUES "
        '(1, "UK", "London", "BakerStreet", 12345, 1, 1),'
        '(2, "GB", "Berlin", "BakerStreet", 12345, 1, 2),'
        '(3, "RUS", "Moscow", "BakerStreet", 12345, 1, 3)'
    ))
    expected = [
        orm.Address(id=1, country="UK", city="London",
                       street="BakerStreet", post_code=12345, house=1, apartment=1),
        orm.Address(id=2, country="GB", city="Berlin", street="BakerStreet",
                       post_code=12345, house=1, apartment=2),
        orm.Address(id=3, country="RUS", city="Moscow", street="BakerStreet",
                       post_code=12345, house=1, apartment=3),
    ]
    db_entries = session.query(orm.Address).all()
    print(db_entries)
    print('expected===>', expected)
    assert db_entries == expected