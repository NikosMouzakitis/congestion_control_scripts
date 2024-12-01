#!/bin/bash

iperf3 -c 10.10.2.100 -P 3 -t 60 -C reno
