


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        report = []
        for op in operations:
            if op == 'C':
                report.pop()
            elif op == 'D':
                report.append(report[-1] * 2)
            elif op == '+':
                report.append(report[-1] + report[-2])
            else:
                report.append(int(op))
        return sum(report)
