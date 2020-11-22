from pprint import pprint

from recursive_update import update


settings = {
    'alpha': {
        'Add': [],
        'Delete': [],
        'Patch': {
            'Software': False,
            'Hardware': False
        }
    },
    'beta': {
        'Flash': [],
        'Definitions': {
            'Occur': False,
            'Define': False,
            'Disable': False,
            'Enable': False
        }
    },
    'gamma': {
        'Allow': {},
        'Block': {}
    }
}

new_settings = {
    'alpha': {
        'Delete': ['model', 'structure'],
        'Patch': {
            'Software': True
        }
    },
    'beta': {
        'Definitions': {
            'Define': True,
            'Disable': True
        }
    },
    'gamma': {
        'Allow': {
            'Update': True
        }
    },
    'thetta': {
        'font': {
            'size': 12,
            'family': 'sans serif'
        }
    }
    
}

update(settings, new_settings)
