from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI(debug=True)
class EmailRequest(BaseModel):
  email: EmailStr
  subject: str
  body: str

@app.get('/')
def root():
  return { 'ping': 'pong' }

@app.post('/sendmail')
def handleSendMail(email_request: EmailRequest):
  pass

