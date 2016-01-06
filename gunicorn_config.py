import multiprocessing


worker_class = 'eventlet'
workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1000
