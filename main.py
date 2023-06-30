
import boto3

s3 = boto3.client('s3')
bucket = 'criadors2'

print("\nThe Created Buckets are : ")
buckets = s3.list_buckets()
for i in range(len(buckets['Buckets'])):
   print(buckets['Buckets'][i]['Name'])

create = s3.create_bucket(
   Bucket = bucket,
   CreateBucketConfiguration={
      'LocationConstraint': 'ap-south-1'
   },
   ObjectLockEnabledForBucket=False
)

print("\n" + bucket + " created...!")

s3.upload_file('Test1.txt', bucket, 'Test1saved.txt')

objects = s3.list_objects(
    Bucket = bucket
)

print("\nThe Uploaded objects in " + objects['Name'] + " are : ")
for i in range(len(objects['Contents'])):
   print(objects['Contents'][i]['Key'])

