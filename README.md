# How to installation
```shell
pip install cloud_watch_logs
```

# How to use
```python
import time
import cloud_watch_logs

cwl = cloud_watch_logs.CloudWatchLogs()
cwl.create_log_group(logGroupName="TestLogGroup")
cwl.create_log_stream(logGroupName="TestLogGroup", logStreamName="TestLogStream")

cwl.put_log_event(logGroupName="TestLogGroup", logStreamName="TestLogStream",
                  message="hello python")

cwl.put_log_event(logGroupName="TestLogGroup", logStreamName="TestLogStream",
                  timestamp=int(time.time() * 1000),
                  message="hello python")

cwl.put_log_events(logGroupName="TestLogGroup", logStreamName="TestLogStream", logEvents=[
    {"timestamp": int(time.time() * 1000), "message": "hello python1"},
    {"timestamp": int(time.time() * 1000), "message": "hello python2"},
])
```

# Implicit variable
### Implicit variable passing order
1. direct
2. environment
3. aws profile

### direct
```python
CloudWatchLogs(
    region_name='region_name',
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
)
```

### environment
```dotenv
aws.cloud_watch_logs.region_name=region_name
aws.cloud_watch_logs.aws_access_key_id=aws_access_key_id
aws.cloud_watch_logs.aws_secret_access_key=aws_secret_access_key
```

```python
CloudWatchLogs()
```

### aws profile
```python
CloudWatchLogs()
```

# Reference
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html
