import pytest

from src.Product import Product
from src.Category import Category


@pytest.fixture
def sample_product() -> Product:
    """Fixture that returns a sample product for testing."""
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    """Fixture that returns a sample category for testing."""
    return Category("Test Category", "Test Description", [sample_product,])


@pytest.fixture
def dict_of_product() -> dict:
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}


def test_product_initialization(sample_product: Product) -> None:
    """Test product initialization with correct values."""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_category_initialization(
    sample_category: Category,
    sample_product: Product,
) -> None:
    """Test category initialization with correct values"""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert sample_category.product == str(sample_product)

def test_category_count() -> None:
    """Test category and product counting."""
    # Сбрасываем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Создаем тестовые продукты
    product1 = Product("Product 1", "Desc 1", 100.0, 5)
    product2 = Product("Product 2", "Desc 2", 200.0, 3)

    # Создаем категории
    Category("Category 1", "Desc 1", [product1])
    Category("Category 2", "Desc 2", [product1, product2])

    assert Category.category_count == 2
    # Общее количество продуктов в категориях
    assert Category.product_count == 3


def test_product_new_product( dict_of_product):
    new_product1 = Product.new_product(dict_of_product)
    assert  new_product1.name == "Samsung Galaxy S23 Ultra"
    assert  new_product1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product1.price == 180000.0
    assert new_product1.quantity == 5


