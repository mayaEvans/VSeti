from multiprocessing import cpu_count

name = 'djangoTask'
max_requests = 1024

worker_class = 'djangoTask.asgi.UvicornH11Worker'

bind = "0.0.0.0:8000"
workers = cpu_count() + 1

env = {
    'DJANGO_SETTINGS_MODULE': 'djangoTask.settings'
}
