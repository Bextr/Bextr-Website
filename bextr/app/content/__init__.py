import json
import markdown
from os.path import join, abspath, isabs, dirname, split
from yaml.constructor import ConstructorError
from yaml import (
    load as yaml_load,
    Loader,
    ScalarNode,
    SequenceNode,
    MappingNode)
from flask import Markup


cont_dir = abspath(dirname(__file__))


class YLoader(Loader):
    def __init__(self, stream):
        self._root = split(stream.name)[0]
        super().__init__(stream)
        YLoader.add_constructor('!include', YLoader.include)

    def include(self, node):
        if isinstance(node, ScalarNode):
            return self.extract_file(self.construct_scalar(node))

        elif isinstance(node, SequenceNode):
            result = []
            for filename in self.construct_sequence(node):
                result += self.extract_file(filename)
            return result

        elif isinstance(node, MappingNode):
            result = {}
            for k, v in self.construct_mapping(node).iteritems():
                result[k] = self.extract_file(v)
            return result

        else:
            print('Error: unrecognised node type in !include statement.')
            raise ConstructorError

    def extract_file(self, filename):
        return load(join(self._root, filename))


def _markup_hook(obj):
    if 'markup' in obj and obj['markup'] is True:
        mrk = markdown.markdown(obj['data'],
                                output_format='html5',
                                extensions=['markdown.extensions.extra'])
        return Markup(mrk)
    return obj


def _process_markup(obj):
    return json.loads(json.dumps(obj), object_hook=_markup_hook)


def load(f_path):
    f_path = f_path if isabs(f_path) else join(cont_dir, f_path)
    with open(f_path, encoding='utf-8') as file:
        return _process_markup(yaml_load(file, YLoader))


# Global content (header, footer, etc.)

c_global = load('global.yml')


# Top level pages

c_home = load('home.yml')
c_touchscreens = load('touchscreens.yml')
c_signage = load('signage.yml')
c_about = load('about.yml')
c_contact = load('contact.yml')


# Products

c_touch_tables = load('touch_tables.yml')
c_touch_windows = load('touch_windows.yml')
c_indoor_signage = load('indoor_signage.yml')
c_outdoor_signage = load('outdoor_signage.yml')
c_indoor_kiosks = load('indoor_kiosks.yml')
c_outdoor_kiosks = load('outdoor_kiosks.yml')
