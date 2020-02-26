import json
import csv
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        requestPath = self.path

        #Log to us
        print(f'\n----- GET Request Start ----->\n')
        print(f'Request path: {requestPath}')
        print(f'Request headers:\n')
        for line in self.headers:
            print(f'  > {line}: {self.headers[line]}')
        print(f'\n<----- GET Request End -----\n')

        #Answer 200 => OK Status
        self.send_response(200)

        #Add Headers if any needed
        #self.send_header("Set-Cookie", "cate=true")
        self.end_headers()

        #Body of reply
        tablenumber = 0
        table = []
        linenumber = 0
        students = []
        with open('FDTables.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                linenumber += 1
                if 'W' in row[1]:
                    student = {
                    'name' : row[0].replace('|', ''),
                    'table' : row[1].replace('|','').replace('W', ''),
                    "waiter" : "Yes"
                    }
                else:
                    student = {
                    'name' : row[0].replace('|', ''),
                    'table' : row[1].replace('|','').replace('W', ''),
                    'waiter' : 'No'
                    }
                students.append(student)
        seating = {"students" : students}
        json_reply = json.dumps(seating)
        self.wfile.write(json_reply.encode(encoding='utf_8'))



# Listen on Port 80
port = 80
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
server.serve_forever()





                ##table.append(row[0].replace('|', ''))
                ##if linenumber % 8 == 0 or (row[1].replace('|', '') == 'kitchen' and (linenumber - 7) % 8 == 0):
                    ##json_reply = json.dumps({'table': row[1].replace('|', '').replace('W', ''), 'students': table})
                ##    table = []
                ##    self.wfile.write(json_reply.encode(encoding='utf_8'))
                ##linenumber += 1
