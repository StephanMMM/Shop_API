FROM python:3.10
WORKDIR /Shop_API
COPY requirements.txt ./app/
RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt
COPY . .
EXPOSE 80
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]