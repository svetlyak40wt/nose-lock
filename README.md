Nose Lock
=========

[![changelog](http://allmychanges.com/p/python/nose-lock/badge/)](http://allmychanges.com/p/python/nose-lock/?utm_source=badge)

This is a plugin for python-nose which locks test execution
and doesn't allow to run them in parallel from two terminals. 

You could want this behaviour, when parallel tests will
interfer for some reason. This could be because they
go into one database or have other side effects which
hard to isolate.

Usage
-----

Install via `pip install nose-lock`, then run tests
with argument `--with-lock`.
