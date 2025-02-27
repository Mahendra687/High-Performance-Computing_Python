<!--
SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>

SPDX-License-Identifier: CC-BY-NC-SA-4.0
-->

## Interfacing with C

### Using cffi

The files `evolve.h` and `evolve.c` contain a pure C implementation of the
single time step in heat equation. The C implemention can be built into a
shared library with the provided [Makefile](Makefile) by executing `make`
command. Use **cffi** for utilizing the library function instead of the Python
function in [heat.py](heat.py). Compare the performance to
Cython implementation.

