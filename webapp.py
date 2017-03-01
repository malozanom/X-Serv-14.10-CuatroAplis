#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que contiene la clase principal webApp.
"""

import socket


class app:
    """Application to which webApp dispatches. Does the real work

    Usually real applications inherit from this class, and redefine
    parse and process methods"""

    def parse(self, req, rest):
        """Parse the received request, extracting the relevant information.

        req:    HTTP request received from the client
        rest:   rest of the resource name after stripping the prefix
        """

        return None

    def process(self, parsedReq):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "Dumb application just saying 'It works!'"
                          "</h1></body></html>")


class webApp:
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def select(self, req):
        """Selects the application (in the app hierarchy) to run.

        Having into account the prefix of the resource obtained
        in the request, return the class in the app hierarchy to be
        invoked. If prefix is not found, return app class
        """

        resource = req.split(' ', 2)[1]
        for prefix in self.apps.keys():
            if resource.startswith(prefix):
                print("Running app for prefix: " + prefix +
                      ", rest of resource: " + resource[len(prefix):] + ".")
                return (self.apps[prefix], resource[len(prefix):])
        print("Running default app")
        return (self.myApp, resource)

    def __init__(self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()
        self.nums = []      # For the class suma

        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        try:
            while True:
                print('Waiting for connections')
                (recvSocket, address) = mySocket.accept()
                print('HTTP request received (going to parse and process):')
                req = recvSocket.recv(2048).decode('utf-8')
                if len(req) > 0:    # To avoid unexpected errors
                    print(req)
                    (theApp, rest) = self.select(req)

                    # We get the part with obj.
                    tokens = (str(theApp)).split('.')
                    # We separate obj from the rest.
                    tokens2 = (tokens[1]).split()
                    # We get the obj as str.
                    obj = tokens2[0]

                    parsedReq = theApp.parse(req, rest)
                    if obj == "suma":
                        (returnCode, htmlAnswer) = theApp.process(parsedReq,
                                                                  self.nums)
                        if len(self.nums) == 2:
                            self.nums.clear()
                    else:
                        (returnCode, htmlAnswer) = theApp.process(parsedReq)
                    print('Answering back...')
                    recvSocket.send(bytes("HTTP/1.1 " + returnCode +
                                          " \r\n\r\n" + htmlAnswer + "\r\n",
                                          'utf-8'))
                    recvSocket.close()
        except KeyboardInterrupt:
            print("Closing binded socket")
            mySocket.close()


if __name__ == "__main__":
    anApp = app()
    otherApp = app()
    testWebApp = webApp("localhost", 1234, {'/app': anApp,
                                            '/other': otherApp})
