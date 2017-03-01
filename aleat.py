#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que genera URLs aleatorias
con un servidor orientado a objetos.
"""

import webapp
import random


class aleat(webapp.app):
    "Application that generates random URLs."

    def process(self, parsedReq):
        rand = random.randrange(1000000000)
        return("200 OK", "<html><body><h1>Hola. <a href=http://localhost:" +
               "1234/aleat/" + str(rand) + ">Dame otra</a></h1></body></html>")


if __name__ == "__main__":
    urlaleat = aleat()
    testAleat = webapp.webApp('localhost', 1234, {'/aleat/': urlaleat})
