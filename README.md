# Containerized Monitoring Stack (Prometheus + Grafana)

## Overview

This project implements a containerized monitoring stack using Docker, Prometheus, and Grafana to collect, store, and visualize system-level metrics. A custom Python-based metrics exporter is developed to expose real-time CPU, memory, and disk usage. Prometheus scrapes these metrics at regular intervals, and Grafana provides interactive dashboards and alerting capabilities. The project demonstrates core DevOps concepts including containerization, observability, monitoring pipelines, threshold-based alerting, and incident simulation.

## Architecture

```bash

System Metrics
      ↓
Python Exporter (Flask + psutil)
      ↓
Docker Container
      ↓
Prometheus (Metric Scraping)
      ↓
Grafana (Visualization & Alerting)

```

## Features

- Custom metrics exporter built using:

  1. Flask

  2. psutil

  3. prometheus_client

- Dockerized application deployment

- Prometheus scrape configuration

- Grafana dashboard with:

  1. CPU Usage (Time Series with thresholds)

  2. Memory Usage (Stat + Sparkline)

  3. Disk Usage (Gauge visualization)

- Threshold-based alerting for CPU utilization

- CPU stress testing for alert validation

- Configurable evaluation groups and alert logic

## Tech Stack

- Python 3

- Flask

- psutil

- Prometheus

- Grafana

- Docker

- Docker Compose

## Metrics Collected

The exporter exposes the following Prometheus-compatible metrics:

- system_cpu_usage_percent

- system_memory_usage_percent

- system_disk_usage_percent

Metrics are scraped every 5 seconds by Prometheus.

## Alerting Configuration

A CPU alert rule is configured with:

- Evaluation interval: 30 seconds

- Pending period: 1 minute

- Threshold: CPU > 70%

- Cooldown duration: 1 minute

This prevents false positives caused by temporary spikes and ensures stable alert behavior.

## Project Structure
```bash
containerized-monitoring-stack/
│
├── app/
│   ├── Dockerfile
│   ├── metrics.py
│   └── requirements.txt
│
├── prometheus/
│   └── prometheus.yml
│
├── docker-compose.yml
└── README.md
```
## Running the Project

- Start the monitoring stack:
  ```bash
     docker compose up --build
  ```
- Access the services:

  1. Prometheus → http://localhost:9090

  2. Grafana → http://localhost:3000

- Default Grafana credentials:
  ```bash
     Username: admin
     Password: admin
  ```

## DevOps Concepts Demonstrated

- Containerization using Docker

- Service orchestration using Docker Compose

- Observability and monitoring architecture

- Prometheus scrape targets configuration

- Grafana dashboard design

- Threshold-based alert rule configuration

- Controlled stress testing for validation

- Production-style alert evaluation behavior

## Use Case

This monitoring stack can be extended to:

- Monitor cloud-based services

- Observe container workloads

- Integrate with CI/CD pipelines

- Route alerts to Slack or email

- Track application-level metrics
