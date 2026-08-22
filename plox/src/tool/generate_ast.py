class GenerateAst:
    output_dir: str
    base_name: str
    types: list[str]

    def __init__(self, output_dir: str, base_name: str, types: list[str]):
        self.utput_dir = output_dir
        self.base_name = base_name
        self.types = types

        with open(output_dir, "w", encoding="utf-8") as file:
            file.write("from abc import ABC, abstractmethod\n")
            file.write("")
            file.write("")
            file.write("class Expr")
            # TODO: What should be the output?
