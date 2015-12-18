class Statuscode:
    def __init__(self, code, title, description):
        self.code = code
        self.title = title
        self.description = description

statuscodes = {
    200: Statuscode(200, "OK", "Everything was alright"),
    201: Statuscode(201, "ACCEPTED", "The request was accepted but is still processing"),
    404: Statuscode(404, "NOT FOUND", "The requested resource could not be found")
}
