from app.sales import Sales
from datetime import date


def main():

    date_range = [date.today(),
                  date(2020, 9, 1),
                  date(2020, 9, 6),
                  date(2020, 9, 13)]

    for d in date_range:
        s = Sales(d)

        output = f"Date: {d}| Is Sun: {s.is_sunday()} | Next Sun: {s.next_sunday()} | "
        output += f"Is 2nd: {s.is_second_sunday_of_month()} | "
        output += f"Next 2nd: {s.next_second_sunday()} "
        print(output)


if __name__ == "__main__":
    main()
