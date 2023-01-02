# -*- coding: utf-8 -*-

"""Summary

Description
"""

import dataclasses as dc
import datetime as dt

from dal.base_model import BaseModel
from dal.fields import (
    IntegerField, CharField, DateField, ChoiceField,
    PrimaryKeyField, ForeignKeyField,
)

LOAN_TYPES = {1: 10, 2: 5, 3:2}

@dc.dataclass
class BooksModel(BaseModel):
    id: PrimaryKeyField = PrimaryKeyField()
    name: CharField = CharField(min_length=1, max_length=1024)
    author: CharField = CharField(min_length=1, max_length=256)
    year_published: DateField = DateField()
    loan_type: ChoiceField = ChoiceField((1, 2, 3))


@dc.dataclass
class CustomersModel(BaseModel):
    id: PrimaryKeyField = PrimaryKeyField()
    name: CharField = CharField(min_length=2, max_length=64)
    city: CharField = CharField(max_length=64, default='')
    age: IntegerField = IntegerField(min_value=6)


@dc.dataclass
class LoansModel(BaseModel):
    customer_id: ForeignKeyField = ForeignKeyField(CustomersModel)
    book_id: ForeignKeyField = ForeignKeyField(BooksModel)
    loan_date: DateField = DateField()
    return_date: DateField = DateField()
