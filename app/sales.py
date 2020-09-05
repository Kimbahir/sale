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

        # if other_date is None:
        #     delta = 6-self.current_date.weekday()
        #     if self.today_is_sunday():
        #         delta += 7
        #     return self.current_date + timedelta(days=delta)
        # else:
        #     delta = 6-other_date.weekday()
        #     if self.is_sunday(other_date):
        #         delta += 7
        #     return other_date + timedelta(days=delta)

    def today_is_sunday(self):
        """Returns if current day of class is a Sunday

        Returns:
            bool: True for Sunday, false for any other
        """

        if self.current_date.weekday() == 6:
            return True
        else:
            return False

    def is_sunday(self, input_date=None):
        if input_date is None:
            input_date = self.current_date

        if input_date.weekday() == 6:
            return True
        else:
            return False

    def is_second_sunday_of_month(self, other_date=None):
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
        d = self.current_date
        if other_date is not None:
            d = other_date

        d = self.next_sunday(d)
        while self.is_second_sunday_of_month(d) == False:
            d = d + timedelta(days=7)

        return d
