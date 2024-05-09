from queue import Queue


class Request:
    # Унікальний ідентифікатор заявок
    request_id_counter = 1

    def __init__(self, data):
        self.id = Request.request_id_counter
        Request.request_id_counter += 1
        self.data = data

    def __str__(self):
        return f"Заявка {self.id}: {self.data}"


class Line:
    def __init__(self):
        self.requests = Queue()

    def generate_request(self, request):
        self.requests.put(request)
        print(f"Нова заявка: {request}")

    def process_request(self):
        while not self.requests.empty():
            processed_request = self.requests.get()
            print(f"Обробка заявки: {processed_request}")
        else:
            print("Черга порожня")


# Черга
line = Line()

for i in range(5):
    line.generate_request(Request(f"Заявка - {i}"))

line.process_request()
