class Statuscode:
    def __init__(self, code, title, description):
        self.code = code
        self.title = title
        self.description = description

statuscodes = {
    "100": Statuscode("100", "Continue", ""),
    "101": Statuscode("101", "Switching Protocols", ""),
    "200": Statuscode("200", "OK", ""),
    "201": Statuscode("201", "Created", ""),
    "202": Statuscode("202", "Accepted", ""),
    "203": Statuscode("203", "Non-Authoritative Information", ""),
    "204": Statuscode("204", "No Content", ""),
    "205": Statuscode("205", "Reset Content", ""),
    "206": Statuscode("206", "Partial Content", ""),
    "300": Statuscode("300", "Multiple Choices", ""),
    "301": Statuscode("301", "Moved Permanently", ""),
    "302": Statuscode("302", "Found", ""),
    "303": Statuscode("303", "See Other", ""),
    "304": Statuscode("304", "Not Modified", ""),
    "305": Statuscode("305", "Use Proxy", ""),
    "307": Statuscode("307", "Temporary Redirect", ""),
    "400": Statuscode("400", "Bad Request", ""),
    "401": Statuscode("401", "Unauthorized", ""),
    "402": Statuscode("402", "Payment Required", ""),
    "403": Statuscode("403", "Forbidden", ""),
    "404": Statuscode("404", "Not Found", ""),
    "405": Statuscode("405", "Method Not Allowed", ""),
    "406": Statuscode("406", "Not Acceptable", ""),
    "407": Statuscode("407", "Proxy Authentication Required", ""),
    "408": Statuscode("408", "Request Time-out", ""),
    "409": Statuscode("409", "Conflict", ""),
    "410": Statuscode("410", "Gone", ""),
    "411": Statuscode("411", "Length Required", ""),
    "412": Statuscode("412", "Precondition Failed", ""),
    "413": Statuscode("413", "Request Entity Too Large", ""),
    "414": Statuscode("414", "Request-URI Too Large", ""),
    "415": Statuscode("415", "Unsupported Media Type", ""),
    "416": Statuscode("416", "Requested range not satisfiable", ""),
    "417": Statuscode("417", "Expectation Failed", ""),
    "500": Statuscode("500", "Internal Server Error", ""),
    "501": Statuscode("501", "Not Implemented", ""),
    "502": Statuscode("502", "Bad Gateway", ""),
    "503": Statuscode("503", "Service Unavailable", ""),
    "504": Statuscode("504", "Gateway Time-out", ""),
    "505": Statuscode("505", "HTTP Version not supported", ""),
}
