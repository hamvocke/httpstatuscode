class Statuscode:
    def __init__(self, code, description):
        self.code = code
        self.description = description

statuscodes = {
    200: Statuscode(200, "OK"),
    201: Statuscode(201, "ACCEPTED"),
    404: Statuscode(404, "NOT FOUND")
}
