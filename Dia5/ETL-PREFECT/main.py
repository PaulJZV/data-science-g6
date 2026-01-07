from taskss.extract import extract
from taskss.transform import transform
from taskss.load import load
from prefect import flow

@flow
def main():
    data = extract()
    data_transform = transform(data)
    load(data_transform)
    
if __name__ == "__main__":
    main()