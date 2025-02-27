# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from multiprocessing import Process

def squared(x):
    print(x**2)

# create parallel processes
procs = [Process(target=squared, args=[x]) for x in range(10)]

# start all processes
for p in procs:
    p.start()

# wait for all tasks to finish
for p in procs:
    p.join()

