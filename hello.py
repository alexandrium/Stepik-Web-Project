def app(environ, start_response):

    data = environ['QUERY_STRING'].encode()    

   # data = data.split(b'&')

    data = data.replace(b'&', b'\n')

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

#    return [data]
#    return iter(data)
