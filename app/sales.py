from datetime import date, timedelta
"""Helps clarifying whether the next Sunday is a sales day
"""


class Sales():
    """Contains the manager for reporting back on sales"""

    def __init__(self, current_date: date):
        """Initialize current date

        Args:
            current_date (date): Set date to be calculated
        """
        self.current_date = current_date

    def next_sunday(self, other_date=None):
        """Returns next sunday based on class current_date

        Args:
            other_date (date): If set, uses that date instead of class current_date

        Returns:
            date: Next Sunday
        """

        d = self.current_date
        if other_date is not None:
            d = self.current_date

        delta = 6 - d.weekday()
        if d.weekday() == 6:
            delta += 7

        return d + timedelta(days=delta)

    def is_sunday(self, input_date=None):
        """Returns true if date is a Sunday

        Returns:
            bool: True for Sunday, false for any other
        """
        if input_date is None:
            input_date = self.current_date

        if input_date.weekday() == 6:
            return True
        else:
            return False

    def is_second_sunday_of_month(self, other_date=None):
        """Checks if the date is the second Sunday of month. Uses integer division to see how many 
        full weeks have passed. Because we check if the day is a Sunday itself and returns False,
        we can safely assume it is a Sunday when we do integer division. Just one whole week, and 
        we know this is the second Sunday

        Args:
            other_date (date, optional): Optional for checking other dates than class initial. Defaults to None.

        Returns:
            bool: True for second Sunday, False for any other state
        """
        d = self.current_date
        if other_date is not None:
            d = other_date

        if self.is_sunday(d) == False:
            return False

        if d.day // 7 == 1:
            return True
        else:
            return False

    def next_second_sunday(self, other_date=None):
        """Returns the next second Sunday. Safely iterates forward a week at a time by 
        initially jumping to next Sunday

        Args:
            other_date (date, optional): Optional for checking other dates than class initial. Defaults to None.

        Returns:
            date: Next second Sunday
        """
        d = self.current_date
        if other_date is not None:
            d = other_date

        d = self.next_sunday(d)
        while self.is_second_sunday_of_month(d) == False:
            d = d + timedelta(days=7)

        return d
