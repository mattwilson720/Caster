from dragonfly import (IntegerRef, Integer)
from dragonfly.grammar.elements import RuleWrap, Choice
from dragonfly.language.base.integer_internal import MapIntBuilder
from dragonfly.language.loader import language

from castervoice.lib import settings
from castervoice.rules.core.alphabet_rules import alphabet_support # Conditional import load from user directory?

'''
Integer Remap feature needs to be rewritten:
    - allow customization
    - make it language sensitive (can this be done without eval?)
''' 
if not settings.settings(["miscellaneous", "integer_remap_crash_fix"]):
    class IntegerRefST(RuleWrap):
        def __init__(self, name, min, max, default=None):
            if not settings.settings(["miscellaneous", "short_integer_opt_out"]):
                content = language.ShortIntegerContent
            else:
                content = language.IntegerContent
                
            if "en" in language.language_map and settings.settings(["miscellaneous", "integer_remap_opt_in"]):
                content.builders[1] = MapIntBuilder(alphabet_support.numbers_map_1_to_9())

            element = Integer(None, min, max, content=content)
            RuleWrap.__init__(self, name, element, default=default)
            
else:
    print("Integer Remap switch: OFF")

    class IntegerRefST(IntegerRef):
        ''''''


class Boolean(Choice):
    def __init__(self, spec):
        Choice.__init__(self, spec, {spec: True})
