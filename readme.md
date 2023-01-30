# Mongo-opensearch-connector
This project syncs mongodb and opensearch by using monstache. The monstache prototype script denormalizes the collection document and joins it with the sigmf documents.

## Steps to test

1. Add sigmf document
```console 
python mongo-client.py --add "exampleA.sigmf-meta"
```

Remeber the uuids of the inserted sigfm documents

2. Add collection document
```console 
python mongo-client.py --addC "UUID"
```

3. Add sigmf document
```console 
python mongo-client.py --add "exampleB.sigmf-meta"
```

Remeber the uuids of the inserted sigfm documents

4. Add collection document
```console 
python mongo-client.py --addC "UUID"
```

5. Query Opensearch to see the joined document
```console 
python os-client.py --all "iqdm"
```

6. Execute full-text search query
```console
python os-client.py --query "matlab"
```
