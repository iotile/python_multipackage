{# The :autogenerated: tag is picked up by breadcrumbs.html to suppress "Edit on Github" link #}
:autogenerated:

{{ fullname }} package
{% for item in range(8 + fullname|length) -%}={%- endfor %}

.. currentmodule:: {{ fullname }}

.. automodule:: {{ fullname }}
    {% if members -%}
    :members: {{ members|join(", ") }}
    :undoc-members:
    :show-inheritance:
    {%- endif -%}

{% if all_refs %}
Key Functions and Classes
-------------------------

.. autosummary::
    :nosignatures:

    {% for ref in all_refs -%}
    {% set ref_name1 = ref.split('<') -%}
    {% set ref_name2 = ref_name1[1].split('>') -%}
    ~{{ ref_name2[0] }}
    {% endfor -%}
{%- endif %}

{% if submodules %}
Submodules
----------

.. autosummary::
    :nosignatures:
    :toctree:
{% for item in submodules %}
    ~{{ fullname }}.{{ item }}
    {%- endfor %}
    {%- endif %}

{% if subpackages %}
Subpackages
-----------

.. autosummary::
    :nosignatures:
    :toctree:
{% for item in subpackages %}
    ~{{ fullname }}.{{ item }}
    {%- endfor %}
    {%- endif %}

{% if members %}
    Summary
    -------

    {%- if exceptions %}

    Exceptions:

    .. autosummary::
        :nosignatures:
{% for item in exceptions %}
        {{ item }}
{%- endfor %}
    {%- endif %}

    {%- if classes %}

    Classes:

    .. autosummary::
        :nosignatures:
{% for item in classes %}
        {{ item }}
{%- endfor %}
    {%- endif %}

    {%- if functions %}

    Functions:

    .. autosummary::
        :nosignatures:
{% for item in functions %}
        {{ item }}
{%- endfor %}
    {%- endif %}
{%- endif %}

    {%- if data %}

    Data:

    .. autosummary::
        :nosignatures:
{% for item in data %}
        {{ item }}
{%- endfor %}
    {%- endif %}


{% if members %}
    Reference
    ---------

{%- endif %}
