#!/bin/bash
# Simulate a motion event from a trusted IP

curl -X POST http://localhost:5000/motion \
  -H "Content-Type: application/json" \
  -d '{
    "camera": "test_cam",
    "event": "motion_detected",
    "timestamp": "'$(date -u +"%Y-%m-%dT%H:%M:%SZ")'"
  }'
