from fastapi import FastAPI
from pydantic import BaseModel
import requests
from requests.auth import HTTPBasicAuth

app = FastAPI()


#uvicorn jenkins_trigger_api:app --host 0.0.0.0 --port 8000




# Nếu bạn muốn cho dev gửi tham số động, dùng model
class TriggerRequest(BaseModel):
    job_name: str
    trigger_token: str

@app.post("/trigger")
def trigger_build(data: TriggerRequest):
    jenkins_url = "https://4b37-222-254-34-167.ngrok-free.app"  # ngrok URL của bạn
    user = "truongvck33"
    api_token = "11ed703b1c4d8d1df2e75e631bca996d0"

    url = f"{jenkins_url}/job/{data.job_name}/build?token={data.trigger_token}"
    response = requests.post(url, auth=HTTPBasicAuth(user, api_token))

    if response.status_code == 201:
        return {"status": "✅ Build triggered thành công!"}
    else:
        return {"status": f"❌ Lỗi ({response.status_code}): {response.text}"}