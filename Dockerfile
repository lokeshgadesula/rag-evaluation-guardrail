FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python","-m","rag_eval.cli","--dataset","data/sample.jsonl","--out","artifacts","--threshold","0.85"]
