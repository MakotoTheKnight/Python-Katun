# -*- coding: utf-8 -*-
import models

def init_db():

    models.Base.metadata.create_all()

init_db()