# qa_python

## BooksCollector Test Documentation
This test suite aims to validate the functionality of the BooksCollector application. The following sections describe the tests written for various functionalities of the app.

Test Descriptions
### Test adding two books

Tests whether two books can be successfully added to the library.
Uses the method add_new_book() twice.
Verifies that the length of the returned list of books from get_books_genre() is 2.

### Test single book addition for validity

Uses parameterized testing to validate the addition of a single book.
Verifies if the added book is in the list of books and if its genre is not set.

### Test setting book genre

Validates if the genre of a book can be successfully set.
Uses the methods add_new_book() and set_book_genre().

### Test getting book genre

Tests the retrieval of a specific book's genre.

### Test getting books of a specific genre

Validates if books of a particular genre can be successfully retrieved.

### Test getting the list of all book genres

Verifies that a newly added book is included in the list of all book genres.
### Test getting books for children

Validates if books suitable for children are successfully retrieved.
### Test adding a book to favorites

Verifies that a book can be added to the favorites list.
### Test deleting a book from favorites

Validates the removal of a book from the favorites list.
### Test getting the list of favorite books

Checks if the retrieval of the favorites list works as expected.
### Test adding and getting book genre

Uses parameterized testing to verify if the genre for a specific book can be added and retrieved.
### Test setting genre for a nonexistent book

Validates that a genre can't be set for a book that doesn't exist in the list.
### Test setting an invalid book genre

Tests that setting an unrecognized genre results in no genre being set.
### Test adding a book with an invalid name length

Uses parameterized testing to validate that books with too short or too long names can't be added.
### Test adding a book to favorites that already exists

Checks that a book can't be added to favorites more than once.