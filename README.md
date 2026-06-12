# WebLogic Runtime Exporter

WebLogic runtime metrics collection for Zabbix using WLST (Jython), Oracle MBeans and JSON output.

## Overview

This project collects runtime information directly from Oracle WebLogic MBeans and exports the results in JSON format for Zabbix monitoring.

The exporter was designed to provide visibility into:

- Server health
- JVM metrics
- Datasource metrics
- Application status
- ThreadPool metrics
- WorkManager metrics

## Architecture

WebLogic Server
      |
      v
WLST Script
      |
      v
JSON Output
      |
      v
Zabbix Agent
      |
      v
Zabbix Server

## Collected Metrics

### JVM

- HeapFreePercent
- HeapSizeCurrent
- HeapSizeMax
- Uptime

### Datasource

- State
- Available Connections
- Active Connections
- Total Connections
- Waiting Connections

### ThreadPool

- Pending Requests
- Hogging Threads
- Stuck Threads

### WorkManager

- Pending Requests
- Stuck Threads

### Applications

- Deployment Status

## Example Output

```json
{
  "server_state": "RUNNING",
  "server_health": "HEALTH_OK",
  "application_status": "STATE_ACTIVE",
  "jvm_heap_free_percent": 47,
  "threadpool_stuck": 0
}
```

## Technologies

- Oracle WebLogic
- WLST
- Jython
- Zabbix
- JSON
