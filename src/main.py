from src.database.requests_db import ReqData
import asyncio
if __name__ == '__main__':
    req = ReqData()

    res = asyncio.run(req.get_services())

    print(res)