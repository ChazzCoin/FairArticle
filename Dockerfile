
FROM python:3.8
ENV ACTIVATE_DATABASE=True
ENV ARTICLE_DATABASE_NAME='research'
ENV ARTICLE_DATABASE_HOST='sozindb.vaatu.co'
ENV ARTICLE_DATABASE_PORT='1214'
WORKDIR /jarticle_enhancer
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader vader_lexicon
COPY . .
CMD [ "python3", "lambda_enhancer.py" ]