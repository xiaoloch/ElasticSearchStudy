query_body= {

  "query": {
    "bool": {
      "filter": [

        {"match_phrase":{
          "@enterpriseId": "27591"
        }},

        {"bool": {
          "should": [
          {
            "match_phrase": {
              "@result": 500
            }
          },
          {
            "match_phrase": {
              "@result": 501
            }
          },
          {
            "match_phrase": {
              "@result": 502
            }
          },
          {
            "match_phrase": {
              "@result": 503
            }
          },
          {
            "match_phrase": {
              "@result": 504
            }
          }
      ]}
        },
        {
            "range": {
              "@time": {
                "gte": "2022-05-01T16:00:00.000Z",
                "lte": "2022-05-06T15:59:59.999Z",
                "format": "strict_date_optional_time"
              }
            }
          }
      ]}},

  "_source": ["@appName","@result","@correlationId","@enterpriseId"],

  "size":10000

}
