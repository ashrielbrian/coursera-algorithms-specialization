# python3
from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def Process(self, request):
        
        if self.finish_time:
            last_finish_time = self.finish_time[-1]
            ## the request's finish (and start) times IF it is to be processed
            if request.arrival_time > last_finish_time:
                new_finish_time = request.arrival_time + request.process_time
                new_start_time = request.arrival_time
            else:
                new_finish_time = last_finish_time + request.process_time
                new_start_time = last_finish_time

            ## Remove from self.finish_time packets that have finished processing by the time
            ## the new packet arrives
            keepPopping = True
            while keepPopping:
                if self.finish_time:
                    current_finish_time = self.finish_time.popleft()
                    if current_finish_time > request.arrival_time:
                        self.finish_time.appendleft(current_finish_time)
                        keepPopping = False
                else:
                    keepPopping = False
            
            if len(self.finish_time) < self.size:
                # there is sufficient space in the buffer to add another packet
                self.finish_time.append(new_finish_time)
                return Response(False, new_start_time)
            else:
                # insufficient space in the buffer - drop the packet
                return Response(True, -1)
        else:
            # the queue is empty
            self.finish_time.append(request.process_time)
            return Response(False, request.arrival_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)

