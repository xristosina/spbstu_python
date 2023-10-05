
information_volume_of_diskette_in_mb = 1.44
pages_in_the_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_for_one_symbol = 4
one_book_in_bytes = bytes_for_one_symbol * symbols_per_line * lines_per_page * pages_in_the_book
book_in_mb = (one_book_in_bytes / 1024) / 1024
books_per_diskette = information_volume_of_diskette_in_mb // book_in_mb
print("Количество книг, помещающихся на дискету:", int(books_per_diskette))
