
def setattr_with_obj(model,Form,fm):
    dic = Form.__dict__['base_fields'].__dict__['_OrderedDict__map'].keys()
    for key in dic:
        model.key =fm[str(key)]
    
