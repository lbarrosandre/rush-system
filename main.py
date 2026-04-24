from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

app = FastAPI()

SUPABASE_URL = "https://fxazgecbhcyenaorvoia.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ4YXpnZWNiaGN5ZW5hb3J2b2lhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NjkyNjMsImV4cCI6MjA5MjU0NTI2M30.Ytx4pUIrGZTE8WKNG73x_zUK4NdN1GmpL7tXPRKCduU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Login(BaseModel):
    email: str
    senha: str

@app.get("/")
def home():
    return {"msg": "Rush API online 🚀"}

@app.post("/login")
def login(data: Login):
    try:
        res = supabase.table("usuarios").select("*").eq("email", data.email).execute()

        if not res.data:
            return {"erro": "Usuário não encontrado"}

        user = res.data[0]

        if user["senha"] != data.senha:
            return {"erro": "Senha inválida"}

        return {"msg": "ok", "user": user}

    except Exception as e:
        return {"erro_real": str(e)}
