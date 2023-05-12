import os
import uvicorn
from fastapi import FastAPI
import calendar_routes
import front_routes


app = FastAPI()
app.include_router(calendar_routes.router)
app.include_router(front_routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
