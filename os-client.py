from opensearchpy import OpenSearch
import json
import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("os-client")

host = 'localhost'
port = 9200
auth = ('admin', 'admin')

opensearch = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = False,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)

index_name = 'iqdm'


def create_index(index_name):
    response = opensearch.indices.create(index=index_name, ignore=400)
    logger.info(f'Creating index: {json.dumps(response, indent=2)}')

def add_document(index_name, document_name, id):
    with open(document_name) as f:
        document = json.load(f)
        
        response = opensearch.index(
            index = index_name,
            body = document,
            id = id,
            refresh = True
        )

        logger.info(f'Adding document: {json.dumps(response, indent=2)}')

def query_all_documents(index_name):
    response = opensearch.search(
        index = index_name,
        body = {
            'query': {
                'match_all': {}
            }
        }
    )

    logger.info(f'Search results: {json.dumps(response, indent=2)}')

def query_index(index_name, q):
    logging.info(f'Ececute query: {q}')

    query = {
     'query': {
        'multi_match': {
            'query': q,
            'fields': [],
            "fuzziness": "AUTO",
            "lenient": True,
            "operator": "or"
        }
      },
       "_source": {
        "exclude": ["captures", "annotations"]
      }
    }

    response = opensearch.search(
        body = query,
        index = index_name,
        pretty=True
    )

    logger.info(f'Search results: {json.dumps(response, indent=2)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OpenSearch client')
    parser.add_argument('--index', help='Index name')
    parser.add_argument('--query', help='Query string')
    parser.add_argument('--add', help='new index name')
    parser.add_argument('--all', help='Query all documents')
    args = parser.parse_args()

    if args.index:
        create_index(args.index)
        exit()

    if args.query:
        query_index(index_name, args.query)
        exit()

    if args.add:
        add_document(index_name, "example.sigmf-meta", args.add)
        exit()

    if args.all:
        query_all_documents(args.all)
        exit()

