from .BaseDataModel import BaseDataModel
from .db_schemes import Project

class ProjectModel(BaseDataModel):

    def __init__(self, db_client):
        super().__init__(db_client)
        