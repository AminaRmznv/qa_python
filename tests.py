import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name", ["Человек-амфибия", "Властелин колец", "Хоббит"])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.set_book_genre("Человек-амфибия", "Фантастика")
        assert collector.get_book_genre("Человек-амфибия") == "Фантастика"

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.set_book_genre("Человек-амфибия", "Фантастика")
        genre = collector.get_book_genre("Человек-амфибия")
        assert genre == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.set_book_genre("Человек-амфибия", "Фантастика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert "Человек-амфибия" in books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        books = collector.get_books_genre()
        assert "Человек-амфибия" in books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.set_book_genre("Человек-амфибия", "Фантастика")
        books = collector.get_books_for_children()
        assert "Человек-амфибия" in books

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.add_book_in_favorites("Человек-амфибия")
        assert "Человек-амфибия" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.add_book_in_favorites("Человек-амфибия")
        collector.delete_book_from_favorites("Человек-амфибия")
        assert "Человек-амфибия" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.add_book_in_favorites("Человек-амфибия")
        favorites = collector.get_list_of_favorites_books()
        assert "Человек-амфибия" in favorites

    @pytest.mark.parametrize("book_name,book_genre", [("Человек-амфибия", "Фантастика"), ("Фрэд", "Ужасы")])
    def test_add_book_genre(self, book_name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.get_books_genre()

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.set_book_genre("Человек-амфибия", "Неизвестный жанр")
        assert collector.get_book_genre("Человек-амфибия") == ''

    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_add_new_book_invalid_name_length(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) is None

    def test_add_book_in_favorites_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Человек-амфибия")
        collector.add_book_in_favorites("Человек-амфибия")
        collector.add_book_in_favorites("Человек-амфибия")
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count("Человек-амфибия") == 1
