#!/usr/bin/env bash

# docker run -e ACTIVATE_DATABASE=True -e ARTICLE_DATABASE_NAME='research' -e ARTICLE_DATABASE_HOST='192.168.1.180' -e ARTICLE_DATABASE_PORT='27017' chazzcoin/microcrawler:beta
# --tag chazzcoin/hark-api:latest
docker buildx build --push --platform linux/arm64,linux/amd64 --tag chazzcoin/jarticle_enhancer:stage .