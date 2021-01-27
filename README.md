# Socket-Programming Networking
This program creates a socket and bind it to a specific address and port as well as send and receive HTTP packet.
Web server:
1.) Accepts and parse the HTTP request.
2.) Retrieves requested file from server's file system.
3.) Creates an HTTP response message that consists of the requested file preceded by header lines.
4.) Sends the response directly to the client
Responses can consist of ether the file found or an HTTP 404 "Not Found" message\
Security is built into the web server that will not allow its clients to access "/grades/students.html" or any file in "/grades/" folder
This will respond with a HTTP 403 "Forbidden" response\
Examples are shown on Wiki Page

