# WebLogic Runtime Exporter

Coletor de métricas runtime para Oracle WebLogic utilizando WLST (Jython) e integração com Zabbix.

## Objetivo

Disponibilizar métricas internas do WebLogic que não estão presentes nos templates padrão do Zabbix, permitindo monitoramento de:

- JVM
- Datasources
- Aplicações
- Thread Pools
- Work Managers
- Health State do servidor

## Fluxo de Coleta

WebLogic Runtime
    ↓
WLST (Jython)
    ↓
Oracle MBeans
    ↓
JSON
    ↓
Zabbix Agent
    ↓
Zabbix Server

## Métricas Coletadas

### Servidor

- State
- OverallHealthState

### JVM

- HeapFreePercent
- HeapSizeCurrent
- HeapSizeMax
- Uptime

### Datasource

- State
- NumAvailable
- ActiveConnectionsCurrentCount
- ConnectionsTotalCount
- WaitingForConnectionCurrentCount

### Thread Pool

- PendingUserRequestCount
- HoggingThreadCount
- StuckThreadCount

### Work Managers

- PendingRequests
- StuckThreadCount

### Aplicações

- Component Status

## Exemplo de Saída

```json
{
  "server_state":"RUNNING",
  "server_health":"HEALTH_OK",
  "application_status":"STATE_ACTIVE",
  "jvm_heap_free_percent":47,
  "datasource_active":5,
  "threadpool_stuck":0,
  "workmanager_pending":0
}
