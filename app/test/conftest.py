from app.db.connection import Session
import pytest
from app.db.models import Category as CategoryModels
from app.db.models import Product as ProductModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModels(name='Roupa', slug='roupa'),
        CategoryModels(name='Brinquedos', slug='brinquedos'),
        CategoryModels(name='Itens de Cozinha', slug='itens-de-cozinha'),
        CategoryModels(name='Decoracao', slug='decoracao'),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModels(name='Carro', slug='carro')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camisa-adidas',
        slug='camisa-adidas',
        price=100.99,
        stock=20,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()
