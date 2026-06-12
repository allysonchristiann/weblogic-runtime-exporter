# put YOUR configuration here
WL_USER = '<WEBLOGIC_USER>'
WL_PASSWORD = '<WEBLOGIC_PASSWORD>'
WL_URL = 't3://<WEBLOGIC_HOST>:<PORT>'

connect(WL_USER, WL_PASSWORD, WL_URL)

serverRuntime()

# server
server_state = str(get('State'))

h = str(get('OverallHealthState'))
if 'State:' in h:
    server_health = h.split('State:')[1].split(',')[0]
else:
    server_health = h

# jvm
SERVER_NAME = '<SERVER_NAME>'

cd('JVMRuntime/' + SERVER_NAME)

jvm_uptime = str(get('Uptime'))
jvm_heap_free_percent = str(get('HeapFreePercent'))
jvm_heap_size_current = str(get('HeapSizeCurrent'))
jvm_heap_size_max = str(get('HeapSizeMax'))

# datasource
cd('../../JDBCServiceRuntime/' + SERVER_NAME + '/JDBCDataSourceRuntimeMBeans')

ds = cmo.getJDBCDataSourceRuntimeMBeans()[0]

datasource_state = str(ds.getState())
datasource_available = str(ds.getNumAvailable())
datasource_active = str(ds.getActiveConnectionsCurrentCount())
datasource_total = str(ds.getConnectionsTotalCount())
datasource_waiting = str(ds.getWaitingForConnectionCurrentCount())

# application status
application_status = "UNKNOWN"

try:
    cd('/ApplicationRuntimes')

    apps = cmo.getApplicationRuntimes()

    for app in apps:
        try:
            comps = app.getComponentRuntimes()

            for comp in comps:
                try:
                    application_status = str(comp.getStatus())
                    break
                except:
                    pass

            if application_status != "UNKNOWN":
                break

        except:
            pass

except:
    pass

serverRuntime()

# threadpool
cd('../../../../ThreadPoolRuntime/ThreadPoolRuntime')

threadpool_pending = str(get('PendingUserRequestCount'))
threadpool_hogging = str(get('HoggingThreadCount'))
threadpool_stuck = str(get('StuckThreadCount'))

# WORKMANAGERS
total_pending = 0
total_stuck = 0

try:

    cd('../../WorkManagerRuntimes')

    workmanagers = ls(returnMap='true')

    for wm in workmanagers.keys():

        try:

            cd(wm)

            try:
                total_pending += int(get('PendingRequests'))
            except:
                pass

            try:
                total_stuck += int(get('StuckThreadCount'))
            except:
                pass

            cd('..')

        except:

            try:
                cd('..')
            except:
                pass

except:
    pass

workmanager_pending = str(total_pending)
workmanager_stuck = str(total_stuck)

print('ZBX_RESULT={"server_state":"' + server_state +
      '","server_health":"' + server_health +
      '","application_status":"' + application_status +
      '","jvm_uptime":' + jvm_uptime +
      ',"jvm_heap_free_percent":' + jvm_heap_free_percent +
      ',"jvm_heap_size_current":' + jvm_heap_size_current +
      ',"jvm_heap_size_max":' + jvm_heap_size_max +
      ',"datasource_state":"' + datasource_state +
      '","datasource_available":' + datasource_available +
      ',"datasource_active":' + datasource_active +
      ',"datasource_total":' + datasource_total +
      ',"datasource_waiting":' + datasource_waiting +
      ',"threadpool_pending":' + threadpool_pending +
      ',"threadpool_hogging":' + threadpool_hogging +
      ',"threadpool_stuck":' + threadpool_stuck +
      ',"workmanager_pending":' + workmanager_pending +
      ',"workmanager_stuck":' + workmanager_stuck +
      '}')

disconnect()
exit()
