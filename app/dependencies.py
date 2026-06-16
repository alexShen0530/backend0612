from fastapi import Path, Query
async def common_params(
        skip: int,
        limit: int
):
    return {"skip": skip, "limit": limit}
