#!/bin/bash
sudo ip addr add 10.10.2.100/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 10.10.2.1

sudo stop network-manager
