# v1/api.py
from flask import Blueprint
from .arxiv import arxiv_bp

api_bp = Blueprint("api_bp", __name__)

api_bp.register_blueprint(arxiv_bp, url_prefix="/arxiv")