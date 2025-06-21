from typing import Literal, List, Dict, Any
from dataclasses import dataclass
from agents import function_tool


@dataclass
class UseCase:
    name: str
    includes: List[str]
    extends: List[str]

@dataclass
class RequirementModel:
    system_name: str
    roles: List[str]
    modules: List[Dict[str, Any]]
    usecases: List[UseCase]

@function_tool
def generate_use_case(name: str, includes: List[str], extends: List[str]) -> UseCase:
    return UseCase(name=name, includes=includes, extends=extends)

@function_tool
def generate_requirement_model(system_name: str, roles: List[str], modules: List[Dict[str, Any]], usecases: List[UseCase]) -> RequirementModel:
    return RequirementModel(system_name=system_name, roles=roles, modules=modules, usecases=usecases)