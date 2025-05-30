import pytest

from src.Product import Product
from src.Category import Category
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


@pytest.fixture
def sample_product() -> Product:
    """Fixture that returns a sample product for testing."""
    return Product("Test Product", "Test Description", 100.0, 10)

@pytest.fixture
def sample_smartphone() -> Smartphone:
    """Fixture that returns a sample smartphone for testing."""
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def sample_grass() -> Smartphone:
    """Fixture that returns a sample grass for testing."""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

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

def test_str_and_add(sample_product, sample_category):
    assert sample_category.product == str(sample_product)
    assert str(sample_category) == f"{sample_category.name}, количество продуктов: 10 шт."
    product1 = Product("Product 1", "Desc 1", 100.0, 5)
    product2 = Product("Product 2", "Desc 2", 200.0, 3)
    assert product1 + product2 == 100*5 + 200*3

def test_smartphone_grass(sample_smartphone, sample_grass, sample_category):
    with pytest.raises(TypeError):
        sample_smartphone + sample_grass
    with pytest.raises(TypeError):
        sample_category.add_product("sample_smartphone")

def test_print_mixin(capsys):
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"

def test_middle_price_zero():
    c = Category("Test Category", "Test Description", [])
    assert c.middle_price() == 0

def test_middle_price(sample_category):
    assert sample_category.middle_price() == 100



