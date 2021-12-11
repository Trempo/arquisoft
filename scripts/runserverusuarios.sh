#!/bin/bash
cd /home/ec2-user/arquisoft
git pull
cd /home/ec2-user/
hostname=$(curl http://169.254.169.254/latest/meta-data/public-hostname) && \
curl -X POST http://ec2-3-219-151-84.compute-1.amazonaws.com:8001/upstreams/ManejadorUsuarios/targets --data target="$hostname:3000"

sudo nano runservercomercio.sh
sudo chmod +x runservercomercio.sh
./runservercomercio.sh