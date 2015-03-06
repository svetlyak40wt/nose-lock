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

By default, lock is created as `/tmp/<cur-dir-name>.lock` file,
but you could override this behaviour using optional parameter
`--lock-file`:

    nosetests --with-lock --lock-file /tmp/blah-minor

Hack it
-------

Fork the project at [GitHub](https://github.com/svetlyak40wt/nose-lock). Don't forget
to send a pull request or file an issue.
