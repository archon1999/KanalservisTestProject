Q_CLUSTER = {
    'name': 'project',
    'workers': 2,
    'recycle': 500,
    'timeout': 300,
    'retry': 300,
    'compress': True,
    'save_limit': 5000,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': 'redis://redis:6379',
}
