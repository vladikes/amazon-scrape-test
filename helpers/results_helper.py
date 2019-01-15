import csv


class ResultHelper:

    def __init__(self, titles=None, dates=None, authors=None,
                 prices=None, stars=None, reviews=None, rows=None):

        self.titles = titles
        self.dates = dates
        self.authors = authors
        self.prices = prices
        self.stars = stars
        self.reviews = reviews
        self.rows = rows

    @classmethod
    def set_results(cls, titles, dates, authors,
                    prices, stars, reviews):
        rows = zip(titles, dates, authors,
                   prices, stars, reviews)
        cls.rows = rows

    @classmethod
    def write_to_csv(cls):
        with open('results.csv', "a") as f:
            writer = csv.writer(f)
            for row in cls.rows:
                writer.writerow(row)