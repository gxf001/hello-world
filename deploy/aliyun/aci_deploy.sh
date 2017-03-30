#!/bin/bash
set -e

# WORK_DIR must be code root dir
export WORK_DIR=${WORK_DIR:=$PWD}
export ENV=${ENV:="int"}
echo "WORK_DIR: $WORK_DIR, ENV: $ENV"

deploy_dir="${WORK_DIR}/deploy/aliyun"
. ${deploy_dir}/env-${ENV}.env

echo "build image..."
docker build -t ${IMAGE_URL} .

echo "docker login..."
export ACR_USER="LaplaceAI"
export ACR_KEY="laplace@2023"
docker login ${ACR_SERVER} -u ${ACR_USER} -p ${ACR_KEY}

echo "push image..."
docker push ${IMAGE_URL}

