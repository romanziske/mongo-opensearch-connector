import json
import argparse
import logging
from bson import ObjectId
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mongo-client")

mongo_client = MongoClient("mongodb://admin:admin@localhost:27017")
logger.info("Connecting to MongoDB...")

db = mongo_client['iqdm']
sigmf_collection = db['sigmf']
collection_collection = db['collection']

def add_document(file_name):
    logger.info(f'Adding document: {file_name}')
    with open(file_name) as f:
        document = json.load(f)
        result = sigmf_collection.insert_one(document)
        logger.info(f'Added document: {result.inserted_id}')

def update_document(id):
    result = sigmf_collection.update_one({'_id': ObjectId(id)},  {'$set': {"global.core:updated": "Updated..."}}) 
    logger.info(f'Updated documents: {result.modified_count}')

def add_collection_document(datasets):
    with open("collection.json") as f:
        document = json.load(f)
        datasetList = []
        for dataset in datasets:  
            datasetList.append( ObjectId(dataset))

        document['datasets'] = datasetList
        result = collection_collection.insert_one(document)
        logger.info(f'Added document: {result.inserted_id}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MongoDB client')
    parser.add_argument('--add', help='File name')
    parser.add_argument('--update', help='ID')
    parser.add_argument('--addC', action='append')
    args = parser.parse_args()

    if args.add:
        add_document(args.add)

    if args.addC:
        add_collection_document(args.addC)

    if args.update:
        update_document(args.update)
