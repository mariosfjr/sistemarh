from django import template

register = template.Library()

@register.filter
def endswith(value, suffix):
    """Verifica se a string termina com o sufixo especificado."""
    if isinstance(value, str):
        return value.lower().endswith(suffix.lower())
    return False
