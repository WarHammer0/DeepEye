## Copyright (c) 2020 Attila Tőkés (tokes_atti@yahoo.com). All rights reserved.
## Licence: MIT

from DeepLib import *

def checkCreated(element, description):
    if not element:
        raise error("Failed to create Gst {}".format(description))
    return element

class GstElementFactory:

    @staticmethod
    def pipeline():		
        print("Creating Pipeline")
        pipeline = Gst.Pipeline()
        return checkCreated(pipeline, "pipeline")

    @staticmethod
    def element(type, properties = None):
        print("create_elem {}: props={}".format(type, properties))
        element = Gst.ElementFactory.make(type)
        if properties:
            for name, value in properties.items():
                element.set_property(name, value)
        return checkCreated(element, type)

    @staticmethod
    def capsFilter(caps):
        return GstElementFactory.element("capsfilter", \
            { 'caps' : Gst.caps_from_string (caps) } \
        )
