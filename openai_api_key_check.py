# from dotenv import load_dotenv
import os

# .env 파일 로드
# load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")

print(api_key)