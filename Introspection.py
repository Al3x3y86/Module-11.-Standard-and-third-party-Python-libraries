import inspect


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': 'main'
    }

    for attr in dir(obj):
        attr_value = getattr(obj, attr)
        if inspect.isfunction(attr_value) or inspect.ismethod(attr_value):
            info['methods'].append(attr)
        else:
            info['attributes'].append(attr)

    return info


number_info = introspection_info(42)
print({
    'type': number_info['type'],
    'attributes': number_info['attributes'],
    'methods': number_info['methods'],
    'module': number_info['module']
})
