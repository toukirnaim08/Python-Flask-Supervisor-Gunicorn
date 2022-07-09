# Python-Flask-Supervisor-Gunicorn

Supervisor is a monitoring tool which controls various child processes and handles starting/restarting of these child processes when they exit abruptly or exit due to some reasons.

In this project, I will demonstrate how to set up Supervisor to work with our application. For this, I will create a simple application in Flask along with Gunicorn to act as our WSGI HTTP server.

I assume that you have a basic understanding of Flask, Gunicorn and environment setup using virtualenv while developing a Python application.

Run gunicorn command
```bash
gunicorn -w 1 -b 127.0.0.1:5000 autoapp:app
```

or supervisord command using supervisord.config file
```bash
sudo cp supervisord.conf /etc/supervisord.conf
supervisord
```

or you can run the load_supervisord.sh bash file directly

open swagger on http://127.0.0.1:5000/


