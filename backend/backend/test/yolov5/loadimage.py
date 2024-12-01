import os
import yaml
from dotenv import load_dotenv

def update_dataset_yaml():
    # .env 파일 로드
    load_dotenv()

    # 환경 변수 가져오기
    base_dir = os.getenv("BASE_DIR", os.getcwd())
    images_subdir = os.getenv("IMAGES_SUBDIR")
    labels_subdir = os.getenv("LABELS_SUBDIR")

    # 절대 경로 생성
    images_dir = os.path.join(base_dir, images_subdir)
    labels_dir = os.path.join(base_dir, labels_subdir)

    # dataset.yaml 파일 경로
    dataset_yaml_path = os.path.join(base_dir, "dataset.yaml")

    # dataset.yaml 수정
    try:
        with open(dataset_yaml_path, "r") as file:
            dataset_config = yaml.safe_load(file)

        dataset_config["train"] = images_dir
        dataset_config["val"] = labels_dir

        with open(dataset_yaml_path, "w") as file:
            yaml.safe_dump(dataset_config, file, default_flow_style=False)

        print(f"Updated dataset.yaml: train={dataset_config['train']}, val={dataset_config['val']}")

    except FileNotFoundError:
        print(f"Error: {dataset_yaml_path} not found!")
    except Exception as e:
        print(f"An error occurred: {e}")