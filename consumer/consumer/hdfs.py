import pyhdfs


def write_parquet_file(parquet_data, file_num):
    hdfs = pyhdfs.HdfsClient(hosts="84.252.132.150:9870")
    hdfs.create(f'/user/hive/warehouse/kv/file{file_num}.parquet', parquet_data)
    print(hdfs.listdir(f'/user/hive/warehouse/kv'))
