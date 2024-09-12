# Backup dynamoDB

## Crear backup
```java
aws dynamodb create-backup --table-name <table-name> --backup-name <backup-name>
```

## Listar backups
```java
aws dynamodb list-backups
```

example
```java
aws dynamodb list-backups
{
    "BackupSummaries": [
        {
            "TableName": "Feature-jy66hzva7bbmdknjk3umkrw5uq-dev",
            "TableId": "47a2f8ca-40c3-4c15-83d6-165c787679f2",
            "TableArn": "arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev",
            "BackupArn": "arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af",
            "BackupName": "Test-backup",
            "BackupCreationDateTime": 1724417358.298,
            "BackupStatus": "AVAILABLE",
            "BackupType": "USER",
            "BackupSizeBytes": 468
        }
    ]
}

```

## Describe de backup en específico
```java
aws dynamodb describe-backup \
--backup-arn arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af
```

example
```java
aws dynamodb describe-backup \                                    
--backup-arn arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af
{
    "BackupDescription": {
        "BackupDetails": {
            "BackupArn": "arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af",
            "BackupName": "Test-backup",
            "BackupSizeBytes": 468,
            "BackupStatus": "AVAILABLE",
            "BackupType": "USER",
            "BackupCreationDateTime": 1724417358.298
        },
        "SourceTableDetails": {
            "TableName": "Feature-jy66hzva7bbmdknjk3umkrw5uq-dev",
            "TableId": "47a2f8ca-40c3-4c15-83d6-165c787679f2",
            "TableArn": "arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev",
            "TableSizeBytes": 468,
            "KeySchema": [
                {
                    "AttributeName": "id",
                    "KeyType": "HASH"
                }
            ],
            "TableCreationDateTime": 1694805727.905,
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 0,
                "WriteCapacityUnits": 0
            },
            "ItemCount": 3,
            "BillingMode": "PAY_PER_REQUEST"
        },
        "SourceTableFeatureDetails": {
            "StreamDescription": {
                "StreamEnabled": true,
                "StreamViewType": "NEW_AND_OLD_IMAGES"
            }
        }
    }
}

```

## Hacer recuperación desde un backup
```
aws dynamodb restore-table-from-backup \
    --target-table-name Feature-jy66hzva7bbmdknjk3umkrw5uq-dev \
    --backup-arn arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af
```

> [!info]
> No se puede hacer la recuperación a una tabla que ya existe (el comando anterior da error)

```
aws dynamodb restore-table-from-backup \
    --target-table-name Feature-jy66hzva7bbmdknjk3umkrw5uq-dev \
    --backup-arn arn:aws:dynamodb:us-east-1:036134507423:table/Feature-jy66hzva7bbmdknjk3umkrw5uq-dev/backup/01724417358298-1bb271af

An error occurred (TableAlreadyExistsException) when calling the RestoreTableFromBackup operation: Table already exists: Feature-jy66hzva7bbmdknjk3umkrw5uq-dev
```



# PITR

Cost: 
- $ 0.20 per GB stored.

>[!note]
>If you're starting with 10GB and adding 1GB every day, you would calculate the sum of data stored each day throughout the month.
>
>Day 1: 10GB Day 2: 11GB Day 3: 12GB … Day 30: 39GB The total sum of these amounts is 735GB for the month.
>
>The cost for continuous backups in DynamoDB is $0.20 per GB-month. So, multiply the total GB stored by the cost per GB-month:
>
>735 GB * $0.20 per GB-month = $147.00



## Habilitar PITR dede  la consola
![[Pasted image 20240902102652.png]]
![[Pasted image 20240902102712.png]]
## habilitar PITR con AWS CLI
```
aws dynamodb update-continuous-backups \
--region us-east-1 \
--table-name <ddb-table-name> \
--point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
```

