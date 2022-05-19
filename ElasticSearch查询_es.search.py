from elasticsearch import Elasticsearch

# 建立连接
es = Elasticsearch(["http://192.168.29.128:9200","http://192.168.29.131:9200","http://192.168.29.132:9200"],
                   sniff_on_start=True,
                   sniff_on_node_failure=True,
                   sniff_timeout=60)


# result = es.search(index='.ds-metricbeat-8.0.1-2022.03.08-000001',filter_path=['hits.total', 'hits.hits._source'])

# result = es.search(index='python3',filter_path=['hits.total', 'hits.hits._source'])

# result = es.search(index='python3')

body = {
  "query": {
    "match_all": {}
  }
}
result = es.search(index='python3', body= body,filter_path=['hits.total', 'hits.hits._source'], _source=['name'])
count = es.count(index='python3', body= body)
print(result)
print(count)
print(es.info())

