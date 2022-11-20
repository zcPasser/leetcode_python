class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = float('%.5f' % (celsius + 273.15))
        fahrenheit = float('%.5f' % (celsius * 1.80 + 32.00))

        return [kelvin, fahrenheit]


a = 36.50
b = 122.11
s = Solution()
print(s.convertTemperature(a))
