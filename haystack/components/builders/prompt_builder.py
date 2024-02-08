from typing import Dict, Any

from haystack import component, default_to_dict
from haystack.components.builders.jinja2_builder import Jinja2Builder


@component
class PromptBuilder:
    """
    PromptBuilder is a component that renders a prompt from a template string using Jinja2 engine.
    The template variables found in the template string are used as input types for the component and are all required.

    Usage:
    ```python
    template = "Translate the following context to {{ target_language }}. Context: {{ snippet }}; Translation:"
    builder = PromptBuilder(template=template)
    builder.run(target_language="spanish", snippet="I can't speak spanish.")
    ```
    """

    def __init__(self, template: str):
        """
        Initialize the component with a template string.

        :param template: Jinja2 template string, e.g. "Summarize this document: {documents}\\nSummary:"
        :type template: str
        """
        self.builder = Jinja2Builder(template=template)

    def to_dict(self) -> Dict[str, Any]:
        return default_to_dict(self, template=self.builder._template_string)

    @component.output_types(prompt=str)
    def run(self, **kwargs):
        return {"prompt": self.builder.run(**kwargs)["string"]}
