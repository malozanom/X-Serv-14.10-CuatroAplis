#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que devuelve una página HTML con el texto Hola o Adios (dependiendo
el recurso) con un servidor orientado a objetos.
"""

import webapp


class saludo(webapp.app):
    """Application that returns an HTML page with the text "Hola" when
    resources that start with /hola are invoked."""

    def process(self, parsedReq):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>Hola</h1></body></html>")


class despedida(webapp.app):
    """Application that returns an HTML page with the text "Adios" when
    resources that start with /adios are invoked."""

    def process(self, parsedReq):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>Adios</h1></body></html>")


if __name__ == "__main__":
    unHola = saludo()
    unAdios = despedida()
    testHola = webapp.webApp("localhost", 1234, {'/hola': unHola,
                                                 '/adios': unAdios})
