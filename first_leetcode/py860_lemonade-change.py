"""
description:
    1、At a lemonade stand, each lemonade costs $5.
    2、Given an integer array bills where bills[i] is the bill the ith customer pays
    3、Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
    4、Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
    5、ou must provide the correct change to each customer so that the net transaction is that the customer pays $5.
    6、you do not have any change in hand at first.

return:
    true if you can provide every customer with the correct change, or false otherwise.

"""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        if bills[0] != 5:
            return False
        value_to_cnt = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            value_to_cnt[bill] += 1
            if bill == 10:
                if value_to_cnt[5] == 0:
                    return False
                value_to_cnt[5] -= 1
            elif bill == 20:
                if value_to_cnt[10] > 0 and value_to_cnt[5] > 0:
                    value_to_cnt[10] -= 1
                    value_to_cnt[5] -= 1
                elif value_to_cnt[5] > 2:
                    value_to_cnt[5] -= 3
                else:
                    return False

        return True
