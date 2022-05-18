from elasticsearch import Elasticsearch

# 连接单节点
# es = Elasticsearch(['http://192.168.29.128:9200'])

# 连接集群
es = Elasticsearch(["http://192.168.29.128:9200","http://192.168.29.131:9200","http://192.168.29.132:9200"],
                   sniff_on_start=True,
                   sniff_on_node_failure=True,
                   sniff_timeout=60)

es.index(index='python3',id=2,document={'name':'张开','age':18})

print(es.get(index='python3',id=1))

