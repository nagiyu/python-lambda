import os
from app.screenshot_to_s3 import save_url_screenshot_to_s3

def test_save_url_screenshot_to_s3():
    # テスト用のURL（例: Googleトップページ）
    url = "https://www.google.com"
    s3_url = save_url_screenshot_to_s3(url)
    print("S3 URL:", s3_url)
    assert s3_url.startswith("https://")
    assert os.environ["S3_BUCKET_NAME"] in s3_url

if __name__ == "__main__":
    test_save_url_screenshot_to_s3()
    print("save_url_screenshot_to_s3() test passed.")
