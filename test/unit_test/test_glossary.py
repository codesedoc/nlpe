from enum import Enum, auto
from nlpe.utils import Glossary, GLOSSARY_POOL

class GlossaryEnum(Glossary, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return Glossary(name)
    
class NameEnum(GlossaryEnum):
    A = auto()
    

def test_self():
    glossary = Glossary('glossary')
    
    new_glossary = Glossary(glossary)
    assert new_glossary == glossary
    assert Glossary(Glossary('glossary', update=True)) == Glossary('glossary', update=True)
    
def test_enum():
    g = Glossary("A")
    GLOSSARY_POOL.search(g)
    print(repr(NameEnum(g).value))
    assert NameEnum(g) == g
    assert isinstance(NameEnum(g),NameEnum)
    assert isinstance(NameEnum(g).value, Glossary)
    