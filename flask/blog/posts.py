from __future__ import annotations
from datetime import datetime
from blog.database import mongo



def get_all_posts(published: bool =True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    """
    /novidades-de-2024 
    """
    post = mongo.db.posts.find_one("slug": slug)
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    ...


def new_post(title: str, content: str, published: bool = True) -> str:
    # TODO : refatorar a criação do slug, removendo acentos
    slug = title.replace(" ", "-").replace("_", "-").lower()
    # TODO: Verificar o post com este slug já existe
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug