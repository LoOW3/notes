import boto3

aws_access_key_id = input("access_key_ID: ")
aws_secret_access_key = input("secret_access_key: ")
bucket_name = input("bucket_name: ")

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)
s3 = session.client('s3')
id_main_folder = input("id_main_folder: ")

folders = [
    f'{id_main_folder}/',
    f'{id_main_folder}/folder_1/',
    f'{id_main_folder}/folder_2/',
    f'{id_main_folder}/folder_2/sub_folder_1/',
    f'{id_main_folder}/folder_2/sub_folder_2/',
    f'{id_main_folder}/folder_3/',
    f'{id_main_folder}/folder_4/',
    f'{id_main_folder}/folder_5/',
    f'{id_main_folder}/folder_6/'
]

for folder in folders:
    s3.put_object(Bucket=bucket_name, Key=folder)

print("listo rey")
