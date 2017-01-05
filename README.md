Signal-triggered process reloader
=================================

Pyexec allows to setup signal handler, which will reload current process. This
functionality might be used to restart application, e.g. when the code's been
changed, by sending an appropriate signal to the python process.
