sudo amazon-linux-extras install docker
sudo cat <<EOF >/etc/docker/daemon.json
{"hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"]}
EOF

sudo mkdir /etc/systemd/system/docker.service.d/
sudo cat <<EOF >/etc/systemd/system/docker.service.d/override.conf
 [Service]
 ExecStart=
 ExecStart=/usr/bin/dockerd
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker.service