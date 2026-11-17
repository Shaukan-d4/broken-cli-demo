FROM python:3.10-slim
WORKDIR /app
COPY dist/*.whl .
RUN pip install --no-cache-dir *.whl
CMD ["mycli"]


