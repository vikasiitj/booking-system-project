#!/bin/bash
apt-get update
apt-get install -y docker.io
docker run -d -p 80:5000 gcr.io/ticketbookingsystem-g24ai1066/booking-app:latest
