from pydantic import BaseModel

from summer.models.camel.str_to_camel_case import str_to_camel_case


def alias_generator_f(name: str) -> str:
    return str_to_camel_case(name)


class CamelModel(BaseModel):
    class Config:
        alias_generator = alias_generator_f
        allow_population_by_field_name = True
