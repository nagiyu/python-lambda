docker build \
  --build-arg AWS_ACCESS_KEY_ID= \
  --build-arg AWS_SECRET_ACCESS_KEY= \
  --build-arg AWS_DEFAULT_REGION= \
  --build-arg S3_BUCKET_NAME= \
  -t python-lambda .