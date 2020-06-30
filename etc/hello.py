def app(environ, start_response):
    """Simplest possible application object"""

#    try:
#        request_body_size = int(environ.get('CONTENT_LENGTH',0))
#    except (ValueError):
#        request_body_size = 0

    # data = bytearray(request_body_size) 
    # data = str(environ['wsgi.input']).encode()
    
#    request_body = environ['wsgi.input'].read(request_body_size)
#    data = request_body

    data = environ['QUERY_STRING'].encode()    
#    data = data.split(b'&')
    data = data.replace(b'&',b'\n')

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
#    return [data]
#    return iter(data)
