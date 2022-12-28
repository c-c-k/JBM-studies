
class Book:
    __next_id = 1
    id = ...
    name = ...
    author = ...
    year_published = ...
    loan_type = ...
    
    def __init__(self, name, author, year_published, loan_type=1, id_=None):
        if id_ is None:
            self.id = Book.__next_id
            Book.__next_id += 1
        else:
            ...
            self.id = id_
        self.name = name
        self.author = author
        self.year_published = year_published
        if 0 < loan_type < 4:
            self.loan_type = loan_type
        else:
            raise ValueError('wrong loan type')


class Books:
    datasource = ...


        
