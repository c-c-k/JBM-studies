#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Summary

Description
"""

import controlers
import settings
import utils


def main():
    if settings.DEMO_MODE:
        utils.extract_book_data()
        utils.extract_client_data()
        utils.gen_loan_data()
    controlers.main()


if __name__ == "__main__":
    main()
