#gunicorn configuration file for hello.py

CONFIG = {
   'mode': 'wsgi',
   'working_dir': '/home/box/web',
    #'python': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8080',
		'--workers=4',
        '--timeout=60',
		'--log-level=debug',
        'hello:app'
    )
}

#pythonpath='/home/box/web'
#bind='0.0.0.0:8080'
#workers=4
