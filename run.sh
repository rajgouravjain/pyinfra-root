#!/bin/bash

pyinfra inventories/test_instance.py exec -- hostname

py.test --hosts='docker://test_instance' tests/integration/testinfra/
