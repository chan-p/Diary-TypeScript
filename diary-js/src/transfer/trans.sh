bq extract --destination_format=AVRO hayashi_private.daily_info2 gs://hayashi-private/info.avro
gsutil cp gs://hayashi-private/info.avro ./
