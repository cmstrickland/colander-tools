import colander
from colander_tools import strict


def test_integer():
    # Serialization
    integer = strict.Integer().serialize({}, 4)
    assert(integer == 4)

    integer = strict.Integer().serialize({}, True)
    assert(integer == 1)

    try:
        integer = strict.Integer().serialize({}, "foo")
        raise
    except colander.Invalid:
        pass

    try:
        integer = strict.Integer().serialize({}, {})
        raise
    except colander.Invalid:
        pass

    # Deserialization
    integer = strict.Integer().deserialize({}, 1)
    assert(integer == 1)

    integer = strict.Integer().deserialize({}, True)
    assert(integer == 1)

    try:
        integer = strict.Integer().deserialize({}, "foo")
        raise
    except colander.Invalid:
        pass

    try:
        integer = strict.Integer().deserialize({}, {})
        raise
    except colander.Invalid:
        pass


def test_float():
    # Serialization
    float = strict.Float().serialize({}, 4.5)
    assert(float == 4.5)

    float = strict.Float().serialize({}, True)
    assert(float == 1)

    try:
        float = strict.Float().serialize({}, "foo")
        raise
    except colander.Invalid:
        pass

    # Deserialization
    float = strict.Float().deserialize({}, 4.5)
    assert(float == 4.5)

    float = strict.Float().deserialize({}, True)
    assert(float == 1)

    try:
        float = strict.Float().deserialize({}, "foo")
        raise
    except colander.Invalid:
        pass


def test_boolean():
    # Serialization
    boolean = strict.Boolean().serialize({}, True)
    assert(boolean is True)

    boolean = strict.Boolean().serialize({}, 1)
    assert(boolean is True)

    boolean = strict.Boolean().serialize({}, "foo")
    assert(boolean is True)

    boolean = strict.Boolean().serialize({}, {})
    assert(boolean is False)

    # Deserialization
    boolean = strict.Boolean().deserialize({}, True)
    assert(boolean is True)

    boolean = strict.Boolean().deserialize({}, 1)
    assert(boolean is True)

    boolean = strict.Boolean().deserialize({}, "foo")
    assert(boolean is True)

    boolean = strict.Boolean().deserialize({}, {})
    assert(boolean is True)


def test_string():
    # Serialization
    string = strict.String().serialize({}, "foo")
    assert(string == "foo")

    string = strict.String().serialize({}, True)
    assert(string == "True")

    string = strict.String().serialize({}, 1)
    assert(string == "1")

    string = strict.String().serialize({}, {})
    assert(string == "{}")

    # Deserialization
    string = strict.String().deserialize({}, "foo")
    assert(string == "foo")

    try:
        string = strict.String().deserialize({}, True)
        raise
    except colander.Invalid:
        pass

    try:
        string = strict.String().deserialize({}, 1)
        raise
    except colander.Invalid:
        pass

    try:
        string = strict.String().deserialize({}, {})
        raise
    except colander.Invalid:
        pass


def test_mapping():
    class Foo(colander.MappingSchema):
        schema_type = strict.Mapping

        foo = colander.SchemaNode(strict.String())
        bar = colander.SchemaNode(strict.String())

    try:
        Foo().deserialize({"foo": "bar"})
        raise
    except colander.Invalid:
        pass

    try:
        Foo().deserialize({"bar": "foo"})
        raise
    except colander.Invalid:
        pass

    correct = {"bar": "foo", "foo": "bar"}
    mapping = Foo().deserialize(correct)
    assert(mapping == correct)
