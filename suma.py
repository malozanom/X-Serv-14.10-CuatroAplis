#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que realiza una suma en dos etapas
con un servidor orientado a objetos.
"""

import webapp


class suma(webapp.app):
    """Application that makes a sum in two stages."""

    def parse(self, req, rest):
        """Parse the received request, extracting the relevant information.

        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """

        return rest

    def process(self, parsedReq, nums):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        try:
            nums.append(int(parsedReq))
        except ValueError:
            return ("400 Bad Request", "<html><body><h1>No me has dado" +
                    " un entero. Vete.</h1></body></html>")

        if len(nums) == 1:
            return ("200 OK", "<html><body><h1>Me has dado un " +
                    str(nums[0]) + ". Dame mas.</h1></body></html>")
        else:
            result = nums[0] + nums[1]
            return ("200 OK", "<html><body><h1>Me habias dado un " +
                    str(nums[0]) + ". Ahora un " + str(nums[1]) +
                    ". Suman " + str(result) + "." + "</h1></body></html>")


if __name__ == "__main__":
    unaSuma = suma()
    testSuma = webapp.webApp('localhost', 1234, {'/suma/': unaSuma})
