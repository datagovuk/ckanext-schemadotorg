# ckanext-schemadotorg

A simple CKAN extension for rendering organizations and datasets in a format that schema.org likes.

## Installation (for development)

* Go to the src folder of your CKAN installation 

```
git clone git@bitbucket.org:leedsdatamill/ckanext-schemadotorg.git
cd ckanext-schemadotorg
python setup.py develop
```

* Add ```schemadotorg``` to your ckan.plugins section in the .ini file.
* Add the following in your organization/read_base.html template
 
```
{% block scripts %}
  {{ super() }}
  {% if h.sdo_installed() %}
    {% snippet "snippets/organization_sdo.html",organization=c.group_dict %}
  {% endif %}
{% endblock %}
```

* Add the following in your package/read.html template

```
  {% block scripts %}
    {{ super() }}
    {% if h.sdo_installed() %}
      {% snippet "snippets/dataset_sdo.html",package=pkg %}
    {% endif %}
  {% endblock %}
```