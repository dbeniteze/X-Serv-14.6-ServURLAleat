#!/usr/bin/python3

import webapp
import random


class Aleat(webapp.webApp):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        direccion_aleat = random.randint(0, 10000000)
        html = ("<html><body><h1>Hello World!" +
                "</h1></body></html>" +
                '<a href=' + str(direccion_aleat) +
                '>Dame otra </a>' +
                "\r\n")
        return ("200 OK", html)

if __name__ == "__main__":
    ulrAleat = Aleat("localhost", 1234)
