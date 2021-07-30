class Fan:
    def wings(self, c, l, d, n):
        self._color = c
        self._length = l
        self._dust = d
        self._number = n

    def motor(self, s, h):
        self._speed = s
        self._heat = h

    def display_fan(self):
        print(f"The color of the fan is {self._color}")
        print(f"The length of the fan is {self._length}m")
        print(f"The fan has dust. True/False - {self._dust}")
        print(f"The number of the fan(s) is/are {self._number}")
        print(f"The speed of the fan is {self._speed}rpm")
        print(f"The fan gives heat. True/False - {self._heat}")

fan = Fan()
fan.wings("white", 1, True, 2)
fan.motor("200", True)
fan.display_fan()
