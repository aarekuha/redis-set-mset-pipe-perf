#!/bin/sh

sleep 5

echo "yes" | redis-cli --cluster create \
  173.18.0.2:6379 \
  173.18.0.3:6379 \
  173.18.0.4:6379 \
  173.18.0.5:6379 \
  173.18.0.6:6379 \
  173.18.0.7:6379 \
  --cluster-replicas 1

echo "Redis cluster ready."