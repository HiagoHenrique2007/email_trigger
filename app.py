from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from utils.email_sender import sendMail

app = FastAPI(debug=True)
class EmailRequest(BaseModel):
  email: EmailStr
  subject: str
  body: str

@app.get('/')
def root():
  return { 'ping': 'pong' }

@app.post('/sendmail')
async def handleSendMail(email_request: EmailRequest):
  await sendMail(email=email_request.email, subject=email_request.subject, body=email_request.body)
  return { 'message': 'Email enviado!' }

