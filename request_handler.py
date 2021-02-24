import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from locations.request import create_location
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal, get_animals_by_location, get_animals_by_status
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee, get_employee_by_location
from customers import get_all_customers, get_single_customer, delete_customer, update_customer, get_customer_by_email

class HandleRequests(BaseHTTPRequestHandler):

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:

            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return ( resource, key, value )

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                else:
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers()}"
            elif resource == "employees":
                if id is not None:
                    response = f"{get_single_employee(id)}"
                else:
                    response = f"{get_all_employees()}"
            elif resource == "locations":
                if id is not None:
                    response = f"{get_single_location(id)}"
                else:
                    response = f"{get_all_locations()}"

        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            if key == "email" and resource == "customers":
                response = get_customer_by_email(value)
            if key == "location_id" and resource == "animals":
                response = get_animals_by_location(value)
            if key == "location_id" and resource == "employees":
                response = get_employee_by_location(value)
            if key == "status" and resource == "animals":
                response = get_animals_by_status(value)

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_resource = None

        if resource == "animals":
            new_resource = create_animal(post_body)

        if resource == "locations":
            new_resource = create_location(post_body)

        if resource == "employees":
            new_resource = create_employee(post_body)

        self.wfile.write(f"{new_resource}".encode())

    def do_DELETE(self):

        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "animals":
            success = delete_animal(id)
        if resource == "locations":
            success = delete_location(id)
        if resource == "employees":
            success = delete_employee(id)
        if resource == "customers":
            success = delete_customer(id)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            update_animal(id, post_body)

        if resource == "locations":
            update_location(id, post_body)

        if resource == "customers":
            update_customer(id, post_body)

        if resource == "employees":
            update_employee(id, post_body)

        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()