Nose Lock
=========

This is a plugin for python-nose which locks test execution
and doesn't allow to run them in parallel from two terminals. 

You could want this behaviour, when parallel tests will
interfer for some reason. This could be because they
go into one database or have other side effects which
hard to isolate.
