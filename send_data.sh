#!/bin/sh
attempts=$(journalctl _SYSTEMD_UNIT=sshd.service | egrep -o "sshd\[[0-9]*\]: (Failure|Accepted|Invalid)" | wc -l)
node_hostname=$(hostname)
echo $attempts
echo $node_hostname
curl -i -H "Content-Type: application/json" -X POST -d "{\"node_hostname\":\"$node_hostname\", \"ssh_attempts\":\"$attempts\"}" http://172.31.95.42:5000