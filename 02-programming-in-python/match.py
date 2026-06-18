http_status = 200

match http_status:
    case 200:
        print("Success")
    case 300:
        print("Redirect")
    case 400:
        print("Client Error")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Http status")  # default
