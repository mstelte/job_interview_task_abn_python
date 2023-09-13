# job_interview_task_abn_python

This repository contains a simple software as part of a programming assignment for an ABN Amro job application.

The program client_data_collector.py reads client data from two different files, one containing address details and the other containing banking details. It creates a new file containing the following user data:

* Client Identifier
* E-Mail Address
* Country
* Bitcoin Address
* Credit Card Type

The clients can be filtered by country when executing the program.

The program can also be run in a flask server in the root directory. The parameters then have to be passed as /cdc/<file1>/<file2>/<countries>. The countries need to use '_' instead of ' ' and need to be separated by a comma ','.