def app(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-Type', 'text/plain')]
	start_response(status, response_headers)
	data = environ['QUERY_STRING'].split('&')
	data = [item + "\r\n" for item in data]
	return data

