from . import router
from app.models import User
from uuid import uuid4
from fastapi import  status, HTTPException
from fastapi.responses import JSONResponse


@router.get('/user')
async def get_users():
    user = User.get()
    if user:
        return JSONResponse(
            status_code=200,
            content={
                'data':user,
                'message':'Success',
                'status':status.HTTP_200_OK
            }
        )
    return JSONResponse(
        status_code=200,
        content={
            'message':'No Content',
            'data':[],
            'status':204
        }
    )

@router.post('/user')
async def create_user():
    return user.dict()
