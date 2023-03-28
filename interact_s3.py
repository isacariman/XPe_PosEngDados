import boto3
import pandas as pd

#Criando um cliente para interagir com AWS S3
s3 = boto3.client('s3')

s3.download_file("datalake-isabellecariman-944460547625",
                        "raw-data/ITENS_PROVA_2020.csv",
                        "data/ITENS_PROVA_2020.csv")                                          

df = pd.read_csv("data/ITENS_PROVA_2020.csv")
print(df)

