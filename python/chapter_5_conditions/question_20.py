#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# ------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------
from python.jbm_helper import test_answer


# ------------------------------------------------------------
# MESSAGES
# ------------------------------------------------------------
MSG_ID = "Customer ID: "
MSG_TOTAL_VAL = "Total value of all products the customer bought: "
MSG_ALWAYS_PAY = "Did the customer always pay on time? (y/n): "
MSG_LOYALTY = "How many years has the customer been buying from the company? : "
MSG_TREATMENT_SPECIAL = "give customer {customer_id} special treatment."
MSG_TREATMENT_NORMAL = "give customer {customer_id} normal treatment."
MIN_TOTAL_PAY = 8000
MIN_YEARS = 5


# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------
def main():
    customer_id = input(MSG_ID)
    total_pay = float(input(MSG_TOTAL_VAL))
    pay_on_time = input(MSG_ALWAYS_PAY) == "y"
    years = int(input(MSG_LOYALTY))
    preferred_customer = pay_on_time or (
            total_pay >= MIN_TOTAL_PAY and years > MIN_YEARS)
    msg = MSG_TREATMENT_SPECIAL if preferred_customer else MSG_TREATMENT_NORMAL
    print(msg.format(customer_id=customer_id))


# ------------------------------------------------------------
# TEST
# ------------------------------------------------------------
class TestAnswer(test_answer.TestAnswer):
    base_output = "".join((
        MSG_ID, MSG_TOTAL_VAL, MSG_ALWAYS_PAY, MSG_LOYALTY))
    customer_id = "012345"
    positive_output = (
            base_output
            + MSG_TREATMENT_SPECIAL.format(customer_id=customer_id) + "\n"
    )
    negative_output = (
            base_output
            + MSG_TREATMENT_NORMAL.format(customer_id=customer_id) + "\n"
    )

    def test_answer_1(self):
        self.set_stdin(f"{self.customer_id}\n7999\nn\n10")
        self.expected_output = self.negative_output
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)

    def test_answer_2(self):
        self.set_stdin(f"{self.customer_id}\n8000\nn\n10")
        self.expected_output = self.positive_output
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)

    def test_answer_3(self):
        self.set_stdin(f"{self.customer_id}\n7999\ny\n10")
        self.expected_output = self.positive_output
        main()
        output = self.test_stdout.getvalue()
        self.assertEqual(output, self.expected_output)


# ------------------------------------------------------------
# PROGRAM CODE
# ------------------------------------------------------------
if __name__ == "__main__":
    test_answer.unittest.main()
    # main()
