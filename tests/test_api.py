from django.urls import reverse

import pytest 

import requests

from posts.models import Category,Subcategory
url_list_product = "http://127.0.0.1:8000" + reverse('product-list')
url_detail_product = "http://127.0.0.1:8000/api/v1/posts/product/"
url_list_category = "http://127.0.0.1:8000" + reverse('category-list')
url_detail_category = "http://127.0.0.1:8000/api/v1/posts/category/"
url_list_subcategory = "http://127.0.0.1:8000" + reverse('subcategory-list')
url_detail_subcategory = "http://127.0.0.1:8000/api/v1/posts/subcategory/"

@pytest.fixture()
def subcategory(db):
    category = Category.objects.create(title='title')
    return Subcategory.objects.create(title='title',category=category)


@pytest.fixture()
def category(db):
    return Category.objects.create(title='title')


def test_product_get_list():
    response = requests.get(url_detail_product+'1/',)
    assert response.status_code == 200


def test_product_get_retrieve():
    response = requests.get(url_list_product)
    assert response.status_code == 200


def test_product_create(subcategory):
    data = {
        "title": "test",
        "descriptions": "test",
        "price": 15552.12,
        "subcategory": subcategory.id
    }
    len_products_before = len(requests.get(url_list_product).json())
    product = requests.post(url=url_list_product,data=data).json()
    len_products_after = len(requests.get(url_list_product).json())
    
    assert len_products_before == len_products_after - 1
    assert product.get('title') == data.get('title')
    assert product.get('subcategory') == subcategory.id


def test_product_put():
    data = {
        "title": "test1",
        "descriptions": "test",
        "price": 15552.12,
        "subcategory": 1
    }
    response = requests.put(url_detail_product+'1/',data=data).json()
    print(response)
    product_after = requests.get(url_detail_product+'1/',).json()

    assert product_after.get('title') == data.get('title')
    assert product_after.get('subcategory') == data.get('subcategory')
    assert float(product_after.get('price')) == data.get('price')
    assert product_after.get('descriptions') == data.get('descriptions')


def test_product_patch():
    data = {
        "title": "test",
    }
    requests.patch(url_detail_product+'1/',data=data).json()
    product_after = requests.get(url_detail_product+'1/').json()

    assert product_after.get('title') == data.get('title')


def test_product_delete():
    
    products = requests.get(url_list_product).json()
    product = products[-1]
    id = product.get('id')
    response_delete = requests.delete(url_detail_product+str(id))
    response = requests.get(url_detail_product+str(id))

    assert response_delete.status_code == 204
    assert response.status_code == 404

# -----


def test_category_get_list():
    response = requests.get(url_detail_category+'1/',)
    assert response.status_code == 200


def test_category_get_retrieve():
    response = requests.get(url_list_category)
    assert response.status_code == 200


def test_category_create():
    data = {
        "title": "test"
    }
    len_products_before = len(requests.get(url_list_category).json())
    product = requests.post(url=url_list_category,data=data).json()
    len_products_after = len(requests.get(url_list_category).json())
    
    print(len_products_before)
    assert len_products_before == len_products_after - 1
    assert product.get('title') == data.get('title')


def test_category_put():
    data = {
        "title": "test1",
    }
    response = requests.put(url_detail_category+'1/',data=data).json()
    print(response)
    product_after = requests.get(url_detail_category+'1/',).json()

    assert product_after.get('title') == data.get('title')


def test_category_patch():
    data = {
        "title": "test2",
    }
    requests.patch(url_detail_category+'1/',data=data).json()
    product_after = requests.get(url_detail_category+'1/').json()

    assert product_after.get('title') == data.get('title')


def test_category_delete():
    
    products = requests.get(url_list_category).json()
    product = products[-1]
    id = product.get('id')
    response_delete = requests.delete(url_detail_category+str(id))
    response = requests.get(url_detail_category+str(id))

    assert response_delete.status_code == 204
    assert response.status_code == 404


# --------


def test_subcategory_get_list():
    response = requests.get(url_detail_subcategory+'1/',)
    assert response.status_code == 200


def test_subcategory_get_retrieve():
    response = requests.get(url_list_subcategory)
    assert response.status_code == 200


def test_subcategory_create(category):
    data = {
        "title": "test",
        "category":category.id
    }
    len_products_before = len(requests.get(url_list_subcategory).json())
    product = requests.post(url=url_list_subcategory,data=data).json()
    len_products_after = len(requests.get(url_list_subcategory).json())
    
    print(len_products_before)
    assert len_products_before == len_products_after - 1
    assert product.get('title') == data.get('title')


def test_subcategory_put(category):
    data = {
        "title": "test1",
        "category":category.id
    }
    response = requests.put(url_detail_subcategory+'1/',data=data).json()
    print(response)
    product_after = requests.get(url_detail_subcategory+'1/',).json()

    assert product_after.get('title') == data.get('title')


def test_subcategory_patch():
    data = {
        "title": "test2",
    }
    requests.patch(url_detail_subcategory+'1/',data=data).json()
    product_after = requests.get(url_detail_subcategory+'1/').json()

    assert product_after.get('title') == data.get('title')


def test_subcategory_delete():
    
    products = requests.get(url_list_subcategory).json()
    product = products[-1]
    id = product.get('id')
    response_delete = requests.delete(url_detail_subcategory+str(id))
    response = requests.get(url_detail_subcategory+str(id))

    assert response_delete.status_code == 204
    assert response.status_code == 404
