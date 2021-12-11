#!/bin/bash
cd /home/ec2-user/arquisoft
git pull
cd /home/ec2-user/
hostname=$(curl http://169.254.169.254/latest/meta-data/public-hostname) && \
curl -X POST http://ec2-3-219-151-84.compute-1.amazonaws.com:8001/upstreams/ManejadorOrdenes/targets --data target="$hostname:3000" && \
redis-server --daemonize yes && \
python3 /home/ec2-user/arquisoft/manejadorOrdenes/manage.py runserver 0.0.0.0:3000

sudo nano runserverordenes.sh
sudo chmod +x runserverordenes.sh
./runserverordenes.sh