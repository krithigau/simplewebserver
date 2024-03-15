from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<body>
<table border="2" cellspacing="5" cellpadding="5" width="500" height="500">
     <caption>Revenue Ranking of Top 10 Software Companies</caption>
         <tr>
             <th bgcolor="sky blue">Rank</th>
             <th bgcolor="sky blue">Company</th>
             <th bgcolor="sky blue">Revenue(in $000s)</th>
         </tr>
         <tr>
             <td>1</td>
             <td>Apple</td>
             <td>1859</td>
         </tr>
         <tr>
             <td>2</td>
             <td>Facebook</td>
             <td>1621</td> 
         </tr>
         <tr>
             <td>3</td>
             <td>Alphabet</td>
             <td>1253</td>
         </tr>
         <tr>
             <td>4</td>
             <td>VeriSign</td>
             <td>1154</td>
         </tr>
         <tr>
             <td>5</td>
             <td>Visa</td>
             <td>1062</td>
         </tr>
          
     </table>
     </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()