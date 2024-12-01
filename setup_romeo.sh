#!/bin/bash
sudo ip addr add 10.10.1.100/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 10.10.1.1

sudo sysctl -w net.ipv4.tcp_no_metrics_save=1

sudo stop network-manager
