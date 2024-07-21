from werkzeug.serving import run_simple

run_simple('localhost',9000,app,use_reloader=False, use_debugger=False)
