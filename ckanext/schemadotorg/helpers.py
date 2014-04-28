



def get_suborganizations(organization):
    import ckan.model as model
    org = model.Group.get(organization['id'])
    return org.get_children_groups(type='organization')
