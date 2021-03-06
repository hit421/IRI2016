#!/usr/bin/env python
""" Time Profile: IRI2016 """
from datetime import timedelta
from argparse import ArgumentParser
import iri2016 as iri
from matplotlib.pyplot import show
import iri2016.plots as piri


def main():
    p = ArgumentParser()
    p.add_argument('latlon', help='geodetic latitude, longitude (degrees)',
                   type=float, nargs=2)
    p.add_argument('-alt_km', help='altitude START STOP STEP (km)',
                   type=float, nargs=3, default=(100, 200, 20))
    P = p.parse_args()

    sim = iri.timeprofile(('2012-08-21', '2012-08-22'), timedelta(hours=1.0),
                          P.alt_km, *P.latlon)

    piri.timeprofile(sim)
    show()


if __name__ == '__main__':
    main()
