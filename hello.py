def app(env, start_response):
  status = '200 ok' 
  headers = [('Content-Type', 'text/plain')]
  query_vars = env['QUERY_STRING'].split("&")
  data = ""
  for var in query_vars:
    data += var + '\n' 
  start_response(status, headers)
  return [data.encode('utf-8')]
