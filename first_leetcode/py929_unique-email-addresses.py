

import re
import sys


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        real_address = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.replace('.', '') #re.sub('.', '', local_name)
            local_name = local_name.split('+', 1)[0]

            real_address.add(local_name + '@' + domain_name)

        return len(real_address)


emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
s = Solution()
print(s.numUniqueEmails(emails))