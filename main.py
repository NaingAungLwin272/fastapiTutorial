from typing import Annotated, Optional, Union
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class BlogModel(BaseModel):
    title: str
    description: str
    published_at: Optional[bool]


@app.get("/blog")
def index(limit: int, published: bool):
    if published:
        return {"data": f"{limit} blog list from the database"}
    return {"data": "There is no data"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "blog lists for unpublished"}


@app.post("/blog/create")
def create_blog(request: BlogModel):
    return {"data": f"created {request.title} of blog"}


# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q}) # type: ignore
#     return results


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
