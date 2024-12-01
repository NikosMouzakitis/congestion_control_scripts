#!/bin/bash
sudo ip addr add 10.10.1.1 dev eth0
sudo ip addr add 10.10.2.1 dev eth1
sudo ip link set eth0 up
sudo ip link set eth1 up
sudo sysctl -w net.ipv4.ip_forward=1
sudo sysctl -p
sudo ip route add 10.10.1.0/24 via 10.10.1.1 dev eth0
sudo ip route add 10.10.2.0/24 via 10.10.2.1 dev eth1

sudo stop network-manager


iface_0=$(ip route get 10.10.1.100 | grep -oP "(?<=dev )[^ ]+")
sudo tc qdisc del dev $iface_0 root
sudo tc qdisc add dev $iface_0 root handle 1: htb default 3
sudo tc class add dev $iface_0 parent 1: classid 1:3 htb rate 1Mbit
sudo tc qdisc add dev $iface_0 parent 1:3 handle 3: bfifo limit 0.1MB

echo "iface_0: "
echo $iface_0
echo "OK"

iface_1=$(ip route get 10.10.2.100 | grep -oP "(?<=dev )[^ ]+")
sudo tc qdisc del dev $iface_1 root
sudo tc qdisc add dev $iface_1 root handle 1: htb default 3
sudo tc class add dev $iface_1 parent 1: classid 1:3 htb rate 1Mbit
sudo tc qdisc add dev $iface_1 parent 1:3 handle 3: bfifo limit 0.1MB

echo "iface_1: "
echo $iface_1
echo "OK"


