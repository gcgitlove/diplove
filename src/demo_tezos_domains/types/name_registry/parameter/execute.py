# generated by datamodel-codegen:
#   filename:  execute.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class ExecuteParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    action_name: str
    payload: str
    original_sender: str
